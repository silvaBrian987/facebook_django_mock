# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

# Django migrate
RUN python manage.py makemigrations -v 3 | python manage.py migrate -v 3

# Django collect statics
#RUN yes | python manage.py collectstatic -c
RUN python manage.py collectstatic -c --noinput

#RUN ls -l -R /app/

# Run app.py when the container launches
CMD ["gunicorn", "-c", "gunicorn-config.py", "facebook_django_mock.wsgi"]

#RUN groupadd -g 999 appuser && useradd -r -u 999 -g appuser appuser
#USER appuser
