# The-Blog
Django Blog application
## About
A Django CRUD app. Features include User Authentication, CRUD operations.

## Technologies
- HTML
- CSS
- Javascript
- Django/python
- Postgresql/sqlite3

## Local Installation
Follow these steps if you want to install The-Blog locally.

```
git clone https://github.com/LoisaKitakaya/The-Blog && cd The-Blog/

# create and activate virtual environment
virtualenv env
source env/bin/activate

# install requirements
pip install -r requirements.txt

# run migrations to create database
python manage.py migrate

# create superuser
python manage.py createsuperuser

# run the app
python manage.py runserver
```

## Issues/Troubleshooting
The webapp might not be fully responsive on all devices, but should work fine on the standart desktop/laptop.

If you come across any bugs/issues with the code, feel free to open a [new issue](<https://github.com/LoisaKitakaya/The-Blog/issues>) in the repo. If you experience technical issues, you can always do a quick Google search to see if someone has encountered a similar Django-related issue before.

## Contributing
[Pull requests](<https://github.com/LoisaKitakaya/The-Blog/pulls>) are welcome. For major changes, please open an [issue](<https://github.com/LoisaKitakaya/The-Blog/issues>) first to discuss what you would like to change. Make sure to run tests and migrations as appropriate.
