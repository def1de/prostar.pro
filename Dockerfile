# Use the official Python image from the Docker Hub
FROM python:3.13.3-bookworm

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Initialize the database before starting the application
RUN flask init-db

# Specify the command to run on container start
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
