# random-workout
Generate a variable length workout based on moves from a local JSON database.

To run at commandline:

`pipenv run python main.py`

To start web app locally:

`pipenv run python serve.py`

Then go to localhost:5000/workout (or whatever)


## TODO:
- Serve via HTTPS - https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https
- Serve via waitress
- Figure out some easier way to deploy and run on EC2 other than git clone
- Componentize to facilitate testing
- Create a new shortlink
- Instead of pulling moves from move_list.py, pull from a Google Sheet (or something)
  - Some sort of "fall back to using local move_list.py"
