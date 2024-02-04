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
