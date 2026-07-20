---
title: WordPress migration tip
date: '2019-07-09T15:58:47+00:00'
slug: wordpress-migration-tip
tags:
- DoOO
- OU Create
- WordPress
summary: This is largely a note to myself, but I hope it will be useful for anyone
  else who helps to administer a Domain of One’s Own project. I get a lot of requests
  from OU Create users to migrate a…
originalUrl: https://johnastewart.org/create/wordpress-migration-tip/
archiveUrl: https://web.archive.org/web/20240718235714/https://johnastewart.org/create/wordpress-migration-tip/
lastmod: '2019-07-17T14:08:00+00:00'
cover:
  image: pma-logo.jpg
  alt: phpMyAdmin logo
---

This is largely a note to myself, but I hope it will be useful for anyone else who helps to administer a Domain of One’s Own project.

I get a lot of requests from OU Create users to migrate a WordPress site from one user’s account to another or to create a forked version of a site.

The first part of this is relatively easy. Either download an existing backup of the site or go into the File Manager and create a zipped copy of the file structure for the site.

Next go into phpMyAdmin, select the database for the site and then export a copy.

Now, go to the cPanel for the new copy of the site. Make sure there is a domain/subdomain/or subdirectory ready to receive the files for the site. Upload and unzip the files.

The harder part is manually uploading the database. Go to MySQLDatabases and create a new DB and a new user. Assign the user to the DB and make sure to keep a copy of the password you set up for the user.

Now go back into the files for the new site. Open wp_config.php and update the lines that define the DB_NAME, DB_ USER, and DB_PASSWORD (usually something like lines 23-29 of that config file.

Last, you need to upload and update the DB. Go into phpMyAdmin, and you should see the DB you created a few minutes ago. Select this DB, and then import the copy of the DB from the old site. If successful, you should see all the tables and information from the old site.

Here’s the last bit that I learned today. There is a SQL command that will change every occurrence of the old URL for the site to the new URL for the site. I found this on [a post at a site called WPBeaches.com](https://wpbeaches.com/updating-wordpress-mysql-database-after-moving-to-a-new-url/):

In the site that I just migrated, that updated over a thousand values in the DB. As soon as I ran that, I was able to load the new forked copy of the site at its new URL.

*Edit: After initially writing this, I found one more thing that needs to be changed in the settings. Login to your WP dashboard and go to Settings->Media. There, you will likely need to change the path for where you want your media stored.

Last fun little tip. Go back to the cPanel, and click on WP like you’re going to install a fresh copy. There is a dropdown to the right of the ‘install this application’ button. One of the options there is “import existing install.” On the next screen, choose “From this account.” Then you will get a settings screen with a dropdown of domains, subdomains, etc. You can select the domain or subdomain where you just manually installed WP, and then click import. Now, you’re manually installed WP instance will show in your ‘myApps’ list from Installatron, and you can use the backup, cloning, delete, and auto-login features.