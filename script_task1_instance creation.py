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

# Очікування, поки інстанс буде готовий
print("Waiting for instance to be running...")
instance[0].wait_until_running()
print("Instance is running.")

# Отримання інформації про інстанс
print("Retrieving instance information...")
instance_info = ec2.Instance(instance[0].id)

# Отримання публічної IP-адреси створеного інстансу
public_ip = instance_info.public_ip_address

# Виведення адреси на екран
print("Public IP address of the instance:", public_ip)
