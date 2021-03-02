## Managing Identity Access Management (IAM) Users
"""
--------------------------------------------------------------------------------
In this example Python code is used to create and manage users in IAM.
The code uses the Amazon Web Services (AWS) SDK for Python to
manage users using these methods of the IAM client class:

- create_user
- get_paginator('list_users').
- update_user.
- delete_user.
--------------------------------------------------------------------------------
"""
## Create a User
"""
********************************************************************************
Create a new IAM user for your AWS account.
The example below shows how to:

- Create a new IAM user using create_user.
********************************************************************************
"""
import boto3

# Create IAM client
iam = boto3.client('iam')

# Create user
response = iam.create_user(
    UserName='IAM_USER_NAME'
)

print(response)

## List Users in Your Account
"""
********************************************************************************
List the IAM users.

The example below shows how to:

- List the IAM users using get_paginator('list_users').
********************************************************************************
"""
import boto3

# Create IAM client
iam = boto3.client('iam')

# List users with the pagination interface
paginator = iam.get_paginator('list_users')
for response in paginator.paginate():
    print(response)

## Update a User's Name
"""
********************************************************************************
Update the name and/or the path of the specified IAM user.

To change a user's name or path, you must use the AWS CLI, Tools for
Windows PowerShell, or AWS API.
***There is no option in the console to rename a user.***

The example below shows how to:

- Update an IAM user name using update_user.
********************************************************************************
"""
import boto3

# Create IAM client
iam = boto3.client('iam')

# Update a user name
iam.update_user(
    UserName='IAM_USER_NAME',
    NewUserName='NEW_IAM_USER_NAME'
)

## Delete a User
"""
********************************************************************************
Delete the specified IAM user. The user must not belong to any groups or
have any access keys, signing certificates, or attached policies.

The example below shows how to:

- Delete an IAM user name using delete_user.
********************************************************************************
"""
import boto3

# Create IAM client
iam = boto3.client('iam')

# Delete a user
iam.delete_user(
    UserName='IAM_USER_NAME'
)
