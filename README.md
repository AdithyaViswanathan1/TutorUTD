# OnlineTutoringApp



## Front end local setup guide:
I am using Visual Studio Code for this with the front/app folder open

Have project repo cloned to your computer

Install NodeJS https://nodejs.org/en/download
and verify installation with "node --v" and "npm --v"

Run "npm install -g @angular/cli" to install angular command line interface

may need "ng update typescript@4.9.3" if you get an error about cannot read property createAsExpression

Run "npm i" to install/update the project's npm packages

To run project locally go to the run and debug tab on the visual studio code sidebar then click run locally at the top of the panel. Once the task runs it should pop up a browser window with the application, if not check the vsCode console for a link to the localhost page. Alternatively run the command "ng serve" 
...


##Backend
Run backend with 'python manage.py runserver'

Ensure the following libraries are installed using pip:
Django
Pymysql
djangorestframework
django-storages
boto3
pip install django-cors-headers
pip install duo_client
