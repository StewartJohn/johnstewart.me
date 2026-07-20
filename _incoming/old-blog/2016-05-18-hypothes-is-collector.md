---
id: 261
title: Hypothes.is Collector
slug: hypothes-is-collector
url: https://johnastewart.org/tools/hypothes-is-collector/
archive_url: https://web.archive.org/web/20240708173410/https://johnastewart.org/tools/hypothes-is-collector/
published: '2016-05-18T16:25:38+00:00'
modified: '2019-04-11T14:23:50+00:00'
category: Tools
tags:
- Annotation
- API
- Digital Humanities
- GitHub
- Hypothesis
- Open Web
excerpt: One of my favorite online tools is Hypothes.is. It allows you to annotate web pages
  as you would a book. When you’re using Hypothes.is you can highlight text on a webpage or
  add notes. The to…
featured_image:
  url: https://johnastewart.org/wp-content/uploads/2016/05/HypCollector.gif
  alt: ''
embeds:
- type: youtube
  title: Hypothesis Animated Intro
  url: https://www.youtube.com/watch?v=QCkm0lL-6lc
  source_url: https://www.youtube.com/embed/QCkm0lL-6lc?feature=oembed
recovered_from:
  blog_capture: https://web.archive.org/web/20240810065157/https://johnastewart.org/blog/
  post_capture_timestamp: '20240810065157'
---

One of my favorite online tools is [Hypothes.is](http://hypothes.is). It allows you to annotate web pages as you would a book. When you’re using Hypothes.is you can highlight text on a webpage or add notes.

[Hypothesis Animated Intro](https://www.youtube.com/watch?v=QCkm0lL-6lc)

The tool can be used to take private notes, but it becomes all the more powerful when you use it for collaborative reading. By making your notes public or sharing them with a chosen group, you can share your take on a reading as you’re reading it. My colleague [Lauren Horn Griffin recently wrote on the uses cases for this web annotation](http://laurenhorngriffin.oucreate.com/uncategorized/using-hypothes-is/) within a university setting. She identified five possibilities

- Reading Accountability & Promoting Active Reading
- Collaborative Reading & Modeling
- Public-but-Independent Research
- Instructor Feedback/Self-Assessment
- Citations

You can launch the tool by appending “https://via.hypothes.is/” before a URL. To annotate this post you would visit [https://via.hypothes.is/https://johnastewart.org/tools/hypothes-is-collector/](https://via.hypothes.is/https://johnastewart.org/tools/hypothes-is-collector/). You can also download an extension for Chrome to be able to launch Hypothesis quickly on any website. Site builders can also install Hypothes.is directly into WordPress, Drupal, or Jekyll sites, or pretty much anything else that allows javascript.

Here is how a recent LA Review of Books article on Digital Humanities looks when viewing the public annotations:

[!\[A screenshot of an article in LA Review of Books on Digital Humanities with the Hypothesis tool active\](https://i0.wp.com/johnastewart.org/wp-content/uploads/2016/05/LARB_Hyp.png?resize=500%2C302&ssl=1)](https://via.hypothes.is/https://lareviewofbooks.org/article/neoliberal-tools-archives-political-history-digital-humanities/)

## Hypothes.is Collector

In order to make it easier to track activity in Hypothes.is, I created a program called [Hypothes.is Collector](https://docs.google.com/spreadsheets/d/1KtJZ3tC4uZJC6flHgFpHqMA62Dc5vSeku8dnGuo4UTM/copy). The idea is that you can type in user name, a URL, a tag, or a group ID and click the button to see all of the related annotations. The program will create a new sheet with an archive of up to 200 annotations based on the search terms. It will then create a third sheet that will count how many of these annotations were made on each URL in the set by each user.

[!\[HypCollector\](https://i0.wp.com/johnastewart.org/wp-content/uploads/2016/05/HypCollector.gif?resize=500%2C329&ssl=1)](https://i0.wp.com/johnastewart.org/wp-content/uploads/2016/05/HypCollector.gif?ssl=1)

As with Hypothes.is itself, I see several use cases for this. The original idea for the program was to allow a course instructor to quickly see the activity of their students. If an instructor asks her students to annotate three different articles, she could use this app to assess whether or not each student made their annotations. The easiest way to do this would be to set up a group in Hypothes.is for the class. The instructor could then enter the group ID and her user authorization token (a unique password that allows you to pull your private and group annotations) into the system. When she clicked the button, she would see an archive of the annotations and a count of activity for the students across the three readings.

Other use cases as I currently see them include:

- Studying how various tags are being used within Hypothes.is
- Tracking recent public activity for Hypothes.is
- Breaking down activity on a particular reading by user
- Tracking one of [Remi Holden’s](https://twitter.com/remiholden) annotation flash mobs

I built the Collector as an attempt to make it easy for people to access annotations in a format that could then be analyzed. I think the counter that gets built on the third sheet is handy, but it’s not going to be useful for everyone. As I continue to refine this project, I am going to add some different visualizations of the annotation archive and I will extend the number of annotations that can be pulled at a single time. I welcome feedback and feature requests and encourage everyone to modify the project to best suit their needs.

Please try out the new Hypothes.is Collector. You can follow this [link](https://docs.google.com/spreadsheets/d/133icqjeRM7ZGp2AiziV0XbCb6RkA4QoqIThp8xV5TlU/copy) to get a copy of the spreadsheet and collect annotations. You can also view or modify the code by choosing “Script Editor” from the Tools Menu.

[https://docs.google.com/spreadsheets/d/133icqjeRM7ZGp2AiziV0XbCb6RkA4QoqIThp8xV5TlU/copy](https://docs.google.com/spreadsheets/d/133icqjeRM7ZGp2AiziV0XbCb6RkA4QoqIThp8xV5TlU/copy)

## A few notes on the Code:

The code for the program (shared below) is written in Google Scripts. This is a modified javascript that features a library of functions to facilitate interaction within and between the Google Docs Apps. While writing this particular code, I learned a few tricks for collecting and passing the parameters for the API search and how to pass the authorization token. You can run Google’s version of a GET request, UrlFetchApp.fetch, woith or without an authorization token and other advanced options. To run it with the advanced options (to pass headers like authorization), I formatted the ‘headers’ as a js object, passed them into a second object called ‘options’, and then passed ‘options’ a parameter into UrlFetchApp.fetch.

This probably isn’t interesting to most people, but it took me a long time to figure out and opens the doors to all sorts of other APIs that require authorization. Google Script is a little particular and APIs vary, but I learned a lot about APIs while figuring out the authorization, search parameters, and how to parse the returned json. After writing an initial version of the code, I found better solutions to many of my questions in some of Jon Udell’s [Hypothes.is API code](http://jonudell.net/h/) – so thank you Jon and be sure to check out his site: [jonudell.net](http://jonudell.net).

The bit of code at the end that sets up the third spreadsheet for counting annotations by user and URL is also pretty nifty. I had to figure out how to use arrays to populate [Sheets ranges](https://developers.google.com/apps-script/reference/spreadsheet/range) and then played with [the archaic R1C1 notation](http://www.numeritas.co.uk/2013/09/the-%E2%80%98dark-art%E2%80%99-of-r1c1-notation/) to create dynamic formulas for the sheet. Feel free to hack at or extend the code for your own use. Chunks of the code may also be useful for working on other API projects. As with most of my work, feel free to take whatever is useful.

End of code
