# harness-test
_Backend test_

### Clone repository 

git clone https://github.com/czam20/harness-test.git

### Create / Activate development environment (Windows)

virtualenv venv

_Then you must activate the development environment_

source venv/Scripts/activate

_Finally we are located inside the project folder_

cd harness_test

### Instalations  

_Now we must install the project requirements_

pip install -r requirements.txt

### Migrations

_Now the tables are created in the database with the migration_

python manage.py migrate

## Job

_At this point we must turn on the server to have the service active_

python manage.py runserver

_To create a job you must first create skills, to do this go to_

http://127.0.0.1:8000/jobs/skills/

_To create a job_

http://127.0.0.1:8000/jobs/create/

_To retrieve a job_

http://127.0.0.1:8000/jobs/pk/

example http://127.0.0.1:8000/jobs/1/

_To list jobs_

http://127.0.0.1:8000/jobs/list/

_To obtain how many jobs is each skill in_

http://127.0.0.1:8000/jobs/skills/count/

_To access the admin panel_

http://127.0.0.1:8000/admin/
