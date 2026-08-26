---
title: Recovering a WordPress Site from the Internet Archive
date: 2026-08-17
slug: recovering-a-wordpress-site
tags:
  - WordPress
  - GitHub
  - AI
summary: I rebuilt my old blog thanks to the Internet Archive
lastmod: 2026-08-16T14:54:20+00:00
---
A couple years ago, I allowed my domain registration to expire and my WordPress site disappeared from the public web. I had hosted my blog along with dozens of other web apps with Reclaim Hosting since 2014 as part of the University of Oklahoma's OU Create program. 

I went from being one of the first users of OU Create to the primary admin for the system from 2016 until I left the University in 2024. During that time I helped to support something like 10,000 different faculty members and students build blogs, Drupal sites, Omeka archives, python apps, and flat sites, and I documented many of our initiatives in my blog. 

However, about a year after I left OU, Create was discontinued. My site, along with about 4,000 others were archived. Some were transferred over to individual accounts with Reclaim or other hosts, but the majority were backed up to an AWS archive and taken down.

While AI contributed to the decline of blogging (AI generated answers on Google have radically decreased click through traffic to websites including blogs), it also makes it much easier for someone like me to build a website. I have been thinking about and playing with alternatives to WordPress the entire time I have been working on the web. Despite it's continued market dominance (WordPress still drives something like 43% of websites), it's slow and bloated and the themes are still as hard to customize as they've always been. 

Maintaining a blog in Hugo or Jekyll or Bookdown used to be technically challenging, and I only know a few people who went that way during the height of WordPress. Now though, you can just ask Claude or ChatGPT to spin up a site and it's ready to go in a matter of minutes. The css theme packages and page layouts for each are daunting if you want to modify them by hand, but are again easy to modify using an LLM. 

So, I decided to build a new blog that loads faster and is easier to maintain using Claude and Hugo. I'm hosting it on GitHub, and a GitHub automation automatically converts every Markdown file that I commit into HTML for me. Standing up the new site took me less than an hour and most of that time was just looking at themes for the blog posts and customizing the home page layout. The biggest challenge was recovering all my blog posts from my defunct WordPress site. 
## Finding the Archive

The first step was finding a useful Wayback capture. I started with a saved capture of the blog index:

`https://web.archive.org/web/20240810065157/https://johnastewart.org/blog/`

That page gave me the recent post list. From there, each post could be opened through Wayback and inspected individually. I also checked specific known posts directly, especially when I remembered a title or had an old URL.

The important lesson here is that the Wayback Machine is not a single snapshot of a site. It is a collection of captures taken at different times. A blog index from August 2024 might link to posts whose best-preserved versions came from 2021, 2022, or 2024. So the recovery process had to treat each post as its own archival object.

## Scraping in Iterations

I did not begin with a full-site scrape. That would have been tempting, but it also would have made it harder to notice what was going wrong.

Instead, I started with a small batch: the three most recent posts. That let me test the structure of the recovered HTML and make decisions about what should be preserved.

For each post, the LLM scraper attempted to capture:

- Title
- Original URL
- Wayback source URL
- Publication date
- Modified date, when available
- Categories
- Tags
- Excerpt
- Featured image
- Post body
- Embedded media links

The LLM set up a new md file for each post, wrote the metadata into the YAML header, and wrote the body as markdown. Once that worked, I expanded outward: more posts from the blog index, then individual posts I knew were missing, then the "Top Posts" sidebar, and finally category archive pages.

The category archives became the second major discovery source. Some posts did not appear in the first blog index pages I could recover, but they were still listed under category pages.

Going category by category helped catch posts that would otherwise have been missed. It also surfaced a useful validation step: compare every post discovered in category archives against the WordPress "archive."

I had used several different themes during the life of my WordPress site, so Some pages used one set of HTML classes, while older pages used another. A scraper that worked for recent posts did not automatically work for older category pages. Iterating on the scrape with ChatGPT allowed me to capture posts and pages that I wrote over a decade with various tools and that had been captured on different dates by the Internet Archive.

## Why Markdown

The recovered site was WordPress, but the rebuilt site does not need to be. In fact, one of the goals of this project is to get away from the fragility and bloat of a database-backed personal site when a flat-file structure will do.

Each recovered post is now a Markdown file with front matter. That means the archive is readable even without Hugo, portable across static site generators, easy to version in Git, and easy to edit in a normal text editor.

A simplified front matter example looks like this:

```yaml
title: "OU Create 2.0"
date: 2022-03-23T15:41:07-05:00
categories:
  - Create
tags:
  - WordPress
url: "https://johnastewart.org/create/ou-create-2-0/"
archive_url: "https://web.archive.org/..."
```

I'm using Hugo for this next version of the site because it treats Markdown as a first-class content format. The theme decision is separate from the content recovery. I can choose a theme for post readability and taxonomy support, while customizing the home page independently. That means the new site can have a bespoke front page while still relying on the theme for the routine work of rendering posts and categories.

At the moment, I am leaning toward a minimal Hugo theme in the PaperMod family: clean, fast, readable, and not overly designed. The point is not to rebuild WordPress as it was. The point is to recover the writing and give it a simpler, more durable home.
## Indie Ed Tech

OU Create and some of the other similar DoOO projects have been wound down over the last few years as blogging has been repeatedly declared dead, both in journalism and higher ed. I find it ironic though that both the skills and the ethos of Indie Ed Tech that drove the adoption of web hosting programs at Mary Washington, OU, BYU, VCU and so many other schools are more relevant than ever now. 

The barriers to building on the web are lower than ever. Rather than relying on CMSs like WordPress to provide an overly structured and ultimately restrictive platform for students and faculty, we can focus on storytelling, UX, accessibility, and democratic access that an open web affords. I'm glad I was able to recover my old posts from the Internet Archive and I hope to contribute to a new era of Indie Ed Tech 