# Cerebrico

> __"Well you know, for my experience, your head's for having ideas, not for holding them."__ -_David Allen_

## Overview
Cerebrico is a fast note-taking app that stands on the Markdown syntax and allows customization. 
It can be adapted to your preferences by the usage of custom keywords which generate html code.
It is fast, minimalistic and really easy to use.

## Installation

##### Steps:

> [!NOTE]  
> Prerequisites:
> Python 3+

1. Clone the repository
- `git clone git@github.com:TsvetomirTsvetkov/cerebrico.git`
2. Navigate to the __cerebrico__ folder
- `cd cerebrico`
3. Create a virtual environment
- `python3 -m venv .venv --prompt cerebrico`
4. Set the virtual environment
- `source .venv/bin/activate`
5. Install the dependencies
- `pip install -r requirements.txt`
6. Create a __PostgreSQL__ Database
- `sudo -u postgres -i`
- `psql postgres`
- `CREATE DATABASE <db_name>;`
7. Create __.env__ file
- `touch .env`
8. Fill the file with the secret credentials
> [!NOTE]  You can use [this](https://www.miniwebtool.com/django-secret-key-generator/) tool to generate a new secret key 
- SECRET_KEY=\<secret_key\>
- DB_NAME=\<db_name\>
- DB_USER=\<db_user\>
- DB_PASSWORD=\<db_password\>
- DB_HOST=\<db_host\>
- DB_PORT=\<db_port\>
9. Apply migrations
- `python manage.py migrate`
10. Make migrations for the apps and apply them
- `python manage.py makemigrations notes profiles authentication`
- `python manage.py migrate`
11. Start the local server
- `python manage.py runserver`
12. The application should be available [here](http://127.0.0.1:8000/)


## License

[MIT Licence](LICENSE)
