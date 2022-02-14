# leave-app

## Local Setup
Before setting up, please make sure that you have Python3.6+ installed and running on your machine.

1.  Clone the repo:
```bash
  git clone https://github.com/nickmwangemi/leave-app.git
```

2. Change directory into the project folder:
```bash
  cd leave-app
```

3. Setup and activate the virtual environment:
```bash
  python3 -m venv env
  source env/bin/activate
```

4. Install Python dependencies:
```bash
  pip install -r requirements.txt
```

5. Run the Django database migrations to setup the initial database:
```bash
  python manage.py migrate
```

6. Create the superuser:
```bash
  python manage.py createsuperuser
```

7. Run the server:
```bash
  python manage.py runserver
```

The server should be available at [http://127.0.0.1:8000](http://127.0.0.1:8000), while the admin panel will be at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
