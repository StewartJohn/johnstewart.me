---
id: 1396
title: Checking the status for 5200 websites
slug: checking-the-status-for-5200-websites
url: https://johnastewart.org/create/checking-the-status-for-5200-websites/
archive_url: https://web.archive.org/web/20240416212946/https://johnastewart.org/create/checking-the-status-for-5200-websites/
published: '2019-07-02T16:14:51+00:00'
modified: '2019-07-02T16:14:59+00:00'
category: Create
tags:
- Create
- DoOO
- python
excerpt: OU Create The University of Oklahoma offers all of its students, staff, and faculty
  their own web domains through the OU Create program. Anyone who wants to can sign up for
  a free subdomain (someth…
featured_image:
  url: https://i0.wp.com/johnastewart.org/wp-content/uploads/2019/07/404.png?fit=720%2C408&ssl=1
  alt: image depicting a 404 error web page
embeds: []
recovered_from:
  blog_capture: https://web.archive.org/web/20240810065157/https://johnastewart.org/blog/
  post_capture_timestamp: '20240810065157'
---

## OU Create

The University of Oklahoma offers all of its students, staff, and faculty their own web domains through the OU Create program. Anyone who wants to can sign up for a free subdomain (something like yourname.oucreate.com) or pay $12/year for a top-level domain (something like yourname.com). We provide 5GB of storage, tech support, and workshops to help people get started.

Once someone has registered for OU Create, they can use the Installatron tool that is built into the system to launch a one-click install of WordPress, Drupal, Omeka, and about 150 other web-apps. Right now our Installatron logs show a little more than 5200 active installations of WordPress, accounting for more than 80% of all the active registered domains. This does not include the inactive installations of people who have deleted their accounts or left the university and taken their websites with them.

I’ve been curious for a while as to the status of all of these sites. How many of these installations are actively being used? How many were used for a course at some point but have not been updated for a while? How many installations were set up but never really used? Are there any sites that are glitching, and do the users know about those glitches.

## Checking Statuses

As an administrator, I can use the Installatron logs to see the URLs for all of the WordPress installations on a server. We have 5 servers, so I wrote a python script that will quickly pull that information from each server and compile it into one big list.

Next I wrote another [python script](https://gist.github.com/StewartJohn/af326231123f2fa226e85290cefca461) (the link goes to GitHub gist and the code is also written below) that ingested that list of URLs, went to each URL, and returned the “HTTP status code” for the site. A status code of 200 means that the site loaded as expected. A status code of 301, meant that the URL redirected me to another page that then loaded. A status code of 400, 401, or 404 meant there was some sort of error loading the page. There were also pages where the system couldn’t find anything, so I told my script to record these as “no connection.”

When I tested the script on a list of 50 URLs, it worked, but it took several minutes. When I tried to run it on all 5000+ URLs, it ran for over two hours with no end in site. Ultimately, I split the list up into five smaller lists, and ran the script simultaneously on each of the five lists. It worked, but I left it running overnight, so I’m not entirely sure how long it took. This morning I compiled the five output.csv files.

The end result was that 3800 sites loaded with no problem. An additional 1100 sites redirected once, and then loaded. I think many of these were simply making a minor edit to my URL by adding a “/” to the end, pushing me from something like mysite.oucreate.com/blog to mysite.oucreate.com/blog/.

Of the 23 sites that had 400 status errors, 9 were actually redirects, that the my system didn’t recognize for some reason. The other 14 have issues, and I’ll follow up with their owners to help them either fix the sites or delete them if they’re no longer using them.

The remaining 282 sites returned “no connection.” Many of these are smaller sites that were once installed as subdomains and subdirectories of main sites, but are no longer in use. Others are sites URLs that have expired. I’m going to follow up with the owners of these expired sites. Where they were intentionally allowed to expire, I can delete them from our system. Where they expired unintentionally and haven’t been noticed yet, we can see about re-registering them.

Once I get to a good place with these sites that returned 400 and 500, I’m going to run a third script to see how many of the sites that are working properly are in active use. If the site only has the Hello World blog post that comes with the software and the default theme, I will reach out to the owners to see if they want any help getting set up or want me to delete an unused account. After I get through all of these WordPress sites, I’ll go back to Installatron and run similar checks on the rest of the OU Create domains.
