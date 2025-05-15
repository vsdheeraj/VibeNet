
```markdown
# VibeNet - A Simple Social Network

![VibeNet Logo](static/simplesocial/images/logo.png) 

VibeNet is a simple social network built with Django that allows users to create posts, join groups, and interact with other users.

## Features

- User authentication (Sign up, Login, Logout)
- Create and manage posts
- Join and leave groups
- View posts by specific users
- Responsive design with Bootstrap 5

## Technologies Used

- Python 3.x
- Django 4.1
- Bootstrap 5
- Misaka (for markdown support)
- SQLite (development database)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/vibenet.git
cd vibenet
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

```
simplesocial/
├── accounts/          # User authentication app
├── groups/            # Groups functionality
├── posts/             # Posts functionality
├── templates/         # Base templates
├── static/            # Static files (CSS, JS, images)
├── simplesocial/      # Project settings and configurations
└── manage.py          # Django management script
```

## Configuration

The main configuration file is located at `simplesocial/settings.py`. Key settings include:

- `DEBUG = True` (set to False in production)
- Database configuration (SQLite by default)
- Static files settings
- Login/Logout redirect URLs

## Usage

After starting the development server, access the application at:

- Homepage: http://localhost:8000/
- Admin panel: http://localhost:8000/admin/ (if superuser created)
- Sign up: http://localhost:8000/accounts/signup/
- Login: http://localhost:8000/accounts/login/


## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

