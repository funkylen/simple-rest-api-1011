# Simple API 

HTTP Style as REST API

branch `master` - filesystem
branch `db` - database (PostgreSQL)


## Requirements
* Python
* Poetry
* Make

## Install

```sh
make install
```

or

```sh
poetry install
```

## Start dev server

```sh
make dev
```

or

```sh
poetry run flask --app rest_api:app run
```