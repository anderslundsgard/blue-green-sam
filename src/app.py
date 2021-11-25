import json


def lambda_handler(event, context):

    print('Running Lambda with python 3.x!')

    message = "Lokalise Everything! - Deploy strategy: Linear10PercentEvery1Minute"

    return {
        "statusCode": 200,
        "body": json.dumps({"message": message}),
    }
