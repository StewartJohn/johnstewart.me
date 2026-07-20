---
title: Duplicating Drupal
date: '2016-06-28T11:31:21-05:00'
slug: duplicating-drupal
tags:
- Create
- Digital Humanities
- Domain of One's Own
- Drupal
- Reclaim Hosting
summary: One of my big ongoing projects is an online Drupal database for the History
  of Chemistry called Situating Chemistry. The database connects the sites where
originalUrl: https://johnastewart.org/create/duplicating-drupal/
archiveUrl: https://web.archive.org/web/20210411103811/https://johnastewart.org/create/duplicating-drupal/
lastmod: '2019-11-07T14:57:30-06:00'
cover:
  image: AddOnDomain.png
  alt: ''
---

One of my big ongoing projects is an online Drupal database for the History of Chemistry called [Situating Chemistry](http://situatingchemistry.org). The database connects the sites where chemistry has been done (pharmaceutical factories and dispensaries, bleach and dye works, fertilizer plants, university lecture halls and labs, etc.) with physical materials and the people doing the work.

John Perkins and I have built the database as a tool for researchers. We hope that they will login to the site while visiting archives, libraries, or archeological sites and will take notes in the database – both for their own use and to share the basic facts with the rest of the field.

We also built the site in the hopes that it would serve as a model for other subfields within the history of science. We were recently asked for a copy of the database that could be appropriated for the history of astronomy.

To build this new version of the database, I took backups of the Situating Chemistry database and installed them as a new database on a temporary subdomain. Doing this was not entirely straight forward or well documented, so I wanted to document the steps in case they are useful for others:

1. Create a web space for your new Drupal install
2. Install Drupal
3. Overwrite the new file structure from your backup
4. Point Drupal to the correct DB
5. Overwrite the new DB from your backup

This workflow is fairly simple conceptually, but it requires using the either the cPanel, the command line, or in my case both. Below I’ve explained each step more fully from my own experience:

1. [Create a subdomain](http://create.ou.edu/docs/#setting-up-subdomains) – From the cPanel provided by my web hosting service, I created a subdomain that I could use to host the new database temporarily until I hand it over. [!\[Screenshot of the AddOn Domain function in the cPanel for Reclaim Hosting\](AddOnDomain.png)](AddOnDomain.png)
2. [Install Drupal](http://create.ou.edu/docs/#installing-applications-with-installatron) – My web hosting service (and all of the web hosting services I’ve used) has a one click installation of Drupal that will get the core of Drupal up and running. I used this to install a clean version of Drupal on the new subdomain and a clean database. Situating Chemistry uses a postgreSQL database rather than the usual mySQL database in order to support mapping modules for the sites of chemistry. However the steps are the same for whatever type of DB you might use. [!\[Screenshot of the Druapl installation page in Installatron in Reclaim Hosting\](InstallDrupal.png)](InstallDrupal.png)
3. [Replace the core Drupal file structure](http://create.ou.edu/docs/#accessing-your-files-through-the-file-manager) – Having just installed Drupal, I immediately deleted the entire file structure that the automated system had produced. I replaced this with the file structure from a copy of the backup of the Situating Chemistry database. In this way I was able to get the files for the themes and modules copied over. [!\[Screenshot of the Drupal Core files in FileManager\](CoreDrupal.png)](CoreDrupal.png)
4. Point this Drupal instance to the new DB – By reinstalling Drupal from the backup, I overwrote the file that tells Drupal which DB it’s using. I thus needed to change a file to reestablish the connection to the new DB and prevent any corruption of the Situating Chemistry DB. To do this, I opened the settings.php file which for Drupal is installed under the Sites/Default subdirectory. From a command line text editor, I changed the line that indicates which DB to use from the Situating Chemistry DB to the new DB. [!\[Screenshot of FileManager in Reclaim Hosting's cPanel\](DrupalSettings.png)](DrupalSettings.png)
5. Replace the empty new postgreSQL database with a backup – This was the hardest part of the process. From within the cPanel, [you can access database manager](https://www.phpmyadmin.net/support/). There you could theoretically be able to overwrite the new DB with your backup. However, I got a timeout error because of the size of my DB file. Instead I used the command line to overwrite the DB. After logging into my server, I uploaded a copy of the backed up DB to a temporary, non-public folder. I then used the chmod command to change the read-write options on the new database to give myself write privileges. Finally I used something like this to overwrite the old DB with the new: psql -W -U myUserName newDBname < backUpFileName. Once that was done running, I reversed the changes I made with chmod for security. [!\[Screenshot of Mac Terminal\](ShellDBOverwrite.png)](ShellDBOverwrite.png)

By going through this process, I was able to create pretty much an exact copy of the Situating Chemistry site that I have been working on. I am going to delete out the content from this copy to create a clean version of the project for adaptation as Situating Astronomy. I will leave the taxonomies and relationships that I’ve built, but will delete out the blog posts, logos, and other project specific information from the site.

I will also use the five step workflow to build a second copy of Situating Chemistry to use as a developmental site to test out new Drupal modules and to establish workflows for importing data into the database. I have been doing way too much testing on the production site, and have occasionally caused outages when I run into a module conflict or some other form of break in the system.