# User Authentication through Django Forms

In this project we will practice to use Django Forms for the common functionality of signing up and logging in users of an app, as well as using custom forms to gather other types of user input and do something with it.

* Set up a new Django project and a new Django App
* Register the relevant URLs etc.
* Using default Forms for User management, create a `/frontpage` with the possibility for new users to sign up and for existing users to log in to the app
* Add a `/profile` page that displays the authenticated user's name when they are signed in, and allows them to sign out again (remember to name the associated view `signout()` to avoid conflicts with Django built-in functions!)

# Challenges

- Extend the App with a custom Django Form that takes in an API key, to allow an API call to the [New York Times top stories API](https://developer.nytimes.com/top_stories_v2.json#/README)
- Extend the default User Model and the `UserCreation` form so that new users add their NYT API keys already when signing up
- Create a new Form that allows users to select from the different available `<sections>` of the NYT top-stories API to display the different results
- Display and filter the results in your `/profile` site to show the title, abstract, and a clickable URL of the related NYT story


# Resources

* [Forms API Django docs](https://docs.djangoproject.com/en/2.1/ref/forms/api/)
* [MDN Docs on Forms](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)
* [Project code on GitHub](https://github.com/martin-martin/django-simple-auth)
* [Extending the Django User Model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone)
* [NYT top stories API docs](https://developer.nytimes.com/top_stories_v2.json#/README)
