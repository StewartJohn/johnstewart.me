---
title: My first plugin
date: '2015-08-28T23:52:22+00:00'
slug: my-first-plugin
tags:
- API
- Plugins
- Slack
- WordPress
summary: '*The opensource code for the BadgeOS_Slack integration plugin can be found
  at the OUDigilearn GitHub site: In my office (the University of Oklahoma’s Center
  for Teaching Excellence), we use …'
originalUrl: https://johnastewart.org/create/my-first-plugin/
archiveUrl: https://web.archive.org/web/20240810080306/https://johnastewart.org/create/my-first-plugin/
lastmod: '2019-11-07T20:56:45+00:00'
cover:
  image: Slack-food-300x225.png
  alt: ''
---

**The opensource code for the BadgeOS_Slack integration plugin can be found at the OUDigilearn GitHub site: [https://github.com/oudiglearn/BadgeOS_Slack-Integration](https://github.com/oudiglearn/BadgeOS_Slack-Integration)*.

In![Slack message board window](Slack-food.png?resize=300%2C225&ssl=1) my office (the University of Oklahoma’s Center for Teaching Excellence), we use [Slack](http://slack.com) for internal communication. Slack is a wonderful group messaging system. I can message a single co-worker about a project that we’re working on or taunt them after my Red Devils beat their Gooners. I can also post messages to office chat boards that anyone in the office can sign up for. Our #food_n_drink board regularly has updates on people’s lunch plans, and the #office_decor board was useful when we moved into our new space. There are also private groups where you can talk to your team, a sub group, or an interest group (e.g. our ball_is_life board that is devoted solely to basketball and soccer news). Slack combines the utility of person-to-person text messaging with group texting and thematic discussion boards.

One of my pet projects here has been to develop WordPress BadgeOS systems. I have been using BadgeOS to design a lightweight Learning Management System to incentivize skill based learning and combine those skills into lessons, units, and courses. As a test of the system, I also built a badging system for our office. The idea is that you get lightweight, relatively silly badges for doing the simple things that improve an office. If you bring donuts for the office you earn a Sweetie Pie badge. If you run an errand for someone to drop off a package or pick up a soda, you earn a Gopher badge. The first person to the office each day gets the Early Bird Badge, and if you work late, you get the Night Owl badge.

None of the badges have intrinsic value, but they offer some small degree of recognition for doing your work or doing something that improves the office. The system allows my colleagues to nominate our office mates for badges and allows me as the moderator to award some badges directly (the winner of the office’s NCAA Tourney Bracket Challenge for example). I was able to build out the system over the summer, and we are still tinkering with the exact names and descriptions of the badges. The main restriction on the system though is that my coworkers already have work on so many websites and systems that adding another to the daily checklist doesn’t make sense.

My solution was to integrate my badge system with Slack. I wanted to push notifications of BadgeOS achievements so that winners were notified in the office’s primary messaging system. Slack programmers along with a legion of open source coders on Github and the web generally have been adding Slack integrations to all sorts of other programs. There are several variations already in existence just for WordPress. However, there was not an integration built for BadgeOS. Trusting my 13 year old programming skills (I started college as a CS major learning java), I decided to build my own.

My refresher course on coding was fairly short. The API tutorials on [Codecademy](http://codecademy.com) and [Lynda](http://lynda.com) (OU now offers all it’s students and faculty full access) got me up to speed on the basics of API interactions. After reviewing the strong [WordPress](https://codex.wordpress.org/WordPress_APIs) and [BadgeOS](http://badgeos.org/developer-api-badgeos/) API guides, I was ready for the key step – forking established code.

For the uninitiated, [forking](https://en.wikipedia.org/wiki/Fork_(software_development)) is the practice of replicating something and then adapting the copy to your specific needs. Before starting any coding project, check to see what others have already done and think seriously about forking a project to fit your needs rather than writing from scratch. [Github](http://github.com) is built around this concept serving as a repository to a huge variety of open source code that can be refined, extended, or forked.

I started off by forking the JP bbPress Slack Integration which pushes BuddyPress forum posts to Slack. In this WordPress php plugin, [Josh Pollock](http://joshpress.net) pushed new BuddyPress posts and replies from WordPress to Slack’s incoming Webhooks. By encoding the BuddyPress posts in JSON text package, Josh could feed the posts into a Slack message board. My fork replaced the JSON package from the original plugin with a package derived from BadgeOS variables.

[!\[Side by side comparison of php code\](Integrations-side-by-side.png?resize=300%2C182&ssl=1)](Integrations-side-by-side.png?ssl=1)

In the original JP bbPress Slack Integration, a new bbPress post would trigger an add on function that posted to Slack’s incoming Webhook via API feed. In my fork, a BadgeOS achievement award triggers a similar add on function to Slack’s incoming Webhook. By replacing the trigger action and a few of the variables in the JSON package, I quickly adapted Josh’s plugin to my needs. Now, whenever my system awards someone a badge, it automatically sends that person’s first name, the badge title, and the link for the badge to Slack and displays a message in our #all_things_badge Slack board.

[!\[Slack message board window\](All-Things-Badge.png?resize=300%2C216&ssl=1)](All-Things-Badge.png?ssl=1)

On the small and immediate scale, my love of puzzle solving and my self-image as a digital researcher were sated. On a larger, more universal scale though, I proved (for myself at least) that someone with old, rusty programming skills and a vague mission could write useful code by forking already existing projects. In creating my first plugin, I found a useful, open source starting point and adapted it to the needs of my office and ultimately my students. Educational Technology does not have to be the domain of the large-scale, all-encompassing, professionally developed apps but can be incrementally built by teachers to fit our needs.