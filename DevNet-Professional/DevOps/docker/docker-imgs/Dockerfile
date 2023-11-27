FROM python:latest

# metadata
LABEL description="Net inventory flask app"
LABEL maintainer="Cisco <noreply@cisco.com>"
LABEL version="0.1"

# copy files over to container
COPY ./ /net_inventory

# sets the working directory
WORKDIR /net_inventory/

# install python packages
RUN pip install -r ./requirements.txt

# set environment to development by default
ENV ENV=DEVELOPMENT

# doesn't actually do anything, just documentation purposes.
EXPOSE 5000/tcp

# start the application
ENTRYPOINT python run.py