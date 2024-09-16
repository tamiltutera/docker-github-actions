# USE AN OFFICIAL PYTHON RUNTIME PARENT IMAGE
FROM python:3.9

# SETTING THE ENVIRONMENT VARIABLE
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# SETTING WORKING DIRECTORY

WORKDIR /code

COPY requirements.txt requirements.txt

RUN apt-get -y update && \
    apt-get -y upgrade 

# INSTALLING THE PYTHON PACKAGES
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /code

# RUN MIGRATIONS
RUN python manage.py makemigrations && python manage.py migrate

# EXPOSING THE PORT
EXPOSE 8001

CMD ["python","manage.py","runserver","0.0.0.0:8000"]

# FROM mysql:latest

# ENV DB_HOST=$DB_HOST \
#       MYSQL_DATABASE=$MYSQL_DATABASE \
#       MYSQL_USER=$MYSQL_USER \
#       MYSQL_PASSWORD=$MYSQL_PASSWORD \
#       MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD
#  COPY my_sql.cnf /etc/mysql/conf.d/my_sql.cnf
 
