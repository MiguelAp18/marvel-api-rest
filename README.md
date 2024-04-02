## About The Project
<p>The purpose of this application is to create a backend that consumes the Marvel Official API to get all the heroes data. Once filtering the data is stored in a database and then perform read, update or delete operations. The app was developed using Flask and PostgreSQL</p>

## Installation
First, you need to download the project and install or simply clone it.

Enter to the project dir using a Terminal and type the next command to create the virtual environment:
```
python -m virtualenv env
```

To run the virtual environment:
```
.\venv\Scripts\activate
```

Next, type the following command to install all the dependencies:
```
pip install -r requirements.txt
```

## Setting up the DB
To connect the database, you need to create a new database in PostgreSQL using your username and password. Then you need to create your own environment variables using dotenv and check the database is up and running

## Execute app in dev environment
Once the database is connected the only remaining step is to run the following command in your terminal:
```
.\src\app.py
```


### Notes:
You can work with this backend using a frontend with a framework like React or Angular, or you can use a service like Postman or Insomnia to simulate that functionality
