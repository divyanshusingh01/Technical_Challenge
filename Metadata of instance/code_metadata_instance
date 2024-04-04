import boto3
import json

def get_instance_metadata():
    # Initialize the EC2 client
    ec2_client = boto3.client('ec2')
    
    # Get instance metadata
    response = ec2_client.describe_instances()
    
    # Extract relevant metadata
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_data = {
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'PrivateIpAddress': instance['PrivateIpAddress'],
                # Add more metadata fields as needed
            }
            instances.append(instance_data)
    
    return instances

if __name__ == "__main__":
    instance_metadata = get_instance_metadata()
    print(json.dumps(instance_metadata, indent=4))
