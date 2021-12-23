# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7.9 as integration

# The environment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# create a root directory for our project in the container
RUN mkdir /app

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# tell the port number the container should expose
EXPOSE 8000
