# Django - My site (Polling website)

A polling website, powered by Django (v4.2.9), which is featured on its [official documentation](https://docs.djangoproject.com/en/4.2/intro/tutorial01/).

<br>

## Preview

These pages are featured in this website:

### Polls page

<img src="demo/polls-s.png" alt="polls page" />

<hr>

### Sample Question 1

<img src="demo/q1-s.png" alt="sample question 1" />

After voting, you would see the result:

<img src="demo/q1-result-s.png" alt="sample question 1 - result" />

<hr>

### Sample Question 2

<img src="demo/q2-s.png" alt="sample question 2" />

After voting, you would see the result:

<img src="demo/q2-result-s.png" alt="sample question 2 - result" />

<hr>

### Sample Question 3

<img src="demo/q3-s.png" alt="sample question 3" />

After voting, you would see the result:

<img src="demo/q3-result-s.png" alt="sample question 3 - result" />

<br>

## Prerequisites

Before running the app, please make sure you have following software installed in your machine:
- [Python 3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [MySQL](https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/)
- [Git](https://github.com/git-guides/install-git)

<br>

## How to Run

1. Create a virtual environment

```
python3 -m venv .venv
```

2. Navigate to this directory, then activate the virtual environment

```
source .venv/bin/activate
```

3. Install required packages

```python
pip3 install -r requirements.txt
```

4. Make a new file named `.env`, then copy `.env.example` and paste the content into it

```
cp .env.example .env
```

After that, fill `.env` with appropriate values

5. Create a database (Make sure you have MySQL installed in your machine beforehand)

```python
python3 mydb.py
```

6. Apply database migration

```python
python3 manage.py migrate
```

7. Create a superuser of Django admin panel

```python
python3 manage.py createsuperuser
```

You will then by asked several questions, such as `username`, `email`, and `password` of the superuser.

8. Finally, run the server!

```python
python3 manage.py runserver
```

9. Voila! Visit http://localhost:8000/polls on your browser

<br>

## To-do list

- Put available routes in the docs
- Make a Dockerfile
- Improve site title in base_site.html
- Utilize `python-dotenv` package to store environment variables ✅
- Generate `requirements.txt` ✅

<br>

## References

- [Writing your first Django app](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
- [Advanced tutorial: How to write reusable apps](https://docs.djangoproject.com/en/4.2/intro/reusable-apps/)

<br>

![Hello !](https://api.visitorbadge.io/api/VisitorHit?user=kevinadhiguna&repo=django-mysite&label=thanks%20for%20dropping%20in%20!&labelColor=%23000000&countColor=%23FFFFFF)
