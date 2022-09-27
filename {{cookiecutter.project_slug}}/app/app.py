
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.data_classes import event_source, SNSEvent
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()

def lambda_handler(event: SNSEvent, context: LambdaContext):
    logger.info(f"Enter to function handler: event: {event.raw_event}")


    return {
        'statusCode': 200
    }