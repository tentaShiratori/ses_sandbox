import boto3
from mypy_boto3_ses import SESClient
from mypy_boto3_sesv2 import SESV2Client
from dotenv import load_dotenv
import os
from .ses_client import SesClient
from os.path import join, dirname
load_dotenv()


def main():
    # Create an ses client
    ses:SESClient = boto3.client('ses', region_name='ap-northeast-1',aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
    # Create an sesv2 client
    sesv2:SESV2Client = boto3.client('sesv2', region_name='ap-northeast-1',aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
    client = SesClient(sesv2)
    client.send_email(
        from_="tenta.shiratori@gmail.com",
        to="tenta.developer@gmail.com",
        message="テストメールです",
        attachments=[join(dirname(__file__), "./images/10MB.JPG")],
    )
if __name__ == "__main__":
    main()