
# LES01-AWS200 - Create a Serverless API 
## Cloud Service Provider
- Amazon Web Services

## Difficulty
- Level 200 (Intermediate)

## Estimated Time
- One to Two hours. 

## Project's Author(s)

[Syed Auther](https://twitter.com/syedauther)

## Objectives

### You need to complete the following:
- Create an AWS Lambda with a language of your choice, the purpose of this Lambda is to respond with a 'Hello Serverless World!' message.
- Create an API Gateway endpoint and connect it to the AWS Lambda function created above and deploy it as an API that can be consumed from POSTMAN.
- Secure the API with an API Key




### You need to answer the following:
- What is Function as a service? 
- How many languages are supported by AWS Lambda
- What is the maximum memory allocated to an AWS Lambda function?
- How many ways to deploy a Lambda function?
- Mention some triggers for AWS Lambda apart from API Gateway
- How to assign a role to AWS Lambda? 
- How many way to secure an API Gateway endpoint? 
- How to add API Gateway as a trigger for AWS Lambda? 

## References
- [AWS Lambda- Getting Started](https://aws.amazon.com/lambda/getting-started/)
- [API Gateway Getting Started](https://aws.amazon.com/api-gateway/getting-started/)
- [Connecting AWS Lambda and API Gateway](https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway-tutorial.html)
- [Securing the API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html)

## Ideas
- Use a browser to see if the output message 'Hello Serverless World!' is sent back as a response from your Lambda before securing your API. 
- You will need [POSTMAN](https://learning.postman.com/docs/getting-started/introduction/), for testing the API once its secured with an API Key. 
- POSTMAN is not a hard limit, but if you are familiar with any other testing utility you can use that too, but POSTMAN is a good to learn tool, that will come in handy for some other Serverless projects and APIs as well. 

## Tips
- Use the cloud9 IDE to code the hello world Lambda initially, and then explore other deployment ideas like zip file uploads and SAM deployments
- The AWS Lambda free usage tier includes **1M free requests per month and 400,000 GB-seconds of compute time per month**, so feel free to explore unhinged! 

