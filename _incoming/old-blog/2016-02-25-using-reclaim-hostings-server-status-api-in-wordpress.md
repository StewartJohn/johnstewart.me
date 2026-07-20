---
id: 199
title: Using Reclaim Hosting’s Server Status API in WordPress
slug: using-reclaim-hostings-server-status-api-in-wordpress
url: https://johnastewart.org/coding/using-reclaim-hostings-server-status-api-in-wordpress/
archive_url: https://web.archive.org/web/20230327192107/https://johnastewart.org/coding/using-reclaim-hostings-server-status-api-in-wordpress/
published: '2016-02-25T20:14:00+00:00'
modified: '2016-02-25T20:14:00+00:00'
category: Coding
categories:
- Coding
tags:
- API
- Create
- GitHub
- Reclaim Hosting
- University of Oklahoma
- WordPress
excerpt: I am extremely excited about a server status page that I just published for OU Create.
  The page simply displays the current status, operational or otherwise, of the two Reclaim
  Hosting servers that…
featured_image:
  url: https://s0.wp.com/i/blank.jpg
  alt: ''
embeds: []
recovered_from:
  blog_capture: https://web.archive.org/web/20240810065157/https://johnastewart.org/blog/
  post_capture_timestamp: '20230208012729'
---

I am extremely excited about a [server status page](http://create.ou.edu/server-status) that I just published for [OU Create](http://create.ou.edu).

The page simply displays the current status, operational or otherwise, of the two [Reclaim Hosting](http://reclaimhosting.com) servers that run our OU Create service. The page itself is boring and purely information, but the code that powers it is exciting to me.

After a recent, short outage, Tim Owens at Reclaim Hosting and Tom Woodward at VCU entered a conversation about using RSS to post notifications of outages for each of the schools using Reclaim Hosting servers.
 [@twoodwar](https://twitter.com/twoodwar) Very new setup for us but has an API [https://t.co/rGfAtrM5Ya](https://t.co/rGfAtrM5Ya) Let’s see what’s possible. Nothing automated yet. — Reclaim Hosting (@ReclaimHosting) [February 24, 2016](https://twitter.com/ReclaimHosting/status/702544236365877249)

Drawing on this new Server Status API, [Tom wrote a Google Script](http://bionicteaching.com/server-up-notifications-via-twittergoogle-script/) that would post a tweet on the ALTLab Twitter account whenever the servers were down. Tom’s code runs an HTTP GET request against the Reclaim API every five minutes. It then parses the response json file to check whether their server is ‘Operational.’ If it is, nothing happens. If it’s not, then the system generates a tweet.

Inspired by Tom’s work, I wanted to use the API to add server-status page to the OU Create account. To do this, I added [a plug-in called ‘Insert php’](https://wordpress.org/plugins/insert-php/) to the WordPress account for OU Create that allows us to write php code directly into posts and pages and display the results. I then used Google and advice from our coding guru, Kerry Severin, to write this short php code.

The code first runs WordPress’s version of the HTTP GET operation to pull in the Reclaim Hosting server status information as a string – an unstructured list of characters. Then it uses a php function to parse those characters into an array of json attributes. Next, it sets variables equal to relevant pairs within that array to read the status of the two OU servers. The final If/then command prints the status of the servers with either a green check mark if they are operational or a red ‘X’ if they’re not (these images were modified from Wikimedia files and would need to be modified when adapting this code).

hosted with ❤ by

This code is shared on GitHub and should be readily adaptable for anyone else who wants to produce a similar WordPress page. Simply change out the php header and closing tags as per the instructions in the ‘Insert php’ plugin. Then change the number of your server and get rid of code for the second server. Don’t forget to change the urls for the image files (ours were open-sourced from Wikimedia).
