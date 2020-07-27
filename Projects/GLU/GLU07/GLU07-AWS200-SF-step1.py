
def lambda_handler(event, context):
	#check if 2 inputs a and b were passed, if they have not been passed initialize both inputs to 1
    a=event['a'] if 'a' in event else 1
    b=event['b'] if 'b' in event else 1

    # return the sum of the inputs to the next step
    return {"sum": a+b } 
