from mypy_boto3_ses import SESClient
from mypy_boto3_sesv2 import SESV2Client
from dotenv import load_dotenv
from .ses_client import SesClient
from os.path import join, dirname
load_dotenv()


def main():
    client = SesClient()
    # client.v1_send_email(
    #     from_="tenta.shiratori@gmail.com",
    #     to="tenta.developer@gmail.com",
    #     message="テストメールです",
    #     attachments=[join(dirname(__file__), "./images/10MB.JPG")],
    # )
    client.v2_send_email(
        from_="tenta.shiratori@gmail.com",
        to="tenta.developer@gmail.com",
        message="テストメールです",
        attachments=[
            join(dirname(__file__), "./images/10MB.JPG"),
            join(dirname(__file__), "./images/10MB.JPG"),
        ],
    )
if __name__ == "__main__":
    main()