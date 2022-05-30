# cria politica

import boto3
import json

client = boto3.client('iam')

policy_json = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "iam:GetPolicy",
                "iam:GetUserPolicy",
                "iam:GetGroupPolicy",
                "iam:GetUser",
                "iam:GetGroup"
                ],
            "Resource": "arn:aws:iam::053145803431:policy/*"
        }
    ]   
}

response = client.create_policy(
    PolicyName='readTeste',
    PolicyDocument=json.dumps(policy_json),
    Description='Policy Read'
) 

print(response['Policy'])