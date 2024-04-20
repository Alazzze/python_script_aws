import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

print("Creating EC2 instance...")

instance = ec2.create_instances(
    ImageId='ami-04e5276ebb8451442',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='alazze',
    SubnetId='subnet-0064cf9c34587432d'  
)

print("EC2 instance created.")

# Waiting for the instance to be ready
print("Waiting for instance to be running...")
instance[0].wait_until_running()
print("Instance is running.")

# information about the instance
print("Retrieving instance information...")
instance_info = ec2.Instance(instance[0].id)

# public IP address of the created instance
public_ip = instance_info.public_ip_address

# Display the address on the screen
print("Public IP address of the instance:", public_ip)
