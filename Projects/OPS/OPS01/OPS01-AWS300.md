# OPS01-AWS300 - Deploy a VPC with Terraform


## Cloud Service Provider
✍️ [You need to choose a single cloud provider, unless your project is multi-cloud]

- Amazon Web Services


## Difficulty

- Level 300 (Advanced)

## Estimated Time
- One hour 

## Project's Author(s)


- [Markus Mabson ](https://www.linkedin.com/in/markus-mabson-86917a133/)

## Objectives

### You need to complete the following:
- Download terraform binaries [Terraform binaries](https://www.terraform.io/downloads.html)
- Initialize terraform working directory 
- Document your environment (Draw.io)
- Create the following with Terraform deployment
    - Virtual Private Cloud (VPC)
    - Route Tables (public/private)
    - Route Table Associations
    - Internet Gateway
    - Elastic IP
    - Nat Gateway 
    - 1 EC2 Instance in public/ Private Subnet  (Amazon  Linux 2 AMI)
    - Security Groups
- Verify connectivity of public instance / private instance 
- Delete the Terraform deployment
- Verify resources are deleted 


### You need to answer the following:
- What is Infrastructure as Code (IaC)?
- What is Terraform 
- What is a state file used for?
- In what cases would you use Infrastructure as Code?
- 


## References
- [Terraform](https://www.terraform.io/)
- [Terraform module registry](https://registry.terraform.io/)

## Costs
- Included in the Free Tier


## Estimated time to complete
- 60 minutes
- 2 hours

## Tips
- Indent your code to make it concise and readable
Some resources may need to wait for another resource to be created. 
- It may be useful to create a key_pair in the management UI before creating the EC2 instances

