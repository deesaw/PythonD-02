"""
Installing boto3
"""
##pip install boto3

"""
Configuring aws credentials

you can create the credential file yourself. By default, its location is at
~/.aws/credentials:

[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY

You may also want to set a default region.
This can be done in the configuration file. By default, its location is at
~/.aws/config:

[default]
region=us-east-1
"""

import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
data = open('test.jpg', 'rb')
s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data) ## Assuming that bucket
                                                             ## 'my-bucket' already exists.
