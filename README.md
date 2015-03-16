# <a name="Team-Stream_by_pleso.net"></a>Team-Stream by pleso.net[](#Team-Stream_by_pleso.net)

Team-Stream is a simple time tracking system designed for software developers team. It covers essential need - to answer a question: **"who is/was doing what?"**. Team-Stream tracks time, that developer have spent on the project, builds reports.  

## <a name="Requirements"></a>Requirements[](#Requirements)

*   web-server - its a web-based project
*   python
*   [Django framework](http://djangoproject.com/)

## <a name="Features"></a>Features[](#Features)

*   **multi-user** interface allows many people to work with
*   **multi-project**
*   minimalistic interface:
 *   start tracking a new activity by entering its title and pressing Enter
 *   continue existing activity by clicking on it
 *   cancel wrong activity
 *   shortcuts to the django-admin interface to edit if some tune up is required
*   saved activities are **grouped by the title**
*   **auto-highlight trac tickets** and resolve it to a link. _Example: #125 will became a link pointing to "[http://example.com/trac/ticket/125](http://example.com/trac/ticket/125)"_
*   **the list of all activities for the last few days** in chronological order
*   **time validation** — nobody can work on two activities simultaneously neither in future.
*   **minimalistic TODO** functionality with optional feature to plan activity for some date
*   short **day-review report** build into activities timeline
*   separate **html reports**:
  * by time period
  * by selected project

## <a name="Future_plans"></a>Future plans[](#Future_plans)

*   with respect to user's **time-zone**
*   **specific user roles** to limit access in django admin and to selected projects only
*   a **plugin for Firefox** for submitting tasks
*   make a tidy **design**. _(yeah, we just get used to the current)_

## <a name="Screenshots"></a>Screenshots[](#Screenshots)

### <a name="Main_view"></a>Main view[](#Main_view)

![](http://www.pleso.net/media/images/2009-12/team-stream-main.jpg) 

### <a name="Sample_report"></a>Sample report[](#Sample_report)

![](http://www.pleso.net/media/images/2009-12/team-stream-report.jpg) 
