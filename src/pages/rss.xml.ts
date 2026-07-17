import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import type { APIContext } from "astro";

export async function GET(context: APIContext) {
  const posts = (await getCollection("posts"))
    .filter((p) => !p.data.draft)
    .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());

  return rss({
    title: "Ricardo A. Pasquini — Blog",
    description: "Notes on econometrics, causal inference, DeFi, and applied data science.",
    site: context.site!,
    items: posts.map((post) => ({
      title: post.data.title,
      pubDate: post.data.date,
      description: post.data.excerpt || undefined,
      link: `/${post.data.slug}/`,
      categories: [...post.data.categories, ...post.data.tags],
    })),
  });
}
