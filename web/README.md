# TTC Subway Times UI
This part of the project is a UI where we a user can explore the database and determine how long it will take them.

## Setup
```bash
pyenv local 3.7.2
pip install poetry
hash -r
poetry install
```

Create a `.env` file with these contents for easy loading of the app.
```
FLASK_APP=ttc_subway_times_ui
FLASK_ENV=development
```

Run the app with `flask run`
