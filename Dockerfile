# Use a base image with Python
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the Python files and HTML templates into the container
COPY app.py templates/ /app/

# Install Flask and other dependencies
RUN pip install --no-cache-dir flask

# Expose the port
EXPOSE 5000

# Set the command to run the Flask app
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]

#Entrypoint
#ENTRYPOINT FLASK_APP=/app/app.py flask run --host=0.0.0.0
