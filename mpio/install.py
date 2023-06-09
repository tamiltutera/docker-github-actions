import docker
import os
import argparse

# Set up Docker client
client = docker.from_env()


login_result = client.login(
    registry='quay.io',
    username='tamiltutera',
    password='6VrKr9pSkrzKypnUepGjYbCmbMupMwsXqnp/ONYaz8dcRyatsPcnntTDXemPO4mg'
)

# Check if login was successful
if 'Status' in login_result and login_result['Status'] == 'Login Succeeded':
    print('Quay.io login successful')
    if client.ping():
        print('Docker daemon is responsive')
    else:
        print('Docker daemon is not responsive')
else:
    print('Quay.io login failed')

# Define command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('images', nargs='+', help='list of image names to pull and run')
args = parser.parse_args()

# Define port bindings
port_bindings = {
    'django_mysql': {3306: 3306},
    'django_web_app': {8000:8005}  # no ports to bind for this image
}

# Pull images
# for image_name, image_tag in image_tags.items():
    
#     client.images.pull(image_tag)
# Pull images
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
        print("ENV not set")
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