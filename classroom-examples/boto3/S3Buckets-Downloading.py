## Downloading a File from an S3 Bucket
"""
--------------------------------------------------------------------------------
This example shows how to download a file from an S3 bucket,
using S3.Bucket.download_file().

To set up and run this example, you must first:

. Configure your AWS credentials, as described in Quickstart.
. Create an S3 bucket and upload a file to the bucket.
. Replace the BUCKET_NAME and KEY values in the code snippet with the name
  of your bucket and the key for the uploaded file.

--------------------------------------------------------------------------------
"""


## Downloading a File
""""
********************************************************************************
The example below tries to download an S3 object to a file.
If the service returns a 404 error, it prints an error message indicating
that the object doesn't exist.
********************************************************************************
"""
import boto3
import botocore

BUCKET_NAME = 'my-bucket' # replace with your bucket name
KEY = 'my_image_in_s3.jpg' # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'my_local_image.jpg')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
