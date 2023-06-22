# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the Cloud Run logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
WORKDIR /app
COPY . .

# Install production dependencies.
RUN pip install -r requirements.txt
RUN pip install flask google-api-python-client google-auth-httplib2 google-auth-oauthlib


# Run the web service on container startup.
CMD ["python", "main.py"]

