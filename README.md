# random-workout
Generate a variable length workout based on moves from a local or Dropboxed JSON database.

To run at commandline:

`pipenv run python src/main.py`

To start web app locally:

`pipenv run bash start_app.sh`

Then go to localhost:5000/workout (or whatever endpoint)

## Testing
`pytest`
`flake8`


## TODO
- Serve via waitress: https://flask.palletsprojects.com/en/2.3.x/deploying/waitress/
- Add move functional tests
- Add unit tests for serve methods