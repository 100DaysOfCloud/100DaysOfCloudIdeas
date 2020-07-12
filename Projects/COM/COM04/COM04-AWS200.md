# COM04-AWS200 - Create a cluster of virtual machines using docker swarm

## Cloud Service Provider

- Amazon Web Services

## Difficulty

- Level 200 (Intermediate)

## Project's Author(s)

[Karan Gauswami](https://github.com/KaranGauswami)

## Objectives

### You need to complete the following:

- Create a VPC for our EC2 Instances
- Create an EC2 Instance with initial script to install Docker
- Setup that EC2 Instance as a manager node
- Create multiple instances (4 to 5) with initial script to create worker nodes and join that manager node
- Start any service like nginx to test our Swarm Cluster
- Scale that service to multiple nodes
- Delete all the resources you created after completion

### You need to answer the following:

- How to check status of Docker nodes ?
- What behaviour is expected if one of the Worker or Manager node went down ?
- How to get state of all the containers running on diffrent nodes ?
- How to get token to add more workers and managers ?

## References

- [Running commands on your Linux instance at launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)
- [Install Docker](https://docs.docker.com/engine/install/ubuntu/)
- [Get Started with Docker Swarm](https://docs.docker.com/engine/swarm/swarm-tutorial)

## Costs

- Included in the Free Tier
- \$1-2 per hour running

## Estimated time to complete

- 30-45 minutes

## Tips

- Use t2.micro instances for creating nodes to avoid unexpected charges.
- To add more Manager or Worker node , It is not required to SSH into that Instance.
- Open SSH port for only required machines in Securiy groups.
