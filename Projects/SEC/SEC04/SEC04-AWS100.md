
# SEC04-AWS100 — Create an IAM user

## Cloud Service Provider

* Amazon Web Services

## Difficulty
* Level 100 (Introductory)

## Estimated time:
 * 1 hour

## Cost
* IAM is a free service

## Project's Author(s)
* [Syed Auther](https://twitter.com/syedauther)

## Objectives

### You need to complete the following:

* Create a new user in AWS IAM with programmatic and console access
* Add user to Admin group 
--Create a new group called "Admins"
--Add the AdministratorAccess managed policy to the new group
--Add your new user to the "Admins" group
* Enable MFA for the IAM root user 
* Apply an IAM password policy with best security practices.



### You need to answer the following: 

* What is Identity and Access Management? 
* What is a root user?
* How is a root user different from an Admin user? 
* What is console access and programmatic access? 
* What is the access key and secret key? 
* What is MFA for root user? Why is it a good practise to configure MFA? 
* What are policies and how to create them?
* What are roles and how to create them?
* What is the difference between a role and a policy?
* What is a user group? 
* What are some good security practices for password policies? 

## References

* [Root user in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html)
* [Policy examples](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_examples.html)
* [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
* [IAM Best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
* [Creating an Admin user](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
* [Setting a password policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html?icmpid=docs_iam_console)


## Tips
* User [Google Authenticator ](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2) for MFA.
* Do not ever commit, add or push any of your access and secret keys to source control systems like git, or any other publicly accessible platform where others can access it. If you accidentaly have done so, make sure to delete the access and secret keys immediately in your console and generate new ones. 