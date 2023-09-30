# Use a base Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your Python script into the container
COPY frontend.py /app/
COPY backend.py /app/

# Install any necessary dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Specify the command to run your Python script
CMD ["python", "frontend.py"]