# Development

## Required Packages

**For Debian and Derivatives**
```bash
sudo apt install python3-venv
```

**For Fedora**

Virtual environment installed by default on Fedora.

**For Windows**

Python 3.x must be installed on your system(x64 recomended).
https://www.python.org/downloads/windows/

## Steps for running the project

**Get source code**

**USE HTTPS**
```bash
https://github.com/kaganndemirr/announcement-project.git
```

**USE SSH**
```bash
git@github.com:kaganndemirr/announcement-project.git
```

**Change directory**
```bash
cd announcement-project
```

**Create virtualenv with python on linux**
```bash
python3 -m venv env
```

**Create virtualenv with python on windows**
```bash
python -m venv env
```

**Make active virtualenv on linux**
```bash
source env/bin/activate
```

**Make active virtualenv on windows**
```bash
env\Scripts\activate
```

**Install requirements**
```bash
pip3 install -r requirements/base.txt
```

**Migrate database on linux**
```bash
./manage.py migrate
```

**Migrate database on windows**
```bash
python manage.py migrate
```

**Create cache table**
```bash
python manage.py createcachetable
```

**Add superuser**
```bash
python manage.py createsuperuser
```

**Run project on linux**
```bash
./manage.py runserver 0.0.0.0:8000
```

**Run project on windows**
```bash
python manage.py runserver 0.0.0.0:8000
```
