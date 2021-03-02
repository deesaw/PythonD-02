## Managing Amazon EC2 Instances
"""
------------------------------------------------------------------------------
This Python example shows you how to:

- Get basic information about your Amazon EC2 instances
- Start and stop detailed monitoring of an Amazon EC2 instance
- Start and stop an Amazon EC2 instance
- Reboot an Amazon EC2 instance

In this example, Python code is used perform several basic instance management
operations. The code uses the AWS SDK for Python to manage the instances
by using these methods of the EC2 client class:

.describe_instances.
.monitor_instances.
.unmonitor_instances.
.start_instances.
.stop_instances.
.reboot_instances.
------------------------------------------------------------------------------
"""
## Descrice Instances
"""
******************************************************************************
An EC2 instance is a virtual server in Amazon's Elastic Compute Cloud (EC2)
for running applications on the Amazon Web Services (AWS) infrastructure.

The example below shows how to:

- Describe one or more EC2 instances using describe_instances.
******************************************************************************
"""
import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)

## Monitor or Un-monitor Instances
"""
******************************************************************************
Enable or disable detailed monitoring for a running instance.
If detailed monitoring is not enabled, basic monitoring is enabled.

The example below shows how to:

- Enable detailed monitoring for a running instance using monitor_instances.
- Disable detailed monitoring for a running instance using unmonitor_instances.
******************************************************************************
"""
import sys
import boto3


ec2 = boto3.client('ec2')
if sys.argv[1] == 'ON':
    response = ec2.monitor_instances(InstanceIds=['INSTANCE_ID'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['INSTANCE_ID'])
print(response)

##Start and Stop Instances
"""
******************************************************************************
Instances that use Amazon EBS volumes as their root devices can be quickly
stopped and started. When an instance is stopped, the compute resources are
released and you are not billed for hourly instance usage.
However, your root partition Amazon EBS volume remains, continues to
persist your data, and you are charged for Amazon EBS volume usage.
You can restart your instance at any time. ***Each time you transition an
instance from stopped to started, Amazon EC2 charges a full instance hour,
even if transitions happen multiple times within a single hour.***

The example below shows how to:

- Start an Amazon EBS-backed AMI that you've previously stopped using
  start_instances.
- Stop an Amazon EBS-backed instance using stop_instances.
******************************************************************************
"""
import boto3
from botocore.exceptions import ClientError

instance_id = sys.argv[2]
action = sys.argv[1].upper()

ec2 = boto3.client('ec2')


if action == 'ON':
    # Do a dryrun first to verify permissions
    try:
        ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, run start_instances without dryrun
    try:
        response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
else:
    # Do a dryrun first to verify permissions
    try:
        ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, call stop_instances without dryrun
    try:
        response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)

## Reboot Instances
"""
******************************************************************************
Request a reboot of one or more instances. This operation is asynchronous;
it only queues a request to reboot the specified instances.
The operation succeeds if the instances are valid and belong to you.
Requests to reboot terminated instances are ignored.

The example below shows how to:

- Request a reboot of one or more instances using reboot_instances.
******************************************************************************
"""
import boto3
from botocore.exceptions import ClientError


ec2 = boto3.client('ec2')

try:
    ec2.reboot_instances(InstanceIds=['INSTANCE_ID'], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print("You don't have permission to reboot instances.")
        raise

try:
    response = ec2.reboot_instances(InstanceIds=['INSTANCE_ID'], DryRun=False)
    print('Success', response)
except ClientError as e:
    print('Error', e)
