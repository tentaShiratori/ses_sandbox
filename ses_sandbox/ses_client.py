from email.message import EmailMessage
from typing import List, Union
from mypy_boto3_ses import SESClient
from mypy_boto3_sesv2 import SESV2Client
import imghdr
import boto3
import os


class SesClient:
    v1client: SESClient
    v2client: SESV2Client

    def __init__(
        self
    ):
        self.v1client = boto3.client('ses', region_name='ap-northeast-1',aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
        self.v2client = boto3.client('sesv2', region_name='ap-northeast-1',aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
    


    def v1_send_email(self, from_:str, to:str,message:str, attachments:List[str]):
        source = self._source(from_)
        msg = self._create_multipart_message(
            source, to, message, attachments
        )
        self.v1client.send_raw_email(
            Source=source,
            Destinations=[to],
            RawMessage= {"Data": msg.as_string()},
        )
    def v2_send_email(self, from_:str, to:str,message:str, attachments:List[str]):
        source = self._source(from_)
        msg = self._create_multipart_message(
            source, to, message, attachments
        )
        self.v2client.send_email(
            FromEmailAddress=source,
            Destination={"ToAddresses": [to]},
            Content={"Raw": {"Data": msg.as_string()}},
        )

    def _source(self, source:str) -> str:
        return f"Test<{source}>"
    
    def _create_multipart_message(
        self,
        from_: str,
        to: str,
        message: str,
        attachments: List[str],
    ) -> EmailMessage:
        msg = EmailMessage()
        msg["Subject"] = "テストメールです"
        msg["From"] = from_
        msg["To"] = ", ".join([to])

        msg.set_content(message)

        for (index, attachment) in enumerate(attachments):
            _, file_extension = os.path.splitext(attachment)
            file= open(attachment, "rb")
            img_data = file.read()
            msg.add_attachment(
                img_data,
                maintype='image',
                subtype=imghdr.what(None, img_data),
                filename=f"image{index}{file_extension}",
            )
        return msg
