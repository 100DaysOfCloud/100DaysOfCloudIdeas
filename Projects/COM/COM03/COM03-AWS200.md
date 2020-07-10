# COM03-AWS200 - Create an Auto Scaling Group

## Cloud Service Provider
- Amazon Web Services

## Difficulty
- Level 200 (Intermediate)

## Project's Author(s)

[Chris Nagy](https://twitter.com/chris_the_nagy)

## Objectives

### You need to complete the following:
- Create a Launch Configuration
- Create an Auto Scaling Group with a minimum of two and maximum of five EC2 instances
- Delete one instance manually
- After the ASG is in place, increase the desired number of instances to three (after the ASG is in place)
- Delete all the resources you created


### You need to answer the following:
- What are the key differences between a Launch Template and Launch Configuration?
- What happens if you delete one of the running instances in an ASG manually?
- How can you set and change the minimum, desired and maximum number of instances in an ASG?
- Based on what metrics can an ASG spin up / spin down instances?
- What EC2 configuration settings can you set in a Launch Template/Configuration?
- Can you use Spot instances with a Launch Template/Configuration?
- How many subnets and regions can a single ASG utilize?
- What is the difference between "desired capacity" and "minimum capacity"?
- In which order will EC2 instances be terminated in case of a scale-in event?

## References
- [What Is Amazon EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
- [Auto Scaling Groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html)
- [AWS Auto Scaling FAQs](https://aws.amazon.com/autoscaling/faqs/)

## Tips
- Use t2.small instances for the Auto Scaling Group to avoid unexpected charges.
- Don't panic if the instances always come back after you delete them, there's a reason for that.
