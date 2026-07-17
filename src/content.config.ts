import { defineCollection, z } from "astro:content";
import { glob, file } from "astro/loaders";

const posts = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/posts" }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    slug: z.string(),
    lang: z.enum(["es", "en"]).default("es"),
    categories: z.array(z.string()).default([]),
    tags: z.array(z.string()).default([]),
    excerpt: z.string().optional(),
    draft: z.boolean().default(false),
  }),
});

const publications = defineCollection({
  loader: file("./src/content/publications/data.json"),
  schema: z.object({
    id: z.string(),
    title: z.string(),
    authors: z.array(z.string()).default([]),
    year: z.number().nullable().optional(),
    order: z.number().nullable().optional(),
    section: z.enum(["working-paper", "refereed", "previous-work"]),
    topic: z.string().nullable().optional(),
    venue: z.string().nullable().optional(),
    links: z
      .array(
        z.object({
          label: z.string(),
          url: z.string(),
          kind: z
            .enum(["ssrn", "doi", "arxiv", "pdf", "repo", "venue", "other"])
            .default("other"),
        })
      )
      .default([]),
    abstract: z.string().nullable().optional(),
    keywords: z.array(z.string()).default([]),
    needsReview: z.boolean().default(false),
  }),
});

export const collections = { posts, publications };
