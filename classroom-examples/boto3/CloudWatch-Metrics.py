## Getting Metrics from Amazon CloudWatch
"""
**************************************************************************
This Python example shows you how to:

- Get a list of published CloudWatch metrics
- Publish data points to CloudWatch metrics

Metrics are data about the performance of your systems.
You can enable detailed monitoring of some resources, such as your Amazon CloudWatch instances, or your own application metrics.

In this example, Python code is used to get and send CloudWatch metrics data.
The code uses the uses the AWS SDK for Python to get metrics from
CloudWatch using these methods of the CloudWatch client class:

.paginate('list_metrics').
.put_metric_data.
*************************************************************************
"""
## List Metrics
"""
*************************************************************************
List the metric alarm events uploaded to CloudWatch Logs.

The example below shows how to:

- List metric alarms of incoming log events using paginate('list_metrics').
*************************************************************************
"""
import boto3

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# List metrics through the pagination interface
paginator = cloudwatch.get_paginator('list_metrics')
for response in paginator.paginate(Dimensions=[{'Name': 'LogGroupName'}],
                                   MetricName='IncomingLogEvents',
                                   Namespace='AWS/Logs'):
    print(response['Metrics'])

## Publish Custom Metrics
"""
*************************************************************************
Publish metric data points to Amazon CloudWatch.
Amazon CloudWatch associates the data points with the specified metric.
If the specified metric does not exist, Amazon CloudWatch creates the metric.
When Amazon CloudWatch creates a metric, it can take up to fifteen minutes
for the metric to appear in calls to ListMetrics.

The example below shows how to:

- Publish custom metrics using put_metric_data.
*************************************************************************
"""
import boto3

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Put custom metrics
cloudwatch.put_metric_data(
    MetricData=[
        {
            'MetricName': 'PAGES_VISITED',
            'Dimensions': [
                {
                    'Name': 'UNIQUE_PAGES',
                    'Value': 'URLS'
                },
            ],
            'Unit': 'None',
            'Value': 1.0
        },
    ],
    Namespace='SITE/TRAFFIC'
)
