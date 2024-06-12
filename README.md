# Regatta Results Web Application

## Overview

The Regatta Results Web Application is designed to display race results for rowers, coaches, and officials. This application uses Django for the backend, a REST API for data handling, and HTML, CSS, and JavaScript for the frontend. It integrates with the Regatta Central API to fetch race results.

## Features

- User registration and authentication
- Profile creation and management for rowers, coaches, and officials
- Fetching and displaying race results using Regatta Central API
- Responsive design with a visually appealing registration form

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** SQLite (default for Django, can be replaced with PostgreSQL, MySQL, etc.)
- **API:** Django REST Framework

## Installation

. **Clone the repository:**
   bash
   git clone https://github.com/your-username/regatta-results.git
   cd regatta-results

   python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Access the application:
Open your browser and go to http://127.0.0.1:8000/.

## Usage
Registration and Login
Users can register by providing their details on the registration page. After registration, they can log in to access their profile and view race results.

# Contribution
If you would love to contribute to this please open an issue or submit a pull request.(Or contact me at sepitleleshilo69@gmail.com)

## Acknowledgments
Django![weather](https://github.com/SepitleFTW/The-Hub/assets/136067402/3991fa56-8675-4885-93ce-fa1929ed0d62)

Bootstrap
Open Weather API


