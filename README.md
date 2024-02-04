<h1>Social Project</h1>

The Django project integrates with Facebook and Twitter APIs to enable actions such as posting comments, liking posts, tweeting etc.

<h2>Authentication</h2>

The authentication related functionality is implemented in customprofile app.

The following API keys need to be configured:

    Facebook API Key and Secret: Set FACEBOOK_KEY and FACEBOOK_SECRET environment variables
    Twitter API Key and Secret: Set TWITTER_KEY and TWITTER_SECRET environment variables

These keys enable the application to authenticate and perform actions on behalf of logged in users.

<h2>Dependencies</h2>

Dependencies of this project are managed using pip and requirements.txt file. To install run:

    pip install -r requirements.txt

This will install packages like Django, Facebook SDK, Python Twitter Tools etc.

<h2>Local Setup</h2>

To set up the project locally for development/testing:

Clone the repository

    https://github.com/dhimanhere/Socialproject.git

Create and activate virtual environment


    python -m venv env 
    source env/bin/activate

This keeps project dependencies isolated from system Python installation

Install dependencies


    pip install -r requirements.txt

Installs packages like Django, PIL, psycopg2 etc. required for project.

Run database migrations


    python manage.py makemigrations
    python manage.py migrate

Sets up database by applying migrations

Start development server


    python manage.py runserver

Starts Django development server at http://127.0.0.1:8000

Create superuser (optional)

    python manage.py createsuperuser

To access Django admin site

Now the project should be accessible at http://localhost:8000. As you make code changes, just restart the development server.
