# Overview

The goal of this software was to build a cloud database that will hold data for a trivia web app. I wanted to be more familiar with how cloud data could be stored and manipulated in my personal environment.

I integrated the firebase admin and firestore libraries from Google in the python languages. I have a JSON file that holds secret service account information that connects to my python code as well. This allows my Firestore database to connect to my personal environment and allow me to enter data in through my python code. To add any data you want, you first create a variable that holds dictionary data of with a key value pair. Then you set that data to specific collection and document data that you want with the set() method. There are other methods you can use to manipulate the data like update() and delete() and you can retrieve data using get().

My purpose for writing this software is to understand the fundamentals of cloud databases and be more confident in understanding databases in general as well. 

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of the cloud database.}

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

I'm using Firestore database from Google. Google provides two cloud database platforms: Firebase, and Firestore. I was recommended to use Firestore and so far it's been great to use!

This database has a collection/table of some potential users which so far consist of fellow classmates and a few pieces of information from them. Ideally this user table would consist of login credentials and pertinant information for whatever service this would provide. This will be scaled up in the future to be used for a trivia web app to store login credentials and high score data.

# Development Environment

Developer tools consist of Visual Studio Code, github, and Google Firestore

Languages used: Python 3.9
Libraries used: firebase_admin and 'credentials' and 'firestore' libraries from firebase_admin

# Useful Websites

* [towards data science](https://towardsdatascience.com/nosql-on-the-cloud-with-python-55a1383752fc)
* [Cloud DB workshop](https://byui-cse.github.io/cse310-course/workshops/Cloud_DB/CSE310_Workshop_Cloud_DB.pdf)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Clean up unnecessary data
* Come up with a better structured system for storing data
* Understand how certain fields are ordered in Firestore