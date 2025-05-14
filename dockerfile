FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /myapp

# Install Flask
RUN pip install flask

# Copy the application file into the container
COPY app.py app.py

# Run the application
CMD ["python", "app.py"]
