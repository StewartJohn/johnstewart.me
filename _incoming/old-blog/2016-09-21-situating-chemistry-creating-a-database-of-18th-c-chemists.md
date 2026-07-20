---
id: 488
title: 'Situating Chemistry: Creating a Database of 18th-c. Chemists'
slug: situating-chemistry-creating-a-database-of-18th-c-chemists
url: https://johnastewart.org/dh/situating-chemistry-creating-a-database-of-18th-c-chemists/
archive_url: https://web.archive.org/web/20231204031139/https://johnastewart.org/dh/situating-chemistry-creating-a-database-of-18th-c-chemists/
published: '2016-09-21T13:14:02+00:00'
modified: '2016-09-25T20:02:25+00:00'
category: DH
categories:
- DH
tags:
- Conference
- Digital Humanities
- Drupal
- History of Chemistry
excerpt: '*This post is the first section of a talk I gave at the 7th International Conference
  of the European Society for the History of Science. In 1756, fifty-nine students attended
  William Cullen’s (1710…'
featured_image:
  url: https://johnastewart.org/wp-content/uploads/2016/09/SitChemCreatePeople-1024x692.png
  alt: ''
embeds: []
recovered_from:
  category_archive_sources:
  - DH
  category_capture_timestamp: '20240810065157'
---

**This post is the first section of a talk I gave at the 7th International Conference of the European Society for the History of Science.*

In 1756, fifty-nine students attended [William Cullen](http://situatingchemistry.org/node/856) ’s (1710-1790) chemistry course at the University of Edinburgh. Amongst them was [George Fordyce](http://situatingchemistry.org/node/1029) (1736-1802) of Aberdeen who would go on to earn his medical degree from Edinburgh and become a lecturer of chemistry and medicine in London. He also wrote a book called the Elements of Agriculture and Vegetation that includes diagrams of his interpretation of Cullen’s teachings on the chemical attractions of particles. Although there is no monograph length biography of Fordyce, he has entries in the Dictionary of National Biography and the Dictionary of Scientific Biography and is a relatively well-documented individual.

![Page 83 of George Fordyce's Elements of Agriculture including diagrams of chemical particles](https://i0.wp.com/johnastewart.org/wp-content/uploads/2016/09/FordyceParticles.png?resize=178%2C300&ssl=1)

_George Fordyce’s 1783 diagram of chemical particles_

The other fifty-eight attendees of the course are less known. We know from Cullen’s notes that Robert Cumming was from Edinburgh, that John Richardson was from Northumberland, and that Henry Dunston was from some unspecified part of England. More surprisingly, at least two of the attendees were from Virginia—Thomas Clayton and James Taylor—and one was from Antigua—Christopher Hodge. Clayton, Fordyce, and eight other students would go on to earn their MDs from Edinburgh.

In designing the prosopographical part of the Situating Chemistry database, John Perkins and I wanted to ensure that we could capture structured, machine-readable data on someone like George Fordyce, or for that matter William Cullen. Additionally, we also wanted to be able to create records for people like Henry Dunston, for whom we had only a name and relationships of interest, in this case that he was a student in Cullen’s chemistry course, in Edinburgh, in 1756, with these other people, and he was from England.

Within Situating Chemistry, we assembled the structured data fields for collecting information about people with the assumption that a researcher would more often than not have incomplete data. The only required field is the title of the record. The fields to record dates of birth and death can be partially filled out when only a year or year and month are known. They can also be marked approximate to indicate ambiguity in the historical record.

[!\[Screen shot of the Situating Chemistry Database depicting the fields available for recording data about a person\](https://i0.wp.com/johnastewart.org/wp-content/uploads/2016/09/SitChemCreatePeople.png?resize=500%2C338&ssl=1)](https://i0.wp.com/johnastewart.org/wp-content/uploads/2016/09/SitChemCreatePeople.png?ssl=1)

The database was developed for the [‘Situating Chemistry, 1760-1840’ research group](http://situatingchemistry.org/About) and [funded](http://situatingchemistry.org/funding) in part by a grant from the [Netherlands Organisation for Scientific Research](http://www.nwo.nl/en), so we built it to accommodate the variety of different research projects being conducted by the research group. John Perkins has spent a great deal of time studying probate records to collect information about the relationships, business practices, personal belongings and wealth of French apothecaries and chemical manufacturers. In my research, I have focused instead on networks of education tracking the courses taken and taught in and around universities and the note sets related to those courses. Both of us are interested in the chemical substances and processes studied by our individuals as well as their correspondence.

The record for any individual can be linked to other individuals in several different ways. In addition to familial relations, we also have structured fields to collect information on instructor-student relationships and correspondents. There is also a somewhat generic person-to-person connection field that offers a list of relationships that can be expanded if and when needed. We designed the database such that every individual is the subject of their own record. A field denoting that a person was active in chemistry is automatically checked for every new record, but can be deactivated for familial relations, business partners, and others who are of interest but were not actively ‘doing’ chemistry even in the broadest definition.

In addition to linking a person to other individuals within the system, a person can also be linked to many other kinds of data. The database was initially conceived of as a way to catalogue sites of chemistry. We thus started the database with a table to collect information on apothecary shops, lecture halls, pharmaceutical manufactories, bleach fields, labs, etc. For a given site, the latitude and longitude of the site along with a modern address can be recorded along with information about the ownership and financial history of the site, the chemical activities associated with it, the organizational history, related images, documents, sources, etc. For each individual in the system, we display the sites that they owned and operated and also those additional sites that they were associated with.

After developing tables for the sites and people involved in chemistry, we developed further tables for chemical substances collections, courses, documents, events, images, letters, objects, organizations, primary and secondary sources, processes and techniques of chemistry, and archival and museum repositories. A person can be connected to any of these record types with an extensible series of extensible subject-predicate-object. For example a given individual could be a member of an organization or might have studied a particular chemical substance or been a practitioner of a particular process or technique of chemistry. Every record, whether it be for a person or any other type of data, can and should be sourced by linking it to primary and/or secondary sources. For the system as a whole then, we have tables for more than a dozen types of information and hundreds of structured data fields, all strung together into a relational web of information.

In its first conception, the Situating Chemistry database was thought of as a single table for sites with about a dozen fields. However, this variety of tables and fields grew organically through discussion of the research questions and practices that we, as historians of chemistry, conduct. The goal for the project was not to publish a completed set of sites or records, but rather to facilitate active research. A researcher could enter the data that they were collecting for a research project to organize and analyze the information, and they could take the database with them into the archives to continue to collect information. Researchers can access their records and add new records to Situating Chemistry from a laptop, tablet, or even a phone.

To accommodate both offline note-taking and the rapid upload of external data sets, the database has also been designed so that users can upload CSV files (excel-type tables). Any data in the system can in turn be downloaded as a CSV or in other structured formats including XML, RDF, and JSON. Because Situating Chemistry was designed as a research tool rather than a data-publication, the goal of the database is to allow users to both enter and access whatever fields and records sets they consider interesting. Several visualizations including tables, graphs, and a timeline are built into the system. The user can also extract whatever structured data they want to pull from the system, so that she can also generate her own visualizations using tools like Tableau or programming languages like Python and R.
