import { useMemo, useState } from "preact/hooks";
import Fuse from "fuse.js";

export interface PubLink {
  label: string;
  url: string;
  kind: string;
}

export interface Publication {
  id: string;
  title: string;
  authors: string[];
  year?: number | null;
  order?: number | null;
  section: "working-paper" | "refereed" | "previous-work";
  topic?: string | null;
  links: PubLink[];
  abstract?: string | null;
  keywords: string[];
}

const SECTION_LABELS: Record<Publication["section"], string> = {
  "working-paper": "Working Papers",
  refereed: "Refereed Publications",
  "previous-work": "Previous Work by Topic",
};

export default function PublicationsFilter({ publications }: { publications: Publication[] }) {
  const [query, setQuery] = useState("");
  const [activeKeyword, setActiveKeyword] = useState<string | null>(null);

  const fuse = useMemo(
    () =>
      new Fuse(publications, {
        keys: ["title", "authors", "keywords", "abstract"],
        threshold: 0.32,
        ignoreLocation: true,
      }),
    [publications]
  );

  const topKeywords = useMemo(() => {
    const counts = new Map<string, number>();
    for (const p of publications) {
      for (const k of p.keywords) counts.set(k, (counts.get(k) || 0) + 1);
    }
    return [...counts.entries()]
      .sort((a, b) => b[1] - a[1])
      .slice(0, 16)
      .map(([k]) => k);
  }, [publications]);

  const results = useMemo(() => {
    let list = query.trim() ? fuse.search(query.trim()).map((r) => r.item) : publications;
    if (activeKeyword) {
      list = list.filter((p) => p.keywords.includes(activeKeyword));
    }
    return list;
  }, [query, activeKeyword, fuse, publications]);

  const grouped = useMemo(() => {
    const groups: Record<string, Publication[]> = { "working-paper": [], refereed: [], "previous-work": [] };
    for (const p of results) groups[p.section]?.push(p);
    // Working papers: most recent revision first, per the source page's
    // own stated ordering (captured in `order` at extraction time).
    groups["working-paper"].sort((a, b) => (a.order ?? Infinity) - (b.order ?? Infinity));
    // Refereed / previous work: most recent publication year first;
    // undated entries (all currently flagged needsReview) sink to the end.
    const byYearDesc = (a: Publication, b: Publication) => (b.year ?? -Infinity) - (a.year ?? -Infinity);
    groups["refereed"].sort(byYearDesc);
    groups["previous-work"].sort(byYearDesc);
    return groups;
  }, [results]);

  return (
    <div>
      <div class="filter-bar">
        <input
          type="search"
          placeholder="Search title, author, or keyword…"
          value={query}
          onInput={(e) => setQuery((e.target as HTMLInputElement).value)}
          aria-label="Search publications"
        />
        {topKeywords.map((k) => (
          <button
            type="button"
            class="chip"
            aria-pressed={activeKeyword === k}
            onClick={() => setActiveKeyword(activeKeyword === k ? null : k)}
          >
            {k}
          </button>
        ))}
      </div>

      {(["working-paper", "refereed", "previous-work"] as const).map((section) =>
        grouped[section].length > 0 ? (
          <section>
            <p class="section-label">{SECTION_LABELS[section]}</p>
            <ul class="pub-list">
              {grouped[section].map((p) => (
                <li id={p.id}>
                  <h3>{p.title}</h3>
                  <div class="meta">
                    {p.year ? `${p.year} · ` : ""}
                    {(() => {
                      const coauthors = p.authors.filter((a) => a !== "Ricardo Pasquini");
                      return coauthors.length > 0 ? `With ${coauthors.join(", ")}` : "";
                    })()}
                    {p.topic ? ` · ${p.topic}` : ""}
                  </div>
                  {p.abstract && <p class="excerpt">{p.abstract}</p>}
                  {p.links.length > 0 && (
                    <p>
                      {p.links.map((l, i) => (
                        <>
                          {i > 0 ? " · " : ""}
                          <a href={l.url} target="_blank" rel="noopener noreferrer">
                            {l.kind === "other" || l.kind === "venue" ? l.label : l.kind.toUpperCase()}
                          </a>
                        </>
                      ))}
                    </p>
                  )}
                  {p.keywords.length > 0 && (
                    <div class="tag-list">
                      {p.keywords.map((k) => (
                        <span class="tag">{k}</span>
                      ))}
                    </div>
                  )}
                </li>
              ))}
            </ul>
          </section>
        ) : null
      )}

      {results.length === 0 && <p>No publications match your search.</p>}
    </div>
  );
}
