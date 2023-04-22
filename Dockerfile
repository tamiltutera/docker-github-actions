# USE AN OFFICIAL PYTHON RUNTIME PARENT IMAGE
FROM python:3.9

# SETTING THE ENVIRONMENT VARIABLE
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# SETTING WORKING DIRECTORY

WORKDIR /code

COPY requirements.txt requirements.txt

# INSTALLING THE PYTHON PACKAGES
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /code

# RUN MIGRATIONS
RUN python manage.py makemigrations && python manage.py migrate

# EXPOSING THE PORT
EXPOSE 8001

CMD ["python","manage.py","runserver","0.0.0.0:8000"]

