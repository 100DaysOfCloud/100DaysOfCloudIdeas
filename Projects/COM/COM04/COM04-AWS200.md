# COM04-AWS200 - Deploy a Docker container image on AWS Fargate

## Cloud Service Provider

- Amazon Web Services

## Difficulty

- Level 200 (Intermediate)

## Project's Author(s)

- [Johan Rin](https://twitter.com/johanrin)

## Objectives

### Prerequisites

- [Push a Docker image to Amazon ECR repository](./COM04-AWS100.md)

### You need to complete the following:

- Configure your container with your Docker image
- Configure your task definition
- Define your service
- Configure your cluster

### You need to answer the following:

- What is a _container_?
- What is the difference between Soft memory limit and Hard memory limit for a custom container?
- What is a _task definition_?
- What is the name of the default task execution role?
- What does a task size allow?
- What is a _service_?
- Which load balancer type Fargate can handle?
- How many security groups are created by default if you use a load balancer?
- What is a _cluster_?
- What are cluster names limitations?

## References

- [Getting started with Amazon ECS using Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-fargate.html)
- [Deploy Docker Containers](https://aws.amazon.com/getting-started/hands-on/deploy-docker-containers/)
- [How Amazon ECS manages CPU and memory resources](https://aws.amazon.com/blogs/containers/how-amazon-ecs-manages-cpu-and-memory-resources/)
- [Amazon ECS Task Execution IAM Role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html)

## Costs

- Included in the Free Tier

## Estimated time to complete

- 45 minutes - only if you already have a Docker image
