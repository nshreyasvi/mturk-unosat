# Mechanical Turk Annotation Tool for Satellite Imagery based Shelter Counting

**_Organization: UNOSAT (CERN Openlab 2018)_**

**_Supervisors: Lars Bromley, François Grey, Sofia Vallecorsa_**

**_Student: Shreyasvi Natraj_**

## Introduction
This project can be used in order to launch a mechanical turk web instance externally.
The project offers a customizable front end wherein a polygon can be drawn on top of a shelter image and a python back end which is intergrated to Amazon Mechanical Turk for deploying it in the form of a Human Intelligence Task on Amazon MTurk website. This project gives the ability generate rapid polygon data over several different refugee shelter satellite images in order to provide accurate figures regarding the amount of resources which is required in those refugee camps.

**Presently, this project has been tested on ubuntu 16.06 and must be compatible with windows 10.**

## Steps to set up Mechanical Turk:

**1) Install all dependencies** 
`pip install boto==2.46.1 boto3==1.4.4 botocore==1.5.88 matplotlib==2.0.2 numpy==1.12.1 numpydoc==0.6.0 Pillow==4.1.1`

**2) Get the Site deployed on Firebase and set up Amazon MTurk**
- Install firebase using `npm install -g firebase-tools`
- Login to Firebase Console `firebase login`
- Create a Firebase Project by going to the firebase website. 
- Open terminal and move into the `/toWeb` directory
- Run `firebase list` in terminal and see the project-id for the project that you just created
- Open the script ASCRIPT_INSTALL.py
- Copy and paste the firebaseProjectID inside `ASCRIPT_INSTALL.py` and `config.ini` under the right field in the file once you have hosted the page on firebase.
- Make a folder in `/toWeb/public/images/<your folder name>` and store all the satellite images here
- Run the `sudo python ASCRIPT_INSTALL.py`
- Set Up your MTurk Requester Account following [these instructions](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkGettingStartedGuide/SetUp.html#setup-aws-account). Make sure you complete all steps through Step 5 (setting up the developer sandbox). When making an IAM user, save your AWS Access and Secret Access keys somewhere safe
- Place your preferred username (doesn't matter what it is so long as you are consistent in your code), AWS Access, and AWS Secret Access Keys inside the `config.ini` For example, if you wanted to create access for a user named 'Student' with AWS Key 'ABCD' and AWS Secret Access Key '1234'

>[User name]
>awskey = Your AWS Key Here
>awssakey = Your AWS Secret Access Key
>would become

>[Student]
>awskey = ABCD
>awssakey = 1234

**3) Launching MTurk Campaign**
- Open the `ASCRIPT_begin.py` and `ASCRIPT_finish.py` file and change the values for the according to the requirement

| to change | value |
| --------------- | ----------- |
| folderToPublish | name of `<your folder name`>|
| user | add same username as config name |
| serverType | set 'production' for live event or developer for sandbox mode |
| imagesPerPerson | number of images to be classified as one HIT |
| hitBatch | folder in which results will be stored |

- The front end of the website can be changed by editing the HTML and Javascript code inside the `toWeb` folder
- When everything is done, run:
`sudo python ASCRIPT_begin.py`
- Go online to a link posted by the begin script when it is publishing hits. It will take you to the developer sandbox where you can see exactly what your HIT would look like to an actual user without having to pay them for it. Do a couple hits so you can test with data.

**4) Getting Results from MTurk** 
- When the campaign time ends, run 
1) Run `ASCRIPT_finish.py` and see some statistics about your HIT.

2) If no crashes occur, you have finished! Explore the images stored inside the data folder

3) The annotations for each image submitted to you will be stored in JSON Format (1 line per image) inside `all_submitted.txt`, a text file inside your specific hit batch folder. Learn more about the JSON format here

4) The JSON for the condensed images will also be stored in `condensed_all_submitted.txt`

5) A condensed image combines the annotations of everyone who annotated the same image into one line of JSON. For example, if three people annotated powerplants on top of an image independently, a condensed image would have all three polygons in the same line of JSON
6) All condensed JSON is stored in `condensed_all_submitted.txt`
7) A visual represntation of each condensed image, where each annotated feature is drawn, is stored in `allSubmittedCondensedImages`.

**5) Accepting/Rejecting HITs:**
- After running `sudo python ASCRIPT_finish.py`:
1) Run `sudo python ASCRIPT_hit_checker.py` script with the proper variables and accept or reject annotations. The hitcheker:
2) Reads through each line of `all_submitted.txt`
3) Generates an image of the annotations given the JSON data
4) Displays the image in a window and asks you to accept or reject the annotation
5) Accepts all assignments containing an image that you accepted and rejects those that contained no image that you accepted once you close out the hit_checker GUI. --folderNote: The only way to reject an assignment and not provide that Turker compensation is if you reject every image that they annotated. If you offered them 10 images to annotate and you rejected 9 of them, you will still pay them the full compensation for the 1 image you accepted.
5) Writes the line of JSON for each accepted annotation into `accepted.txt`
6) Rerun `sudo python ASCRIPT_finish.py`
7) The program will download new unreviewed data for hit checker to process
8) Creates condensed images using only accepted data.
9) The JSONS are stored in `condensed_accepted.txt`
10) The visual representations are stored in acceptedCondensedImages
11) Will begin populating data folder with confidence maps for each image and annotated object using only accepted data
Inside data, a folder will be created for each image annotated and it will be named the same as the image without the file extension.
12) Inside the image's folder will be a raw and normalized confidence map for each object annotated
13) The raw map contains, at every pixel, the number of people who thought this was part of a feature
14) The normalized map contains, at every point, the relative confidence of a point being part of a feature with the highest relative confidence having a value of 255, visualized as white, and the lowest having 0, visualized as black. Note that this is a relative confidence. An image that has a maximum of two people annotating any given point as a feature will show 2 as 255. Another image that has a max of 20 people annotating any given point will show 20 as 255. The normalized map is meant as an easy visualization. For data processing purposes, we recommend using the raw map.
