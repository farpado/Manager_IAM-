#Desativa chave / ativa
import boto3
iam = boto3.client('iam')


client = boto3.client('iam')
response = client.update_access_key(
    UserName='Iam',
    AccessKeyId='AKIAQYX54TKT4VBYXDUZ',
    Status='Active'
)
