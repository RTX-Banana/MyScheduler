[![Build Status](https://travis-ci.com/Innocent-Fear/Cmpe131Team11.svg?branch=master)](https://travis-ci.com/Innocent-Fear/Cmpe131Team11)

# Myscheduler
Many people have trouble scheduling out their day, and they may have trouble finding vacancies in their schedules if they have too many things to do in the day. To help them out with this, we decided to create a web application that would allow people to find the vacancies in their schedule each day. Also, if they happen to be trying to find a time where they can work on a group project or want to find time to hang out with someone, the two users can exchange usernames to view the schedules of others.

## Heroku Link: https://myschedulercmpe131.herokuapp.com/

## Getting Started

This section is for people who want to try to make their own edits to the code.
To run the application, first either clone the repo with
```
https://github.com/Innocent-Fear/Cmpe131Team11.git
```
or download it as a zip.

Afterwards, use the following command to install the required packages
```
pip install -U -r requirements.txt
```
To run the application, use the command
```
python myscheduler.py
```

## Unit Test

Our 8 unit tests are in a file called test_main.py, which can be seen upon opening the repo.
To run the test cases, you will first need to install pytest if you do not already have it, so type the following command in your terminal if needed
```
pip install pytest
```
Afterwards, the following command can be typed into the terminal to run the unit tests.
```
pytest
```

## Home Page
The home page should be the first page the user is directed to. It basically welcomes the user to the myscheduler app and tells them to let us know their schedule. The Home Page has been completed and successfully does its assigned task.
## Register 
If you do not have an account, click the "Register" button at the top of the page in order to register an account. Once the button is pressed, enter your desired username, your email, and your desired password twice in order to confirm your password. Then, click the "Register" button underneath to finish registering an account. This feature successfully registers the user's account onto the database when we run the application.
## Login
If you do not already have an account, go register an account first. Afterwards, click the "Login" button at the top of the page then enter your username and password. Check the "Remember Me" box if you wish to stay logged in. This feature will successfully log the user in when we run the application.
## Logout
After being logged in, if you with to logout, click the "Logout" button at the top of the page in order to logout. This feature works will successfully log the user out when we run the application.
## Userpage
After being logged in, if you are not already on the userpage, hit the "Profile" button at the top of the page to go to the userpage. The userpage should display the user's schedule. The Userpage has been completed and successfully does its assigned task.
## Add event to your schedule (Create)
After being logged in, click the "Schedule Event" button at the top of the page in order to add your event to your schedule. After entering the event name, event date, event start time, and event end time, the user will click the "Finish" button underneath to add the event. The time should be entered on a 24 hr clock scale. The events will display on the userpage. This feature will successfully create an event for the user and display it on the userpage.
## Delete event from your schedule (Delete)
Once an event has been created, you can click the "Delete" button on the right side of the event, which is displayed on the userpage, to delete the event. This feature will successfully delete an event for the user and remove it from the user page.
## Edit a event in your schedule (Edit)
Once an event has been created, you can click the "Edit" button on the right side of the event, which is displayed on the userpage, to edit the properties of your event. The button will take you to an edit page where you can enter in an event name, event date, event start time, and event end time. The time should be entered on a 24 hr clock scale. Currently, all of the boxes have to be filled in order for the feature to allow you to push the "Finish" button at the bottom to commit the changes. However, this feature will successfully edit the properties of the event that the user wishes to edit.
## Find Vacancy
After being logged in and adding your desired events, press the "Find Vancancy" button on the userpage, and it show show you the vacancies in your schedule. The Find Vacancy feature has been implemented and successfully finds the vancancies in your schedule.
## Search User (Search)
After being logged in, click the "Search" to be redirected to the search page. In that page you can input a user's username. If they exist, then you will be redirected to a page to see all of their events. 
## Number of events in a day
In the userpage, under every table of days, the number of events in that day is counted and displayed.
## Notify if event is today
In the userpage, if a user has an event on the current day, they will be notified about that event.
## CSS
We have finished implementing CSS to our project. The changes can be seen when the code is ran. We combined our CSS and html files together, so there are no separate CSS files.
## Sphinx Documentation
Our documentation can be found under /Cmpe131Team11/docs/_build/html/index.html
