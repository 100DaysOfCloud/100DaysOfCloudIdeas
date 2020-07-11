# SEC01-AWS200 — Create a new CMK in KMS and encrypt an object

## Cloud Service Provider
- Amazon Web Services

## Difficulty

- Level 200 (Intermediate)

## Project's Author(s)

- [Andrew Brown](https://twitter.com/andrewbrown)

## Objectives

### You need to complete the following:

- Create a new Customer Master Key (CMK) in Key Management Service (KMS)
- Create a new S3 bucket
- Upload an object (file) to the S3 Bucket
- Encrypt the uploaded file with your custom CMK

### You need to answer the following:

- What is a Hardware Security Module (HSM)?
- What is the difference between multi-tenant and single-tenant HSM?
- What is the cost for for CloudHSM?
- What is key rotation?
- How much do KMS keys cost?

## Ideas

- Creating a single CMK key will result in $1 USD per month so ensure
  you delete your key at the end of this project.

## References

- [Key Management Service](https://aws.amazon.com/kms/)
- [CloudHSM](https://aws.amazon.com/cloudhsm/)
- [AWS Key Management Service concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)
