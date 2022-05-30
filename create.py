#cria user

import boto3
iam = boto3.client('iam')

client = boto3.client('iam')

response = client.create_user(UserName='Rodrigo')
print(response)




