# Python-Tasker

Python-Tasker is a simple, modular task tracking system built using Python. It allows users to create, update, and manage tasks easily, and serves as a solid base for expanding into a CLI or web-based productivity app.

To get started, clone the repository using:
git clone https://github.com/mohammedkausar/Python-tasker.git

Navigate into the project:
cd Python-tasker

Create and activate a virtual environment:
python3 -m venv .venv  
source .venv/bin/activate   # For Windows use .venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Create a .env file and add your configuration:
DEBUG=True  
SECRET_KEY=your-secret-key  
DATABASE_URL=your-db-url


Run the application:
python main.py

Features include task creation, viewing, marking as complete, and deletion. The application supports environment-based configuration, uses SQLite by default, and is structured for easy extension into a full-featured app.


Developed by Mohammed Kawuser.
