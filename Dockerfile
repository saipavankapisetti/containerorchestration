# Use the official Python image as base
FROM python:3.9-slim

# Set environment variables for MySQL connection
ENV MYSQL_HOST=localhost \
    MYSQL_USER=default_user \
    MYSQL_PASSWORD=default_password \
    MYSQL_DB=default_db

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir Flask Flask-MySQLdb

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
