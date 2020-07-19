# OPS04-AWS100 - Create a CloudWatch Alarm

## Cloud Service Provider
- Amazon Web Services

## Difficulty
- Level 200 (Intermediate)

## Project's Author(s)
- [@andrewbrown](https://twitter.com/andrewbrown)

## Objectives

### You need to complete the following:
- Launch an EC2 t2-micro instance with a public IP address and supply the [provided bash script](OPS04-AWS200-userdata.sh) to install a simple website with an apache server in the UserData.
- Visit the the public IP so that you are generating NetworkIn. You need
  to do this so the Metric appears selectable when create your
CloudWatch Alarm
- Create a CloudWatch Alarm and use EC2 NetworkIn as the metric
- Set your CloudWatch Alarm to use a 5 minute period
- Set your CloudWatch Alarm to a very low static threshold such as 5000
- Set the Datapoint to alarms to 3 of 4
- Try to get the Alarm to trigger an Alert state by visiting the website
  and generating NetworkIN

### You need to answer the following:
- What is a CloudWatch Alarm?
- What is a metric?
- What do we mean when we say "breach"?
- What is a threshold?
- What is a data point?
- What is a period?
- What are evaluation periods?

## References
- [NetworkIN Instance Metric](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html#ec2-cloudwatch-metrics)
- [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

## Costs
- t2.micro is included in Free Tier
- First 10 CloudWatch Alarms are in Free Tier

## Estimated time to complete
- 45 minutes

## Tips
- It takes EC2 5 minutes before it reports NetworkIN so expect to wait
  5-10 mins after visiting the website intially

