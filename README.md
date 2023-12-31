# Rollcall_Image_Recognition
Automated roll call system using Face Recognition for efficient attendance management
Take attendance of a class using the roll call system. 
The system uses face recognition to mark the attendance of the students.

Setup Instructions
Download PyCharm, MySQLWorkBench and set it up.

The following sections guide you through configuring, running, and deploying the system.
Clone the roll call repository
Clone the repository to your local machine:
git clone git@github.com:Nayanapm1/rollcall.git
Alternatively, you can download the system as a zip and extract it.

Setting up your local environment, virtual environment and the database.
Go to PyCharm --> Preferences --> Project Interpreter and download the below mentioned packages.

1.	Django
2.	Flask
3.	Jinja2
4.	MarkupSafe
5.	Pillow
6.	PyQt5
7.	PyQt5-sip
8.	TBB
9.	Werkzeug
10.	appdirs
11.	asgiref
12.	click
13.	distlib
14.	django-extensions
15.	dlib
16.	docopt
17.	face-recognition
18.	face-recognition-models]
19.	filelock
20.	itsdangerous
21.	joblib
22.	mysqlclient
23.	numpy
24.	pandas
25.	pip
26.	protobuf
27.	pydotplus
28.	pyparsing
29.	python-dateutil
30.	pytz
31.	scikit-learn
32.	scipy
33.	setuptools
34.	six
35.	sqlparse
36.	threadpoolctl
37.	virtualenv
38.	wheel

Setup the database localhost and set up a schema in the database. Update your database information on the "Settings.py" document under the "rollcall"
folder.

Run below mentioned commands in the PyChram terminal:
1.python3 manage.py makemigrations
2.python3 manage.py migrate (Helps in migrating the tables into the database)
3.python3 manage.py runserver 8000

After the server is run, when clicked on the link provided, you will land on the admin login page. The admin credentials needs to be predefined
in the database under the user table. Provide a username and a password in the "user" table and use those data to login to the system as admin.

The link for student login is http://127.0.0.1:8002/usermgnt/student. Even student login credentials should be pre-defined in the database in the
"user" table.
