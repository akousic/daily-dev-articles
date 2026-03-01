# Blogatto - A Gleam framework for building static blogs

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-01 03:45
- **Original:** https://blogat.to

## Summary

Blogatto A Gleam framework for building static blogs with Lustre and Markdown. Blogatto generates your entire static site from a single configuration: blog posts from markdown with frontmatter, static pages from Lustre views, RSS feeds, sitemaps, and robots.txt — all rendered via Maud components. Features - Blog posts from markdown — write in markdown with YAML frontmatter, Blogatto handles parsing, rendering, and output - Multilingual support — add index-it.md ,index-fr.md , etc.

## Key Takeaways

- alongsideindex.md for language variants - Static pages — map URL paths to Lustre view functions that receive the full list of blog posts - RSS feeds — generate one or more RSS 2.0 feeds with optional filtering and custom serialization - Sitemap XML — automatic sitemap generation covering static pages and blog posts - Robots.txt — configurable crawl policies with sitemap reference - Custom markdown rendering — override any markdown element’s HTML output via Maud components - Blog post templates — full control over the page layout wrapping each blog post - Static asset copying — copy CSS, images, and other assets into the output directory How it works You define a Config using the builder pattern, then call blogatto.build(config) .
- The build pipeline: - Cleans and recreates the output directory - Copies static assets - Generates robots.txt - Parses markdown files, extracts frontmatter, renders HTML, and copies post assets - Renders static pages from route view functions - Generates RSS feeds - Generates sitemap XML The output is a fully static site ready to deploy to any static hosting provider.
- Documentation | Guide | Description | |---|---| | Getting started | Installation, project setup, and your first build | | Example blog | Walkthrough of the complete example project | | Blog posts | Directory structure, frontmatter, multilingual support | | Configuration | Full configuration reference | | Markdown components | Customizing markdown rendering | | Static pages | Routes, view functions, and using post data | | RSS feeds | Feed configuration, filtering, and serialization | | Sitemap and robots.txt | Sitemap and crawler configuration | | Dev server | File watching, auto-rebuild, and live reload | | Error handling | Error types and recovery patterns | API reference Full API documentation is available on HexDocs.

---
_Auto-generated daily digest entry._
