# Python-Tasker

Python-Tasker is a simple, modular task tracking system built using Python. It allows users to create, update, and manage tasks easily, and serves as a solid base for expanding into a CLI or web-based productivity app.

To get started, clone the repository using:
git clone https://github.com/mohammedkausar/Python-tasker.git

Navigate into the project:
cd Python-tasker

Create and activate a virtual environment:
python3 -m venv .venv  
source .venv/bin/activate   # For Windows use .venv\Scripts\activate

# Install dependencies:
pip install -r requirements.txt

Create a .env file and add your configuration:
DEBUG=True  
SECRET_KEY=your-secret-key  
DATABASE_URL=your-db-url



Run the application:
uvicorn main:app --reload

Features include task creation, viewing, marking as complete, and deletion. The application supports environment-based configuration, uses SQLite by default, and is structured for easy extension into a full-featured app.

# API 
# create task - /task/create_task
Request body: 
{
  "title": "string",
  "description": "string",
  "completed": false
}

# get all task - /task/get-all-task

# signup - /auth/register
Request body: 
{
  "email": "ur@example.com",
  "password": "string",
  "confirm_password": "string"  -- optional
}

# login - /auth/login
Request body: 
{
  "email": "ur@example.com",
  "password": "string",
}


Developed by Mohammed Kawuser.
