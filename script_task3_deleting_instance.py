import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

try:
    # Saving the list of existing instances
    response = ec2.describe_instances()

    # Output of information about instances
    print("Existing instances:")
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] != 'terminated':  # condition to check the status
                print("ID: {}, Type: {}, AZ: {}, State: {}".format(
                    instance['InstanceId'],
                    instance['InstanceType'],
                    instance['Placement']['AvailabilityZone'],
                    instance['State']['Name']
                ))

    # Which instance(s) to delete
    instance_ids_to_delete = input("Enter the instance ID(s) to delete, Press Enter to exit): ")

    # Exit without deleting
    if instance_ids_to_delete.strip() == "":
        print("Exit")
        exit()

    # Splitting input into individual instance IDs
    instance_ids_to_delete = instance_ids_to_delete.split()

    # Delete instances
    response = ec2.terminate_instances(InstanceIds=instance_ids_to_delete)

    # Outputting
    for instance in response['TerminatingInstances']:
        print("Instance {} removed successfully".format(instance['InstanceId']))

except Exception as e:
    print("Error: ", e)
