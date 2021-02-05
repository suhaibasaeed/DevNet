# What OS/Kernel it will be running for base OS
FROM ubuntu:20.04
# Author info
LABEL maintainer="saeed.suhaib@googlemail.com"

# Update the container with latest repo. -y means say yes to prompts. Then install python 3 pip and dev environments
RUN apt-get update -y && apy-get install -y python3-pip python3-dev

# Run this raw command - Done as app runs on port 5000 so open this port in container
CMD ["ufw allow 5000"]
# Copy python requirements.txt file from local dir to app dir on the container
COPY ./requirements.txt /app/requirements.txt

# Change paths in the container and make the current working directory /app
WORKDIR /app

# Install the requirements from the requirements.txt file
RUN pip3 install -r requirements.txt

# Copy the actual python code to run from local dir to the app folder on the container
COPY ./my_api.py /app

# Specify what we program want to enter and execute
ENTRYPOINT ["python3"]
# File we're running
CMD ["my_api.py"]

