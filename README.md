# Django Task Manager

Django Manager is a web application for assigning and managing tasks. It's built with Python, Django, Django Rest Framework, PostgreSQL, and includes frontend adjustments using HTML, CSS, etc.

## Environment Configuration

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
## Database Setup

Ensure that your PostgreSQL database is configured and accessible. Update the database settings in the adequate .env file and update the ENV_PATH value in the setup.py file:
```python
ENV_PATH='.env.development'  # For development mode
ENV_PATH='.env.production'   # For production mode
```
## Run Application

Run the following command to start the server:
```bash
python manage.py runserver
```

## Usage
Visit the application in your web browser:

```bash
http://localhost:8000/
```