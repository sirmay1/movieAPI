# movieAPI 08/12/2023
Created A movie API similar to Rotten Tomatoes reviews but in API style
Created this project to improve my skills in created real world API's
Within the array (JSON FILE) there are 40 objects.
40 movie reviews total for this API file.

STEPS:
-created a directory project folder called movie_api.
-created within the directory a folder called env to store my local environment files.
- created a local environment by typing within the terminal: python3 -m venv rottentomatoes
- pip install djangorestframework
- pip install --upgrade pip
- django-admin startproject movieranks
- cd into project
- python3 manage.py migrate
- python3 manage.py run server
- stop server
- django-admin startapp movieapp
- cd movieapp
- touch serializers.py
- touch urls.py
- created models
- create logic for file serializers.py
- created logic for views.py
- created logic for urls.py within app
- created logic for urls.py within project
- tested API and it works
- pushed project to Github
- project completed.
