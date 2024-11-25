# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python", "main.py"]
