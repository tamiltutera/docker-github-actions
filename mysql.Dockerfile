FROM mysql:8.0

# Set the root password
ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD

# Create a new database
ENV MYSQL_DATABASE=$MYSQL_DATABASE

# Create a new user
ENV MYSQL_USER=$MYSQL_USER
ENV MYSQL_PASSWORD=$MYSQL_PASSWORD
ENV MYSQL_ALLOW_EMPTY_PASSOWRD=$MYSQL_ALLOW_EMPTY_PASSWORD

RUN sudo apt-get -y update && \
    sudo apt-get -y upgrade && 
# Copy the custom configuration file
COPY my_sql.cnf /etc/mysql/conf.d/

# Expose the default MySQL port
EXPOSE 3306
