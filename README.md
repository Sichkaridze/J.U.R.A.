# J.U.R.A. – Job Utility & Responsibility Automator
(Автоматизація роботи та відповідальностей)

## Live Demo

The project is deployed on Render:  
(To open in a new tab: **Cmd + click** or **Ctrl + click** )  

🔗 [J.U.R.A. Live Demo](https://j-u-r-a.onrender.com/) 

Credentials for DEMO:
 - #### Username: Admin
 - #### Password: AdminSample

🕒 Please note: Since the application is hosted on a free-tier service,
it may take about a minute to start if it’s been inactive.
The server automatically shuts down after 15 minutes of inactivity.

## Here are some sneak peeks of how it may look when you open the link 👇

<img width="1680" alt="Screenshot 2025-02-18 at 19 38 48" src="https://github.com/user-attachments/assets/e812c614-902e-4156-a4fa-eb1e72bc5e22" />  

---  

<img width="1680" alt="Screenshot 2025-02-18 at 19 38 34" src="https://github.com/user-attachments/assets/be74536f-65b2-4e86-bd29-3acc17c04dad" />

## Overview
J.U.R.A. is a task management system designed for IT companies, built with Django and Bootstrap. The project provides efficient task tracking, team management, and project organization features.  
## Features
- Task and project management
- User authentication and role-based permissions (will be soon)
- Search and filtering functionality
- Responsive Bootstrap UI

## Technologies Used
- **Backend:** Django
- **Frontend:** Bootstrap, Crispy Forms and Custom Styles
- **Database:** SQLite (default, can be switched to PostgreSQL)

---

**Author:** Dmytro Sichkar  
**Contact:** dima.sichkar2003@gmail.com 

---

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
  mv .env.sample .env
```

### 3. Create and Activate Virtual Environment
```sh
  python3 -m venv venv # On Windows: python -m venv venv
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

### 6. Collect Static Files

Before running the project in a production-like environment, collect static files:
```sh
  python manage.py collectstatic --noinput
```
This will gather all static files into the directory staticfiles/.
### 7. Create a Superuser (Optional)
```sh
  python manage.py createsuperuser
```
Follow the instructions to set up the admin credentials.

Or use the existing one:

#### Username: Admin
#### Password: AdminSample

### 8. Loading Test Data

To populate the database with test data, use the following command:

```sh
  python manage.py loaddata test_data.json
```

### 9. Enable Django Support in PyCharm (Optional)

If you are using PyCharm, follow these steps to enable Django framework support:

1. Open **Settings** (*File → Settings*).
2. Navigate to **Languages & Frameworks → Django**.
3. Check **Enable Django Support**.
4. Set the following paths:
   - **Django project root** → `J.U.R.A/`
   - **Settings** → `JuraDjangoProject.settings`
   - **Manage script** → `J.U.R.A/manage.py`
5. Click **Apply** → **OK**.

To run the Django server directly from PyCharm:

1. Go to **Run → Edit Configurations...**.
2. Click `+` → Select **Django Server**.
3. In **Host**, enter `127.0.0.1`, and in **Port**, enter `8000`.
4. In **Environment Variables**, add:
```DJANGO_SETTINGS_MODULE=JuraDjangoProject.settings.dev```
5. Click **Apply** → **OK**.

Now you can run the server directly from PyCharm.

### 10. Run the Development Server
```sh
  python manage.py runserver
```

Now, open `http://127.0.0.1:8000/` in your browser to access the application.

---

And here we go! 🧙✨ The magic is happening! 🪄🔮
