## Working with Amazon EC2 Key Pairs
"""
-------------------------------------------------------------------------------
This Python example shows you how to:

- Get information about your key pairs
- Create a key pair to access an Amazon EC2 instance
- Delete an existing key pair

Amazon EC2 uses public–key cryptography to encrypt and decrypt login information
Public–key cryptography uses a public key to encrypt data, then the recipient
uses the private key to decrypt the data.
The public and private keys are known as a key pair.

In this example, Python code is used to perform several
Amazon EC2 key pair management operations.
The code uses the AWS SDK for Python to manage IAM access keys using
these methods of the EC2 client class:

. describe_key_pairs.
. create_key_pair.
. delete_key_pair.
-------------------------------------------------------------------------------
"""
## Describe Key Pairs
"""
*******************************************************************************
Describe one or more of your key pairs.

The example below shows how to:

- Describe keypairs using describe_key_pairs.
*******************************************************************************
"""
import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_key_pairs()
print(response)

## Create a Key Pair
"""
*******************************************************************************
Create a 2048-bit RSA key pair with the specified name.
Amazon EC2 stores the public key and displays the private key for you to
save to a file. The private key is returned as an unencrypted PEM
encoded PKCS#8 private key. If a key with the specified name already exists,
Amazon EC2 returns an error.

The example below shows how to:

- Create a 2048-bit RSA key pair with a specified name using create_key_pair.
*******************************************************************************
"""
import boto3

ec2 = boto3.client('ec2')
response = ec2.create_key_pair(KeyName='KEY_PAIR_NAME')
print(response)

## Delete a Key Pair
"""
*******************************************************************************
Delete the specified key pair, by removing the public key from Amazon EC2.

The example below shows how to:

- Delete a key pair by removing the public key from Amazon EC2
  using delete_key_pair.
*******************************************************************************
"""
import boto3

ec2 = boto3.client('ec2')
response = ec2.delete_key_pair(KeyName='KEY_PAIR_NAME')
print(response)
