# mturk-unosat
This project can be used in order to launch a mechanical turk web instance along with the URL for the same. 
The project offers a front end wherein a polygon can be drawn on top of a shelter image and a python back end which is intergrated to Amazon Mechanical Turk using AWS Key and Authentication Key.
Presently, this project has been tested on ubuntu 16.06 and must be compatible with windows OS.

#Steps to set up Mechanical Turk:
We recommend conducting this procedure inside a Python Virtual Environment. Please create and activate one with the python package virtualenv or conda if you are using Anaconda.

Clone this repository and install all dependencies. For a quick way to do this, try the following:
$ pip install -r requirements.txt
Get the Site deployed on Firebase

Make a Google Account if you do not have one
Install Firebase CLI (See Link). Complete at least through firebase login
Login to Firebase Console
Create a Firebase Project
Open terminal and move into the MTurkAnnotationTool/toWeb directory
Run firebase list in terminal and see the project-id for the project that you just created
Open the script ASCRIPT_INSTALL.py
Set the firebaseProjectID equal to your project-id
Run the ASCRIPT_INSTALL.py
Set Up your MTurk Requester Account following these instructions. Make sure you complete all steps through Step 5 (setting up the developer sandbox). When making an IAM user, save your AWS Access and Secret Access keys somewhere safe

Place your preferred username (doesn't matter what it is so long as you are consistent in your code), AWS Access, and AWS Secret Access Keys inside the config.ini For example, if you wanted to create access for a user named 'Student' with AWS Key 'ABCD' and AWS Secret Access Key '1234'

[User name]
awskey = Your AWS Key Here
awssakey = Your AWS Secret Access Key
would become

[Student]
awskey = ABCD
awssakey = 1234

Test if installation was successful by running the below scripts in order

`EXTENSION_PreprocessLargeImage.py`
`ASCRIPT_begin.py`
Go online to a link posted by the begin script when it is publishing hits. It will take you to the developer sandbox where you can see exactly what your HIT would look like to an actual user without having to pay them for it. Do a couple hits so you can test with data.

Open ASCRIPT_finish.py and change the variable hitBatch to the name of the folder inside hitBatches
Run ASCRIPT_finish.py and see some statistics about your HIT.
If no crashes occur, you have finished! Explore the images stored inside the data folder

2) After setting up the Firebase account run the following program
   `python ASCRIPT_begin.py`
