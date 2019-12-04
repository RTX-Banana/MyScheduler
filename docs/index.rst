Documentation!
==============

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Our Functions:
==============
Login::

    Takes a username and password so that the user can log in to their account.
    Takes 'form.username.data' and 'form.password.data'
    
Logout::

    Logs the user out of their account and goes back to the home page
    
Register::

    Takes username, password, and email to register the user into the database of existing users
    Takes 'form.username.data', 'form.password.data', and 'form.email.data'
    
Create::

    Creates an event containing a name, date, start time, and end time value
    Takes 'form.event_name.data', 'form.event_date.data', 'form.event_timeStart.data', and 'form.event_timeEnd.data'
    
Edit::

    Allows you to change any values of an existing event
    Takes 'form.event_name.data', 'form.event_date.data', 'form.event_timeStart.data', and 'form.event_timeEnd.data'
    
Delete::

    Removes an event from the database using its id
    Takes 'Event.query.get_or_404(i)'
    
Vacancy::

    Finds vacancies in your schedule based on existing events
    Takes 'form.event_date.data', 'form.event_timeStart.data', and 'form.event_timeEnd.data'

Tutorials:
==========

* :ref:`Login`
* :ref:`Logout`
* :ref:`Register`
* :ref:`Create`
* :ref:`Edit`
* :ref:`Delete`
* :ref:`Find a Vacancy`
