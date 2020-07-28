# DEV03-AWS100 —  Install & Configure AWS CLI then create an S3 Bucket

## Cloud Service Provider
* Amazon Web Services (AWS)

## Difficulty
Level 100 (Introductory)

## Estimated Time
* 30 - 40 minutes
  
## Project's Author(s)
* [Ariela](https://twitter.com/ari_hacks)

## Objectives

###  You need to complete the following:

* Create an IAM user (with Administrator Access) if you do not have one already
* Install AWS CLI 
* Configure AWS credentials locally: `aws configure` 
* Create an S3 bucket: `aws s3 mb s3://<unique-bucket-name>`
* Check the bucket was created: `aws s3 ls`
* Delete the bucket when you are done: `aws s3 rb s3://<unique-bucket-name>`

###  You need to answer the following: 

* How are permissions granted to IAM users?
* What settings are created when configuring AWS locally and where are they stored? 
* What is the difference between `s3` and `s3api` Commands?
  

## References

* [Create an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
* [Install AWS CLI on MacOS](https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html) or with Homebrew:  `brew install awscli` `aws --version`
* [Install AWS CLI on Windows](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html)
* [Install AWS CLI on Linux](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html)
* [Configure AWS locally](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
* [Leveraging the s3 and s3api Commands](https://aws.amazon.com/blogs/developer/leveraging-the-s3-and-s3api-commands/)
