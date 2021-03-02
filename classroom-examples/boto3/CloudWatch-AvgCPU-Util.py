import boto3
import sys
from datetime import datetime, timedelta
    client = boto3.client('cloudwatch')
    response = client.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
            'Name': 'InstanceId',
            'Value': 'i-1234abcd'
            },
        ],
        StartTime=datetime(2018, 4, 23) - timedelta(seconds=600),
        EndTime=datetime(2018, 4, 24),
        Period=86400,
        Statistics=[
            'Average',
        ],
        Unit='Percent'
    )
for cpu in response['Datapoints']:
  if 'Average' in cpu:
    print(cpu['Average'])

# Alternative:
print(response)

for cpu in response['Datapoints']:
  print(cpu)
