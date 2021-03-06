## Using Alarm Actions in Amazon CloudWatch
"""
This Python example shows you how to:

- Create a CloudWatch alarm and enable actions
- Disable a CloudWatch alarm action
The code uses the uses AWS SDK for Python to manage Amazon EC2 instances
using these methods of the CloudWatch client class:

.put_metric_alarm.
.disable_alarm_actions.

Create an IAM role whose policy grants permission to
describe, reboot, stop, or terminate an Amazon EC2 instance.

Use the following role policy when creating the IAM role.
------------------------------------------------------------------------
    {
       "Version": "2012-10-17",
       "Statement": [
          {
             "Effect": "Allow",
             "Action": [
                "cloudwatch:Describe*",
                "ec2:Describe*",
                "ec2:RebootInstances",
                "ec2:StopInstances*",
                "ec2:TerminateInstances"
             ],
             "Resource": [
                "*"
             ]
          }
       ]
    }
------------------------------------------------------------------------
"""
## Create and Enable Actions on an Alarm
"""
************************************************************************
Create or update an alarm and associate it with the specified metric.
Optionally, this operation can associate one or more Amazon SNS
resources with the alarm.

When this operation creates an alarm, the alarm state is immediately
set to INSUFFICIENT_DATA.
The alarm is evaluated and its state is set appropriately.
Any actions associated with the state are then executed.

When you update an existing alarm, its state is left unchanged,
but the update completely overwrites the previous configuration of the alarm.
The example below shows how to:

- Create an alarm and enable actions using put_metric_alarm.
************************************************************************
"""
import boto3

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Create alarm with actions enabled
cloudwatch.put_metric_alarm(
    AlarmName='Web_Server_CPU_Utilization',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=60,
    Statistic='Average',
    Threshold=70.0,
    ActionsEnabled=True,
    AlarmActions=[
      'arn:aws:swf:us-west-2:{CUSTOMER_ACCOUNT}:action/actions/AWS_EC2.InstanceId.Reboot/1.0'
    ],
    AlarmDescription='Alarm when server CPU exceeds 70%',
    Dimensions=[
        {
          'Name': 'InstanceId',
          'Value': 'INSTANCE_ID'
        },
    ],
    Unit='Seconds'
)
## Disable Actions on an Alarm
"""
************************************************************************
Disable the actions for the specified alarms.
When an alarm's actions are disabled, the alarm actions do not execute
when the alarm state changes.

The example below shows how to:

- Disable metric alarm actions using disable_alarm_actions.
************************************************************************
"""
import boto3

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Disable alarm
cloudwatch.disable_alarm_actions(
  AlarmNames=['Web_Server_CPU_Utilization'],
)
