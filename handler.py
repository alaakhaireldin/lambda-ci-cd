import json
import pyjokes


def get_joke(event, context):
    body = {
        "message": "Greetings from Github. Your function is deployed by a Github Actions. Enjoy your joke",
        "joke":pyjokes.get_joke()
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
