# Python Persistent Queue

## Introduction
This project is a template for achieving persistent queuing mechanism in python using `celery`, `redis` and `mysql`.

## Installation

### Docker
You can simply run the whole stack in docker using `docker-compose`,
```shell
docker-compose up -d
```

### Manual Installation
For manual installation, you must have `python3` installed, then follow these steps:
###### Create a virtual environment and activate the environment:
```shell
python3 -m virtualenv venv
source bin/venv/activate
```
###### Install the required dependencies:
```shell
python -m pip install -r requirements.txt
```

###### Run api in a terminal tab:
```shell
uvicorn main:app --host 0.0.0.0 --port 8000
```

###### Run celery worker in another terminal tab:
```shell
celery -A main.celery worker --loglevel=info
```

###### If you need to monitor tasks, run flower:
```shell
celery -A main.celery flower --port=5555
```
