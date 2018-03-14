# CS Syllabus International Computer Science Syllabi Repository


The computer science faculty values free exchange of ideas, availability of open source
software, open publications, exchange of pedagogical advances, etc. Yet, upon entering the
web site of a particular institution understanding the graduation requirements is often a real
challenge and tracking the syllabus of a specific course can be a daunting undertaking. The
goal of this project is to create a national repository of computer science course syllabi to assist
students in making good educational choices, instructors in sharing best practices, and
education researchers in understanding the evolution of our field.


## Prerequisites 

* Python 3.6
* Django 1.11.5 final
* PostgreSQL 9.6
* Web browser (Chrome preferred)

## Installing

* Install all the software mentioned in the prerequisites or make sure all of them are already installed.
* Run Pgadmin and create a database with following credentials: 
```
'NAME'      : 'SER517',
'USER'      : 'npiedy',
'PASSWORD'  : 'root',
'HOST'      : 'localhost',
'PORT'      : '5432',
```
* Open a terminal and change directory to *.../mainsite* and run the following command.
```
manage.py makemigrations
```

* And then run the following command.
```
manage.py migrate
```
## Launching
* Open a terminal and change directory to *.../mainsite* and run the following command.

```
manage.py runserver
```

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [React.js](https://reactjs.org/) - Frontend framework used
* [Python](https://www.python.org/) - Language used
* [Bootstrap](https://www.python.org/) - Frontend tools
* [Github](https://github.com/) - Repository tools

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* Catalin Roman - The sponsor for this project. 
* Robert Reimar Heinrichs - Our professor who gave us great advice and kept us on track. 
