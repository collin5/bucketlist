[![Codacy Badge](https://api.codacy.com/project/badge/Grade/82041bac74e24b0ab47413b22e1b8ec0)](https://www.codacy.com/app/abtcolns/bucketlist?utm_source=github.com&utm_medium=referral&utm_content=collin5/bucketflow&utm_campaign=badger)
[![Build Status](https://travis-ci.org/collin5/bucketlist.svg?branch=master)](https://travis-ci.org/collin5/bucketlist)
[![Coverage Status](https://coveralls.io/repos/github/collin5/bucketlist/badge.svg?branch=master)](https://coveralls.io/github/collin5/bucketlist?branch=master)

### Bucketflow
To keep track of your Todos before you ... !

## Requiremnts
```
$ pip install -r requirements.txt
```

## API Functionality Scope
Documentation https://bucketflow.herokuapp.com/apidocs/

|Method | Endpoint | Usage |
| ---- | ---- | --------------- |
|POST| `/auth/register/` | Registering user. |
|POST| `/auth/login/` | User login, get login token.|
|POST| `/bucketlists/` | Creates a new bucketlist. |
|POST| `/bucketlists/<int:id>/items/` | Adds new item to bucketlist with id `id`. |
|GET| `/bucketlists/` | Gets users bucketlists. |
|GET| `/bucketlists/?offset=` | Gets bucketlists with offset. |
|GET| `/bucketlists?limit=` | Gets bucketlists with limit.|
|GET| `/bucketlists?q=` | Search bucketlists with keword.
|PUT| `/bucketlists/<int:id>` | Updates bucketlist of given `id`. |
|DELETE|`/bucketlists/<int:id>` | Deletes bucketlist of `id`. |


## Installation and Setup.
```
$ sudo chmod +x manage.py
$ ./manage.py db init
$ ./manage.py db migrate
$ ./manage.py db upgrade
$ gunicorn manage:app
```


## Usage
View API doc at https://bucketflow.herokuapp.com/apidocs/

## Testing
In the project directory

```
$ nosetests --with-coverage
```


