# Use a base Python image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev

# Install project dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port on which the Django application will run (replace with your Django app's port)
EXPOSE 3000

# Run the Django application
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "--workers", "4", "pytter_django.wsgi:application"]
