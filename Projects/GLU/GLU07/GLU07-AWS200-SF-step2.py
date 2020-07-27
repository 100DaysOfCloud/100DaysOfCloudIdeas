def lambda_handler(event, context):
	#check if the previous step has passed the data , else initialize sum_from_prev_step variable to 2
    sum_from_prev_step=event['sum'] if 'sum' in event else 2

    #return the square of the sum from previous step
    return {"final": sum*sum }
    