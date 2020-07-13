# COM03-AWS100 - Launch a Hello World website on the internet

## Cloud Service Provider
- Amazon Web Services

## Difficulty
- Level 100 (Introductory)

## Estimated Time
- One to Two hours. 

## Project's Author(s)

[Syed Auther](https://twitter.com/syedauther)

## Objectives

### You need to complete the following:
- Launch a linux based EC2 instance in any one region of your choice in a public subnet 
- Setup a security group that allows http/https connections from the Internet, and ssh from your IP address
- ssh into the EC2 instance
- setup a webserver on the EC2 instance
- add a simple hello world header to the index.html file 
- Hit the public IP address from a browser and confirm the site is served


### You need to answer the following:
- What is a region? 
- What is an availability zone? 
- What is a public subnet? 
- How many subnets can there be in one region? 
- How to launch EC2 instances in public / private subnets? 
- What are AMIs? 
- What are security groups? 
- What are inbound/outbound rules? 
- what is deny By default rule in security groups?
- How to allow access to EC2 from security groups? 
- How to connect to EC2 instances from your machine? 
- How to setup your simple static site with ec2? 




## References
- [What Is Amazon EC2?](https://aws.amazon.com/ec2/faqs/)
- [Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html#:~:text=A%20security%20group%20acts%20as,one%20or%20more%20security%20groups.)
- [Installing httpd](http://httpd.apache.org/docs/2.4/install.html)
- [ssh into ec2 - linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)

## Ideas
- For windows users [Download and install Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
- Connecting to a Linux EC2 instance from Windows is not possible natively, you will need an ssh client such as Putty to connect , and you will need to follow these steps to [ssh into ec2 from windows](https://stackoverflow.com/questions/5264945/ssh-to-ec2-linux-instance-from-windows)
- You can also launch non linux EC2 instances for example windows servers, for which you will need to RDP into.  

## Tips
- Use t2.micro instances from the free tier as it will suffice for this static site 
- Use the default setting on the storage screen as 8GB of EBS storage will be enough for this project.