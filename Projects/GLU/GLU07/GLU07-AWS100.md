# GLU07-AWS100 - Setup a simple state machine with at least 2 steps
## Cloud Service Provider
- Amazon Web Services

## Difficulty
- Level 200 (Intermediate)

## Estimated Time
- 60 minutes 

## Estimated Cost
- This project is included in the free tier. 


## Project's Author(s)

- [Syed Auther](https://twitter.com/syedauther)

## Objectives

### You need to complete the following:
* Create an AWS Lambda to add 2 numbers supplied as input -[ sample code for step 1](./GLU07-AWS100-SF-step1.py?raw=true)  
* Create an AWS Lambda to return the square of a number-  [ sample code for step 2](./GLU07-AWS100-SF-step2.py?raw=true)  
* Create a state machine to connect the above two Lambdas
	* Go to the step  functions console click on create state machine , do not chnage the default settings.
	* Copy [ this ](./GLU07-AWS100-SF-step2.py?raw=true) template to paste into Definition but carefully replace Lambda ARNs with the Lambdas created in above steps where necessary in the template. 
* Execute the state machine and verify the output.




### You need to answer the following:
- What is a step function? What is a state machine? 
- What is workflow configuration and  state management?
- What is [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html)?
- What are tasks? 
- How to visualize the state machine? 



## References
- [AWS Step Functions- Getting Started](https://aws.amazon.com/step-functions/)
- [FAQs](https://aws.amazon.com/step-functions/faqs/)
- [Features of Step functions](https://aws.amazon.com/step-functions/features/)
- [Tasks in step functions](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-task-state.html)
- [Wait state in step functions](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-wait-state.html)
- [I/O data  processing ](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-input-output-filtering.html)

## Ideas
- Just create a Lambda function with default settings and choose the language you want to code in, if you do not want the exact same implementation as this excercise. Make your own flow, take a look at some [use cases](https://aws.amazon.com/step-functions/use-cases/)