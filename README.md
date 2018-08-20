# Implementation of Mechanical Turk for Human Intelligence based Shelter Polygon Drawing
This project can be used in order to launch a mechanical turk web instance along with the URL for the same. 
The project offers a front end wherein a polygon can be drawn on top of a shelter image and a python back end which is intergrated to Amazon Mechanical Turk using AWS Key and Authentication Key.
Presently, this project has been tested on ubuntu 16.06 and must be compatible with windows OS.

# Steps to set up Mechanical Turk:
We recommend conducting this procedure inside a Python Virtual Environment. Please create and activate one with the python package virtualenv or conda if you are using Anaconda.

1) Clone this repository and install all dependencies. For a quick way to do this, try the following:
`$ pip install -r requirements.txt`
2) Get the Site deployed on Firebase
 Make a Google Account if you do not have one
- Install Firebase CLI (See Link). Complete at least through firebase login
- Login to Firebase Console
- Create a Firebase Project
- Open terminal and move into the MTurkAnnotationTool/toWeb directory
- Run firebase list in terminal and see the project-id for the project that you just created
- Open the script ASCRIPT_INSTALL.py
- Set the firebaseProjectID equal to your project-id
- Run the `ASCRIPT_INSTALL.py`
- Set Up your MTurk Requester Account following these instructions. Make sure you complete all steps through Step 5 (setting up the developer sandbox). When making an IAM user, save your AWS Access and Secret Access keys somewhere safe

Place your preferred username (doesn't matter what it is so long as you are consistent in your code), AWS Access, and AWS Secret Access Keys inside the config.ini For example, if you wanted to create access for a user named 'Student' with AWS Key 'ABCD' and AWS Secret Access Key '1234'

[User name]
awskey = Your AWS Key Here
awssakey = Your AWS Secret Access Key
would become

[Student]
awskey = ABCD
awssakey = 1234

3) Test if installation was successful by running the below scripts in order
`EXTENSION_PreprocessLargeImage.py`
`ASCRIPT_begin.py`
Go online to a link posted by the begin script when it is publishing hits. It will take you to the developer sandbox where you can see exactly what your HIT would look like to an actual user without having to pay them for it. Do a couple hits so you can test with data.

4) Open `ASCRIPT_finish.py` and change the variable hitBatch to the name of the folder inside hitBatches
5) Run `ASCRIPT_finish.py` and see some statistics about your HIT.

6) If no crashes occur, you have finished! Explore the images stored inside the data folder
7) After setting up the Firebase account run the following program
   `python ASCRIPT_begin.py`

# Downloading Data and Approving/Rejecting HITs
1) Run ASCRIPT_finish.py after setting the appropriate variables at the start of the script

2) The annotations for each image submitted to you will be stored in JSON Format (1 line per image) inside all_submitted.txt, a text file inside your specific hit batch folder. Learn more about the JSON format here

3) The JSON for the condensed images will also be stored in condensed_all_submitted.txt

4) A condensed image combines the annotations of everyone who annotated the same image into one line of JSON. For example, if three people annotated powerplants on top of an image independently, a condensed image would have all three polygons in the same line of JSON
5) All condensed JSON is stored in condensed_all_submitted.txt
6) A visual represntation of each condensed image, where each annotated feature is drawn, is stored in allSubmittedCondensedImages.
7) Run `ASCRIPT_hit_checker.py` script with the proper variables and accept or reject annotations. The hitcheker:
8) Reads through each line of all_submitted.txt
9) Generates an image of the annotations given the JSON data
10) Displays the image in a window and asks you to accept or reject the annotation
11) Accepts all assignments containing an image that you accepted and rejects those that contained no image that you accepted once you close out the hit_checker GUI. --folderNote: The only way to reject an assignment and not provide that Turker compensation is if you reject every image that they annotated. If you offered them 10 images to annotate and you rejected 9 of them, you will still pay them the full compensation for the 1 image you accepted.
12) Writes the line of JSON for each accepted annotation into accepted.txt
13) Rerun `ASCRIPT_finish.py`
14) The program will download new unreviewed data for hit checker to process
15) Creates condensed images using only accepted data.
16) The JSONS are stored in `condensed_accepted.txt`
17) The visual representations are stored in acceptedCondensedImages
18) Will begin populating data folder with confidence maps for each image and annotated object using only accepted data
Inside data, a folder will be created for each iamge annotated and it will be named the same as the image without the file extension.
19) Inside the image's folder will be a raw and normalized confidence map for each object annotated
20) The raw map contains, at every pixel, the number of people who thought this was part of a feature
21) The normalized map contains, at every point, the relative confidence of a point being part of a feature with the highest relative confidence having a value of 255, visualized as white, and the lowest having 0, visualized as black. Note that this is a relative confidence. An image that has a maximum of two people annotating any given point as a feature will show 2 as 255. Another image that has a max of 20 people annotating any given point will show 20 as 255. The normalized map is meant as an easy visualization. For data processing purposes, we recommend using the raw map.
