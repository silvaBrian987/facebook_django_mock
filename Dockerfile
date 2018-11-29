# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Installing nginx
RUN apt-get update && apt-get install -y nginx

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the nginx config
#RUN ls
COPY ./nginx-config/app /etc/nginx/sites-available/app
RUN ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app
#RUN systemctl restart nginx

RUN nginx -T > nginx-config.log

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80
#EXPOSE 8000

# Define environment variable
#ENV NAME World

# Django collect statics
RUN python manage.py collectstatic

# Run app.py when the container launches
#CMD ["gunicorn", "-c gunicorn-config.py", "facebook_django_mock.wsgi"]
ENTRYPOINT ["/bin/bash", "start.sh"]
