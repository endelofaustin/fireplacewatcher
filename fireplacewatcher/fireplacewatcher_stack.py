from aws_cdk import (
    Stack,
    aws_lambda as _lambda
)
from constructs import Construct
import os

class FireplacewatcherStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda function
        _lambda.Function(
            self, "BasicLambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="handler.handler",
            code=_lambda.Code.from_asset("lambda")
        )

