from email.message import EmailMessage
from typing import List, Union
from mypy_boto3_ses import SESClient
from mypy_boto3_sesv2 import SESV2Client
import imghdr


class SesClient:
    client: Union[SESClient, SESV2Client]

    def __init__(
        self, client: Union[SESClient, SESV2Client]
    ):
        self.client = client


    def send_email(self, from_:str, to:str,message:str, attachments:List[str]):
        source = self._source(from_)
        msg = self._create_multipart_message(
            source, to, message, attachments
        )
        self.client.send_email(
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

        for attachment in attachments or []:
            file= open(attachment, "rb")
            img_data = file.read()
            msg.add_attachment(
                img_data,
                maintype='image',
                subtype=imghdr.what(None, img_data),
            )
        return msg
