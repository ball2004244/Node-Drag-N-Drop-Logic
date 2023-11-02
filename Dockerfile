
# Use the official Python image as the base image
FROM python:3.10.13-alpine

# Set the working directory to /app
WORKDIR /application

# Copy the current directory contents into the container at /app
COPY . /application

# Install the required packages
RUN pip install -r requirements.txt

# Expose port 8080 for the application
EXPOSE 8080

# Start the application using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
