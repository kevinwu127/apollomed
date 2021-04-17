Questions:
1. Is this application going to be scaled for thousands, millions of users?
2. How concerned should I be about scraping, DDOS attacks, or high traffic time periods?
3. What service will this hypothetically be hosted on?

Assumptions:
1. First and Last names are <80 characters long and Hospital addresses are <300 characters long
2. All Hospitals are valid
3. Patients cannot have empty first or last names
4. Patients need a Hospital ID
5. Patient and Hospital IDs start at 1 and auto-increment

All mock Hospital data is in app/test.db

To run app:

Python version 3.9.0
> pip install -r requirements.txt
> export FLASK_APP=run.py
> flask run

Go to 127.0.0.1:5000
