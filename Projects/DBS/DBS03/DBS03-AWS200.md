# DBS03-AWS200 - Create an Aurora RDS Database

## Cloud Service Provider
- Amazon Web Services

## Difficulty
- Level 200 (Intermediate)

## Project's Author(s)
- [Nathan Cho](https://twitter.com/hatchcanon)

## Objectives

### You need to complete the following:
- Create a Security Group in your default VPC that allows traffic from `0.0.0.0/0` (public internet) on port `3306`
- Use the "standard create" mode and choose "MySQL compatibility" with "regional" and "Dev/Test" mode
- Specify your own password for the database
- Choose the db.r5.large instance size
- Choose the region's default VPC
- Enable "Public Access" and add the above created Security Group
- Create the database
- Connect from your computer to the newly created database with a MySQL DBMS like [MySQL Workbench](https://dev.mysql.com/downloads/workbench/?os=src) or [Sequel Ace](https://github.com/Sequel-Ace/Sequel-Ace)
- Create a test table in your database to verify everything is working correctly
- Delete the database


### You need to answer the following:
- What type of database is Aurora?
- What is the minimum storage for Aurora?
- What is Aurora Serverless and how does it differ from regular RDS DB instances?
- How does Aurora's data distribution (redundancy) work, and what are the options for more redundancy?
- How do Aurora's read & write replicas work?
- What is the difference between a "reader" and a "writer" endpoint/instance?
- What are the four types of Aurora Endpoints?
- Does Aurora offer database encrpytion?
- Why is it a bad idea to enable "Public Access"? Why did we enable public access this time?


## References
- [AWS Create a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateDBInstance.html)
- [RDS FAQs](https://aws.amazon.com/rds/faqs/)
- [An Introduction to Amazon Aurora](https://dzone.com/articles/an-introduction-of-amazon-aurora)

## Costs
- Amazon Aurora is not included in the free tier
- An Aurora database running on a db.r5.large instance [will cost $0.29 per hour](https://aws.amazon.com/rds/aurora/pricing/)

## Estimated time to complete
- 60 minutes

## Tips
- To delete the database, make sure that you have disabled "deletion protection"
