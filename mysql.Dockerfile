FROM mysql:8.0

# Set the root password
ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD

# Create a new database
ENV MYSQL_DATABASE=$MYSQL_DATABASE

# Create a new user
ENV MYSQL_USER=$MYSQL_USER
ENV MYSQL_PASSWORD=$MYSQL_PASSWORD

# Copy the custom configuration file
COPY my_sql.cnf /etc/mysql/conf.d/

# Expose the default MySQL port
EXPOSE 3306