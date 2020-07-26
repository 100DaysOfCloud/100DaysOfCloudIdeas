def lambda_handler(event, context):
    sum_from_prev_step=event['sum'] if 'sum' in event else 2
    return {"final": sum*sum }
    