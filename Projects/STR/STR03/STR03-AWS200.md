# STR03-AWS200 - Create an EFS shared file system

## Cloud Service Provider
- Amazon Web Services

## Difficulty
- Level 200 (Intermediate)

## Project's Author(s)
[Chris Nagy](https://twitter.com/chris_the_nagy)

## Objectives

### You need to complete the following:

- Create an EFS file system
- Spin up two EC2 instances in two seperate AZs in the same region
- Make sure you can SSH into both instances
- Mount the EFS volume on both instances
- Create a simple text file on the EFS volume with Instance-1
- Open that file on the EFS volume with Instance-2

### You need to answer the following:
- From how many regions and availability zones can a single EFS volume be accessed?
- What network protocol does EFS use?
- How many instances can an EFS volume be mounted on simultaneously?
- How is the throughput [speed] of an EFS volume determined?
- What do the performance and throughput mode settings influence?
- How can access to an EFS volume be limited?
- Does EFS support security groups?
- Does EFS support encryption at rest and in-transit?
- What is EFS Infrequent Access (EFS IA)?
- What is the operating system requirement for mounting an EFS volume?
- What are the key differences between EFS and EBS volumes?

## References
- [Getting Started with EFS](https://docs.aws.amazon.com/efs/latest/ug/getting-started.html)
- [Security in EFS](https://docs.aws.amazon.com/efs/latest/ug/security-considerations.html)
- [EFS Performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html)

## Costs
- 5GB of EFS file storage is included in the free tier

## Estimated time to complete
- 60-90 minutes

## Tips
- Make sure to expose the EFS volume to only and all the necessary availability zones.
- Pre-built commands for mounting the EFS volume are provided in the volume's console.
- Storing small amounts of data on an EFS volume can lead to performance issues.