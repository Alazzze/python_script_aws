import boto3

#Connecting to Amazon S3
s3 = boto3.client('s3')

# Bucket name
bucket_name = 'sorokolat-test'

# Create new bucket
s3.create_bucket(Bucket=bucket_name)


file_path = '/home/stas/Stanislav_Sorokolat.txt'

# File name
s3_file_name = 'stanislav-sorokolat'

# Uploading
s3.upload_file(file_path, bucket_name, s3_file_name)

# Pulling a file from S3 and printing its contents
response = s3.get_object(Bucket=bucket_name, Key=s3_file_name)
file_content = response['Body'].read().decode('utf-8')
print("Вміст файлу:")
print(file_content)
