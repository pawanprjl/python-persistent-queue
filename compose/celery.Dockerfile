# pull official base image
FROM python:3.9-slim

# set working directory
WORKDIR /code

# copy and install requirements
COPY /requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

# copy app in code folder
COPY /app /code/app
COPY /main.py /code/

# run python api
CMD ["celery", "-A", "main.celery", "worker", "--loglevel=info", "--concurrency=2"]