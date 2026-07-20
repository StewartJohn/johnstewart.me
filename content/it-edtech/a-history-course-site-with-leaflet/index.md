---
title: A History Course Site with Leaflet
date: '2019-06-26T21:27:55+00:00'
slug: a-history-course-site-with-leaflet
tags: []
summary: I’ve been interested in using digital maps to in history projects for a while
  now. My first big project on this was Situating Chemistry. This is a research database
  of places where chemistry …
originalUrl: https://johnastewart.org/dh/a-history-course-site-with-leaflet/
archiveUrl: https://web.archive.org/web/20240220230521/https://johnastewart.org/dh/a-history-course-site-with-leaflet/
lastmod: '2019-11-07T21:14:32+00:00'
cover:
  image: Screen-Shot-2019-06-26-at-3.47.14-PM.png
  alt: Screenshot of the 1945 website depicting the site's main world map with pins
    for student projects.
---

I’ve been interested in using digital maps to in history projects for a while now. My first big project on this was [Situating Chemistry](http://situatingchemistry.org). This is a research database of places where chemistry has been done. Each site can be linked to related people, documents, chemical processes, industries, etc.

![A screen shot of the world map in the Situating Chemistry database featuring data about 18th century Paris](SitChemScreenShot.png?resize=1024%2C596&ssl=1)

_Map of chemical sites in Paris, overlaid onto a map of Paris from 1790. You can interact with this map at [situatingchemistry.org/worldmap](http://situatingchemistry.org/worldmap)_

I presented on Situating Chemistry at a couple of DH workshops at OU, and eventually convinced Prof. Janet Ward to incorporate a similar project into one of her history courses. This Spring, she taught a course on 1945 focusing on the events at the end of the war and some of the more immediate cultural changes.

For Dr. Ward’s class, each student was asked to complete three assignments:

1. An analysis of a visual source including a painting or pamphlet or even physical object from 1945
2. An analysis of a primary textual source from 1945
3. And an analysis of a secondary history of 1945 or the war more generally

For each of these assignments, the students wrote a blog post on their own, free OU Create blogs.

I built a course hub that collected the students’ posts both in a menu and a map. Dr. Ward picked a map from the [David Rumsey Map Collection](https://www.davidrumsey.com/) and I embedded it into a WordPress site using the [Leaflet Map plugin](https://wordpress.org/plugins/leaflet-map/). Once the plugin was activated, I set up a home page for the site and then embedded the map using the Leaflet shortcode:

This loads the custom map as an image and sets the size of the map in the display. Then I added pins to the map for each of the student’s blog posts:

The leaflet-marker coordinates tells the system where to put the pin on the map. The Title, text, author, and link appears in the popup when you click on a pin for a given student project. Temidepelayo Ojekunle, the Office of Digital Learning student assistant, scanned the student’s posts for the course and put together a spreadsheet of titles, short summaries, authors, and links. Using the Leaflet-plugin’s tool for finding the coordinates, I then plotted each of the pins and copied over the information from the spreadsheet. The end result is [this site](https://1945.oucreate.com/):

![Screenshot of the 1945 website depicting the site's main world map with pins for student projects.](Screen-Shot-2019-06-26-at-3.47.14-PM.png?resize=1024%2C591&ssl=1)

_Screen shot of the 1945 course website showing the pins linking to student projects._

I really like the idea of accessing the content of the site both through the menu and through the map. I’ve been looking for web elements that are more interesting than a list, and I really like how the map draws you in and lets you see the focal clusters of the course.

In the next version of this site, for a future class, I’d like to use a tool like [MapTiler](https://www.maptiler.com/) to create tiles for the map, so that you don’t lose resolution as you zoom in on sections. I’d also like to get a better understanding of Leaflet’s resources for using and creating pin icons. I might even move out of WordPress and just use straight HTML since the WordPress php heavy and unnecessary for this type of site. I also hand-coded all the Leaflet pins in this project using the short code, but compiling a geo-json from some sort of form would have been far more efficient.