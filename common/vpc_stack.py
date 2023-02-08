import config

from aws_cdk import (Stack,
    aws_ec2 as ec2,
    Tags)

from constructs import Construct

STACK_ID = "dca-common"
VPC_NAME = f'{STACK_ID}-vpc'

class VpcStack(Stack):

    def __init__(self, scope: Construct, env: dict, **kwargs) -> None:
        super().__init__(scope, STACK_ID, **kwargs)
        self.vpc = ec2.Vpc(self, VPC_NAME, max_azs=2)

        # Tag all resources in this Stack's scope with a cost center tag
        Tags.of(scope).add(config.COST_CENTER_CONTEXT, env.get(config.COST_CENTER_CONTEXT))
