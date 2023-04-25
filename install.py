import docker
import os
import argparse

# # Set up Docker client
# client = docker.from_env()

# # Define image name and tag
# image_name = 'quay.io/tamiltutera/django_mysql_app'
# image_tag = 'latest'

# # Pull image
# client.images.pull(image_name, tag=image_tag)

# # Set up environment variables from .env file
# env_vars = {}
# with open('.env', 'r') as f:
#     for line in f:
#         key, value = line.strip().split('=')
#         env_vars[key] = value
# # Define port to expose
# port_bindings = {8000: 8001}

# # Run container with environment variables
# container = client.containers.run(
#     image_name + ':' + image_tag,
#     name='djang_web_app',
#     environment=env_vars,
#     ports=port_bindings,
#     detach=True
# )

# # Print container ID
# print('Container ID:', container.id)

# Set up Docker client
client = docker.from_env()

# Define image names and tags
# image_tags = {
#     'pure_db': 'quay.io/tamiltutera/django_mysql:latest',
#     'pure_web_app': 'quay.io/tamiltutera/django_web_app:latest'
# }

# Define command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('images', nargs='+', help='list of image names to pull and run')
args = parser.parse_args()

# Define port bindings
port_bindings = {
    'django_mysql': {3306: 3306},
    'django_web_app': {8000:8005}  # no ports to bind for this image
}

for image_name in args.images:
    image_tag = f'quay.io/tamiltutera/{image_name}:latest'
    client.images.pull(image_tag)


# Set up environment variables from .env file
env_vars = {}
with open('.env', 'r') as f:
    for line in f:
        key, value = line.strip().split('=')
        env_vars[key] = value

# Run containers with environment variables
containers = {}
for image_name in args.images:
    
    if image_name in port_bindings:
    
        container = client.containers.run(
            image_tag,
            environment=env_vars,
            name=image_name,
            ports=port_bindings[image_name],
            detach=True
        )
    else:
        
        container = client.containers.run(
            image_tag,
            name=image_name,
            environment=env_vars,
            detach=True
        )
    containers[image_name] = container
    containers[image_name] = container

# Print container IDs
for image_name, container in containers.items():
    print(f'{image_name} container ID:', container.id)