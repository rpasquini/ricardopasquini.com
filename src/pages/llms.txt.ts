import { getCollection } from "astro:content";
import type { APIContext } from "astro";

export async function GET(context: APIContext) {
  const site = context.site!.toString().replace(/\/$/, "");

  const posts = (await getCollection("posts"))
    .filter((p) => !p.data.draft)
    .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());

  const publications = await getCollection("publications");
  const workingPapers = publications.filter((p) => p.data.section === "working-paper");
  const refereed = publications.filter((p) => p.data.section === "refereed");

  const lines: string[] = [];
  lines.push("# Ricardo A. Pasquini");
  lines.push("");
  lines.push(
    "> Economist, Professor, and Researcher. Causal inference, econometrics, and the economics of digital markets. Associate Professor at Universidad Austral and Universidad Torcuato Di Tella; founder of Beta Sigma."
  );
  lines.push("");
  lines.push("## Key pages");
  lines.push(`- [About](${site}/about/): background, affiliations, research interests`);
  lines.push(`- [Publications](${site}/publications/): working papers, refereed publications, previous work by topic`);
  lines.push(`- [Teaching](${site}/teaching-docencia/): courses taught`);
  lines.push(`- [Blog](${site}/blog/): notes on econometrics, causal inference, DeFi, and data science`);
  lines.push(`- [RSS feed](${site}/rss.xml)`);
  lines.push("");

  lines.push("## Working papers");
  for (const p of workingPapers) {
    const link = p.data.links[0]?.url || "";
    lines.push(`- ${p.data.title}${link ? ` (${link})` : ""}`);
  }
  lines.push("");

  lines.push("## Refereed publications");
  for (const p of refereed) {
    const year = p.data.year ? `${p.data.year}. ` : "";
    const link = p.data.links[0]?.url || "";
    lines.push(`- ${year}${p.data.title}${link ? ` (${link})` : ""}`);
  }
  lines.push("");

  lines.push("## Recent blog posts");
  for (const post of posts.slice(0, 15)) {
    lines.push(`- ${post.data.title} (${site}/${post.data.slug}/)`);
  }
  lines.push("");

  return new Response(lines.join("\n"), {
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
}
