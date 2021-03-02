## Creating Alarms in Amazon CloudWatch
"""
**********************************************************************
This Python example shows you how to:

- Get basic information about your CloudWatch alarms
- Create and delete a CloudWatch alarm

In this example, Python code is used to create alarms in CloudWatch.
The code uses the uses AWS SDK for Python to create alarms using
these methods of the AWS.CloudWatch client class:

.paginate(StateValue='INSUFFICIENT_DATA').
.put_metric_alarm.
.delete_alarms.

**********************************************************************
"""
"""
----------------------------------------------------------------------
The example below shows how to:

List metric alarms for insufficient data using
paginate(StateValue='INSUFFICIENT_DATA').
----------------------------------------------------------------------
"""
import boto3

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# List alarms of insufficient data through the pagination interface
paginator = cloudwatch.get_paginator('describe_alarms')
for response in paginator.paginate(StateValue='INSUFFICIENT_DATA'):
    print(response['MetricAlarms'])

"""
-----------------------------------------------------------------------
The example below shows how to:

Create or update a metric alarm using put_metric_alarm.
-----------------------------------------------------------------------
"""
import boto3

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Create alarm
cloudwatch.put_metric_alarm(
    AlarmName='Web_Server_CPU_Utilization',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=60,
    Statistic='Average',
    Threshold=70.0,
    ActionsEnabled=False,
    AlarmDescription='Alarm when server CPU exceeds 70%',
    Dimensions=[
        {
          'Name': 'InstanceId',
          'Value': 'INSTANCE_ID'
        },
    ],
    Unit='Seconds'
)

"""
------------------------------------------------------------------------
Deleting an Alarm:
Delete the specified alarms. In the event of an error, no alarms are deleted.

The example below shows how to:

Delete a metric alarm using delete_alarms.
------------------------------------------------------------------------
"""

import boto3

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Delete alarm
cloudwatch.delete_alarms(
  AlarmNames=['Web_Server_CPU_Utilization'],
)
