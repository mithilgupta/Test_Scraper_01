
# GitHub Actions imported from: https://www.youtube.com/watch?v=xs9oJaaU8I8&t=265s
import json
from extra_utils import get_lambda_message

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(get_lambda_message())
    }


if __name__ == "__main__":
	print (lambda_handler({},{}))
