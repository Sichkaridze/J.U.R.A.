# J.U.R.A. – Job Utility & Responsibility Automator
(Автоматизація роботи та відповідальностей)

## Overview
J.U.R.A. is a task management system designed for IT companies, built with Django and Bootstrap. The project provides efficient task tracking, team management, and project organization features.  
## Features
- Task and project management
- User authentication and role-based permissions (will be soon)
- Search and filtering functionality
- Responsive Bootstrap UI

## Installation and Setup

Before running the project, follow these steps:

### 1. Clone the Repository

```sh
  git clone https://github.com/Sichkaridze/J.U.R.A..git
```
```sh
  cd J.U.R.A.
```


### 2. Rename the Environment File
Before starting, rename the `.env_sample` file to `.env`:
```sh
  mv .env_sample .env
```

### 3. Create and Activate Virtual Environment
```sh
  python -m venv venv
```
```sh
  source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies
```sh
  pip install -r requirements.txt
```

### 5. Apply Migrations
```sh
  python manage.py migrate
```

### 6. Create a Superuser (Optional)
```sh
  python manage.py createsuperuser
```
Follow the instructions to set up the admin credentials.

Or use the existing one:

#### Username: Admin
#### Password: SampleAdmin

### 7. Run the Development Server
```sh
  python manage.py runserver
```

Now, open `http://127.0.0.1:8000/` in your browser to access the application.

## Project Structure
```
J.U.R.A/
│── JuraDjangoProject/       # Django project settings
│── static/                  # Global static files
│── task_manager/            # Main application
│   ├── mixins.py            # Custom mixins
│   ├── models.py            # Database models
│   ├── views.py             # Views for different modules
│── templates/               # Global templates
│── .env_sample              # Sample environment configuration
│── manage.py                # Django management script
│── requirements.txt         # Dependencies
```



## Technologies Used
- **Backend:** Django
- **Frontend:** Bootstrap, Crispy Forms
- **Database:** SQLite (default, can be switched to PostgreSQL)


---
**Author:** Dmytro Sichkar  
**Contact:** dima.sichkar2003@gmail.com 
