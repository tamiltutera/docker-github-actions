# Use the latest version of the official Python image as the base image
FROM python:latest

# Install Ansible and other required packages
RUN apt-get update && apt-get install -y \
    ansible \
    ssh

# Copy your Ansible playbook and inventory file into the container
COPY . .

# Set the working directory to the root directory of your playbook
WORKDIR /

# Define the entrypoint to run the playbook
CMD ["ansible-playbook", "-i", "/product_src/hosts", "/product_src/main.yml"]