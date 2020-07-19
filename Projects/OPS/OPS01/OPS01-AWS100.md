# OPS01-AWS100 — Deploy a CloudFormation template from the AWS Console

## Cloud Service Provider

- Amazon Web Services

## Difficulty

- Level 100 (Introductory)

## Estimated Time
- One hour

## Project's Author(s)
- [Syed Auther](https://twitter.com/syedauther)
- [Chris Nagy](https://twitter.com/chris_the_nagy)

## Objectives

### You need to complete the following:

- Download our simple, pre-made [CloudFormation template](./OPS01-AWS100-CFTEMPLATE.yaml)
- Go to the CloudFormation Console in AWS
- Choose _create stack with new resources_ and use the template file from above
- At the _"Configure stack options"_, leave everything on default
- Watch as CloudFormation deploys the resources
- Make sure that there is a new DynamoDB Table, and a new S3 bucket deployed
- Delete the stack in the CloudFormation console
- Make sure both resources got deleted

### You need to answer the following: 

- What is Infrastructure as Code (IaC)?
- What is CloudFormation? 
- What is a CloudFormation template?
- In what two file formats can a CloudFormation template be specified?
- What is a CloudFormation stack?
- Can the same template be used in other regions?
- What happens to the deployed resources when the stack gets deleted?

## References

- [CloudFormation Introduction](https://www.youtube.com/watch?v=GeERpAAKCsQ&list=PLBfufR7vyJJ6FhBhJJSaMkI-m2wyoPy-G&index=200)
- [AWS - Deploy a CloudFormation stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.Walkthrough.html#GettingStarted.Walkthrough.createstack)
- [CloudFormation Template structure](https://www.youtube.com/watch?v=NhQhltDp1o4&list=PLBfufR7vyJJ6FhBhJJSaMkI-m2wyoPy-G&index=202)

## Costs
- This project is included in the free tier
- There is no additional charge for using AWS CloudFormation. You do pay however for AWS resources (e.g. EC2 instances, S3 buckets) created by CloudFormation as if you created them by hand.






