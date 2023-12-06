# TutorUTD
This is a web based tutoring application in order to help connect students and tutors in a simple and efficient way. To do this we have used a stack of modern technologies and coding languages including Angular, Django, MySQL and AWS hosting. By accomplishing this, students are able to find and book tutors with expertise on the exact courses they need help in and succeed academically. 

Project for CS 4485 Team 63. Faculty Advisor Dr. Pushpa Kumar. 

Team: 
- Jack Wittenbrook
- Mason Kuehne
- Chloe Lee
- Adithya Viswanathan
- Sam Salinas
- Vincent Tran-Bui

Note: Due to differing permissions, the following commands could require administrator privileges and thus `sudo` as a prefix. Example: `sudo npm i`. It is recommended whoever is running this program, that they have administrator privilieges on their local machine.

## Frontend Setup
Recommended: Visual Studio Code with the TutorUTD/front/app folder open

**All Front-end installations should be done in inside the /TutorUTD/front/app directory**

Have project repo cloned to your computer (git needs to be installed)

Install NodeJS https://nodejs.org/en/download
and verify installation with `node --v` and `npm --v`

Alternative: `node -v` and `npm -v`

Run `npm install -g @angular/cli` to install angular command line interface

may need `ng update typescript@4.9.3` if you get an error about cannot read property createAsExpression

Run `npm i` to install/update the project's npm packages


## Backend Setup
Recommended: Visual Studio Code with the TutorUTD/back folder open

Required: Local installation of Python (Developed with 3.1)

**All Back-end installations should be done in inside the /TutorUTD/back directory**

Ensure the following libraries are installed using pip:

- django
- pymysql
- djangorestframework
- django-storages
- boto3
- django-cors-headers
- duo_client

Additionally, the file `secrets.json` (given as part of submission files) has to be placed in TutorUTD/back directory for final website to work. It is not included in the git repository for security reasons. This file should remain confidential.

## Run Application
### BACKEND

Run command `python manage.py runserver` in TutorUTD/back directory. Alternative: `python3 manage.py runserver`

### FRONTEND 

Run command `ng serve` in TutorUTD/front/app directory. Alternatively, go to the run and debug tab on the visual studio code sidebar then click run locally at the top of the panel. Once the task runs it should pop up a browser window with the application, if not check the vsCode console for a link to the localhost page. 

Final website will be at the URL address given by `ng serve` command.

**IMPORTANT: In order for app to work, both frontend and backend commands have to be running in their respective directories.**
