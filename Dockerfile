# python image used
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install dependecies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# copy project to the container
COPY . /app/

# Set env variable
ENV PYTHONUNBUFFERED 1

# Set the 8000 port for Django app
EXPOSE 8000

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Install dependencies
RUN apt-get update && apt-get install -y wget





