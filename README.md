# Insta-Clone
A Django website clone of [Instagram] app

## Getting Started

To get a copy of the project up and running on your local machine for development and testing purposes, 
1. **Clone** this repository to your machine

2. Create a **virtual environment** 
   ```
   python3 -m venv virtual

   source virtual/bin/activate
   ```
   or 
   ```
   pipenv shell
   ```
3. Install project **dependencies**
   ```sh
    (virtual) $ pip install -r requirements.txt
    ```
    Using pipenv will automatically install the dependecies from either requirements.txt or pipfile upon creating the environment.
* See deployment for notes on how to deploy the project on a live system.

### Prerequisites

//


### Installing

1.  To get a development env running, use the **.env.sample** file to create your own **.env** file.
2.  Create a **postgres** db and add the credentials to .env file
3.  Apply all migrations
```sh 
(virtual) $ python manage.py migrate 
```
4. Create admin account
```
(virtual) $ python manage.py createsuperuser
```
5. Make migrations to your database
```sh
(virtual) $ python manage.py makemigrations app_insta
(virtual) $ python manage.py migrate
```
6.  Start development server
```
 (virtual) $ python3 manage.py runserver
 ```

## Running the tests

Run automated tests for this system

```sh
(virtual) $ python3 manage.py test app_insta
```

## Deployment

With all environment variables changed to suit your local copy of this repository, deploy the application to [Heroku](https://medium.com/@hdsingh13/deploying-django-app-on-heroku-with-postgres-as-backend-b2f3194e8a43) to see it live

## Built With

* [Django]
* [Heroku]
* [Python3]
* [Postresql]


## Authors

* [Josephat Ngugi)


## License

This project is licensed under the MIT License - see the [LICENSE.md]for more details.
