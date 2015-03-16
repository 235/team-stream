# Team-Stream by pleso.net #


Team-Stream is a simple time tracking system designed for software developers team. It covers essential need - to answer a question: **"who is/was doing what?"**. Team-Stream
tracks time, that developer have spent on the project, builds reports.

## Requirements ##
  * web-server - its a web-based project
  * python
  * [Django framework](http://djangoproject.com/)

## Features ##
  * **multi-user** interface allows many people to work with
  * **multi-project**
  * minimalistic interface:
    * start tracking a new activity by entering its title and pressing Enter
    * continue existing activity by clicking on it
    * cancel wrong activity
    * shortcuts to the django-admin interface to edit if some tune up is required
  * saved activities are **grouped by the title**
  * **auto-highlight trac tickets** and resolve it to a link. _Example: #125 will became a link pointing to "http://example.com/trac/ticket/125"_
  * **the list of all activities for the last few days** in chronological order
  * **time validation** — nobody can work on two activities simultaneously neither in future.
  * **minimalistic TODO** functionality with optional feature to plan activity for some date
  * short **day-review report** build into activities timeline
  * separate **html reports**:
    * by time period
    * by selected project

## Future plans ##

  * with respect to user's **time-zone**
  * **specific user roles** to limit access in django admin and to selected projects only
  * a **plugin for Firefox** for submitting tasks
  * make a tidy **design**. _(yeah, we just get used to the current)_

## Screenshots ##
<br /><br /><br />
### Main view ###
![http://www.pleso.net/media/images/2009-12/team-stream-main.jpg](http://www.pleso.net/media/images/2009-12/team-stream-main.jpg)
<br /><br /><br /><br /><br /><br /><br /><br />
### Sample report ###
![http://www.pleso.net/media/images/2009-12/team-stream-report.jpg](http://www.pleso.net/media/images/2009-12/team-stream-report.jpg)