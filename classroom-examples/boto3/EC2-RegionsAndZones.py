## Describe Amazon EC2 Regions and Availability Zones
"""
--------------------------------------------------------------------------------
Amazon EC2 is hosted in multiple locations worldwide.
These locations are composed of regions and Availability Zones.
Each region is a separate geographic area. Each region has multiple,
isolated locations known as Availability Zones.
Amazon EC2 provides the ability to place instances and data in multiple locations.

In this example, Python code is used to get details about regions and Availability Zones. The code uses the AWS SDK for Python to get the data by using these methods of the EC2 client class:

- describe_regions.
- describe_availability_zones.
--------------------------------------------------------------------------------
"""
## Describe Regions and Availability Zones
"""
********************************************************************************
Describe one or more regions that are currently available to you.
Describe one or more of the Availability Zones that are available to you.
The results include zones only for the region you're currently using.
If there is an event impacting an Availability Zone, you can use this
request to view the state and any provided message for that Availability Zone.

The example below shows how to:

- Describe regions using describe_regions.
- Describe AvailabilityZones using describe_availability_zones.
********************************************************************************
"""
import boto3

ec2 = boto3.client('ec2')

# Retrieves all regions/endpoints that work with EC2
response = ec2.describe_regions()
print('Regions:', response['Regions'])

# Retrieves availability zones only for region of the ec2 object
response = ec2.describe_availability_zones()
print('Availability Zones:', response['AvailabilityZones'])
