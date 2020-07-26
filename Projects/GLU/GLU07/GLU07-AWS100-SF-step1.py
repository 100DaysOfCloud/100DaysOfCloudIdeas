def lambda_handler(event, context):
    a=event['a'] if 'a' in event else 1
    b=event['b'] if 'b' in event else 1
    return {"sum": a+b } 
