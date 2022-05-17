- Learn how to read error messages
- build the app from the ground up and follow the data.
- Install dependencies and create the virtual environment

```
pipenv install flask pymysql flask-bcrypt
```

- remember to activate the virtual environment

```
pipenv shell
```

- [ ] create [`server.py`](server.py)
- [ ] create the file structure in the `flask_app` directory:
  - [ ] config:
    - [ ] [`mysqlconnection.py`](flask_app/config/mysqlconnection.py)
  - [ ] controllers: 
    - [ ] [`users.py`](flask_app/controllers/users.py)
      - This should be pre populated with the login and registration functionality
    - [ ] [`models.py`](flask_app/controllers/users.py)
  - [ ] models:
    - [ ] [`user.py`](flask_app/models/user.py)
      - This should have all the class and static methods for login/registration and validations
    - [ ] [`model.py`](flask_app/models/model.py)
  - [ ] templates (aka views):
    - [ ] [`index.html`](flask_app/templates/index.html)
      - This should be the pre written login and registration page. This will most likely be the root route of the application.
    - [ ] [`models.html`](flask_app/templates/models.html)
  - [ ] [`__init__.py`](flask_app/__init__.py)