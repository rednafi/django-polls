<h1>Django Polls<img src='https://user-images.githubusercontent.com/30027932/149640721-177e46fc-f108-4cd7-a379-5446b414fd32.png' align='right' width='128' height='128'></h1>

<strong>>> <i>Django polls app for experimentation</i> <<</strong>

</div>

![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![github_actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

## What?

This is the canonical `polls` app from the Django [tutorial](https://docs.djangoproject.com/en/4.0/intro/).

## Why?

Experimenting with Django requires you to write a whole bunch of boilerplate code before you can get to the main point. So, I wanted to make it a reusable package. This is also helpful while communciating with people in blogs and tutorials on Django.

## Quickstart

### Use as a library

* Run `pip install django-polls-rednafi`.

* In your Django project's `settings.py` file, add `polls.apps.PollsConfig` to the `INSTALLED_APPS` section.

* Start using the components of the `polls` app. Inspect the [source](./django-polls) to see what models and views are included in the app. It's exactly the same as the polls [tutorial](https://docs.djangoproject.com/en/4.0/intro/).


### Use as an app

If you want the entire app and not only the reusable models and view, then:

* Clone this repo.

* Go to `django-polls`.

* Run `python manage.py makemigrations && python manage.py migrate`.

* Go to `http://localhost:8000/polls/` and start using the app.


<div align="center">
<i> ✨ 🍰 ✨ </i>
</div>
