# tuiter-app

> The Tuitter App project is a Twitter simulation, using Vuetify (Material Component Framework for Vue.js 2) and the RESTful web service using Python and the Flask microframework.

## Build Setup

> These commands are to run on the windows 10 operating system.

``` bash
# create the virtual environment
$ python -m venv venv

# enable the virtual environment
$ venv\Scripts\activate

# disable the virtual environment
$ venv\Scripts\deactivate

# manually install the dependencies
$ venv\Scripts\pip3.exe install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy flask-migrate datetime flask-script

# installation of dependencies via requirements.tx
$ pip install -r requirements.txt

# initialize the database
$ venv\Scripts\python.exe app.py db init

# migrate the database
$ venv\Scripts\python.exe app.py db migrate

# update the database
$ venv\Scripts\python.exe app.py db upgrade

# run the local server
$ venv\Scripts\python.exe app.py runserver
```