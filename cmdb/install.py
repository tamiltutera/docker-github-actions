import docker
# import os

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

# import docker
import os

# Set up Docker client
client = docker.from_env()

# Define image names and tags
image_tags = {
    'pure_db': 'quay.io/tamiltutera/django_mysql:latest',
    'pure_web_app': 'quay.io/tamiltutera/django_web_app:latest'
}

# Define port bindings
port_bindings = {
    'pure_db': {3306: 3306},
    'pure_web_app': {8000:8001}  # no ports to bind for this image
}

# Pull images
for image_name, image_tag in image_tags.items():
    
    client.images.pull(image_tag)

# Set up environment variables from .env file
env_vars = {}
with open('.env', 'r') as f:
    for line in f:
        key, value = line.strip().split('=')
        env_vars[key] = value

# Run containers with environment variables
containers = {}
for image_name, image_tag in image_tags.items():
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