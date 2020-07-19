# STR04-AWS100 - Create an S3 Bucket and store an object in it

## Cloud Service Provider
- Amazon Web Services

## Difficulty
- Level 100 (Introductory)

## Project's Author(s)
- [Syed Auther](https://twitter.com/syedauther)

## Objectives

### You need to complete the following:

- Using the console, create an S3 bucket
- Upload an object (any file) into the bucket


### You need to answer the following:
- What is Simple Storage Service (S3)?
- What is a bucket?
- What is object storage?
- How is object storage different than block storage?
- What is the maximum amount of data that you can store in an S3 bucket? 
- What is the maximum file size you can store in an S3 bucket?
- By default, are objects in an S3 bucket public?
- What are the security best practices regarding S3 buckets?
- What is an S3 bucket policy?
- What are storage classes in S3?
- How is a bucket policy different from an IAM policy? 

## References
- [Getting Started with S3](https://docs.aws.amazon.com/AmazonS3/latest/gsg/GetStartedWithS3.html)
- [Intro to S3](https://www.youtube.com/watch?v=M_t32mJCXqI)
- [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
- [Uploading your first object into a bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/PuttingAnObjectInABucket.html)
- [Bucket Policies](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html)
- [Storage classes in S3](https://aws.amazon.com/s3/storage-classes/)
- [Security breach due to public bucket policies](https://www.bleepingcomputer.com/news/security/540-million-facebook-records-leaked-by-public-amazon-s3-buckets/)

## Costs
- This project is included in the free tier.
- The free tier includes 5GB of Amazon S3 storage in the S3 Standard storage class; 20,000 GET Requests; 2,000 PUT, COPY, POST, or LIST Requests; and 15GB of Data Transfer Out each month.
- An empty bucket does not incur any costs.
- [S3 Pricing after free tier exhaustion](https://aws.amazon.com/s3/pricing/?nc=sn&loc=4)

## Estimated time to complete
- 15 minutes

## Tips
- Each bucket's name has to be unique _globally_, across every single bucket in the world.
- Try to get the URL for the object you uploaded in this task and access it using a browser, you should get an access denied error
- Do not store sensitive information in a bucket that has public access.
- Do not turn on _versioning_ on this bucket, it will be difficult to delete.
