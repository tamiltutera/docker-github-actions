# import docker
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

import docker
import os

# Set up Docker client
client = docker.from_env()

# Define image names and tags
image_tags = {
    'image1': 'quay.io/tamiltutera/image1:latest',
    'image2': 'quay.io/tamiltutera/image2:latest',
    'image3': 'quay.io/tamiltutera/image3:latest',
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
    container = client.containers.run(
        image_tag,
        environment=env_vars,
        detach=True
    )
    containers[image_name] = container

# Print container IDs
for image_name, container in containers.items():
    print(f'{image_name} container ID:', container.id)