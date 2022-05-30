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
               "iam:DeactivateMFADevice",
                "iam:CreateServiceSpecificCredential",
                "iam:DeleteAccessKey",
                "iam:DeleteGroup",
                "iam:UpdateOpenIDConnectProviderThumbprint",
                "iam:RemoveRoleFromInstanceProfile",
                "iam:UpdateGroup",
                "iam:CreateRole",
                "iam:AddRoleToInstanceProfile",
                "iam:CreateLoginProfile",
                "iam:DeleteServerCertificate",
                "iam:UploadSSHPublicKey",
                "iam:DeleteOpenIDConnectProvider",
                "iam:ChangePassword",
                "iam:UpdateLoginProfile",
                "iam:UpdateServiceSpecificCredential",
                "iam:CreateGroup",
                "iam:RemoveClientIDFromOpenIDConnectProvider",
                "iam:UpdateUser",
                "iam:DeleteRole",
                "iam:UpdateRoleDescription",
                "iam:UpdateAccessKey",
                "iam:UpdateSSHPublicKey",
                "iam:UpdateServerCertificate",
                "iam:DeleteSigningCertificate",
                "iam:DeleteServiceLinkedRole",
                "iam:CreateInstanceProfile",
                "iam:ResetServiceSpecificCredential",
                "iam:DeleteSSHPublicKey",
                "iam:CreateVirtualMFADevice",
                "iam:CreateSAMLProvider",
                "iam:CreateUser",
                "iam:CreateAccessKey",
                "iam:PassRole",
                "iam:AddUserToGroup",
                "iam:RemoveUserFromGroup",
                "iam:EnableMFADevice",
                "iam:ResyncMFADevice",
                "iam:UpdateSAMLProvider",
                "iam:DeleteLoginProfile",
                "iam:DeleteInstanceProfile",
                "iam:UploadSigningCertificate",
                "iam:DeleteUser",
                "iam:CreateOpenIDConnectProvider",
                "iam:UploadServerCertificate",
                "iam:CreateServiceLinkedRole",
                "iam:DeleteVirtualMFADevice",
                "iam:UpdateRole",
                "iam:UpdateSigningCertificate",
                "iam:AddClientIDToOpenIDConnectProvider",
                "iam:DeleteServiceSpecificCredential",
                "iam:DeleteSAMLProvider"
                ],
            "Resource": "arn:aws:iam::053145803431:user/*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "iam:SetSecurityTokenServicePreferences",
                "iam:UpdateAccountPasswordPolicy",
                "iam:CreateAccountAlias",
                "iam:DeleteAccountAlias"
            ],
            "Resource": "*"
        }
    ]   
}

response = client.create_policy(
    PolicyName='writeTeste',
    PolicyDocument=json.dumps(policy_json),
    Description='Policy Write',
) 

print(response['Policy'])