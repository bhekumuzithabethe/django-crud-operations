# django-crud-operations

#Overview
This is an employee management system, whereby a user or an admin can create, read, update and delete employee details.
The project is built using  #Django 4, HTML 5, CSS 3, and Bootstrap 5 with a Bootswatch theme.
---

#Prerequisites
1. [Python 3.8-3.12](https://www.python.org/)
This project uses Django v4.2.4. For Django to work, you must have a correct Python version installed on your machine. More information [Here](https://django.readthedocs.io/en/stable/faq/install.html)
1. [Visual Studio Code]([https://www.python.org/](https://code.visualstudio.com/))

---

#Installation
1.Create a virtual environment
From the root directory, run:
'''
  $ python -m venv venv
'''

1.Activate the virtual environment
From the root directory, run:
On macOS:
'''
  $ source venv/bin/activate
'''
On Windows
'''
  $ venv\scripts\activate
'''

1.Install required dependencies
From the root directory, run:
'''
  $ pip install requirements.txt
'''

1.Create an admin user to access the Django Admin interface
From the root directory, run:
'''
  $ python manage.py createsuperuser
'''
When prompted, enter a username, email, and password.

---

#Run the application
From the root directory, run:
'''
  $ python manage.py runserver
'''

# To view the application

Go to http://127.0.0.1:8000/.

#Copyright and License
Copyright © 2023 - current year Thabethe Programming. Code released under the MIT license.
