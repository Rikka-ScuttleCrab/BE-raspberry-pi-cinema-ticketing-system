from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv
import os

conf = ConnectionConfig(
    MAIL_USERNAME="ticketscinemasupport@gmail.com",
    MAIL_PASSWORD="wxhk tjxs xaiq uuwr",
    MAIL_FROM="ticketscinemasupport@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)

load_dotenv()
template_dir = os.getenv("TEMPLATE_DIR")

env = Environment(
    loader=FileSystemLoader(template_dir)
)


template = env.get_template("ticket_email.html")


async def send_ticket_email(
    email: str,
    subject: str,
    body: str,
    qr_path: str
):

    message = MessageSchema(

        subject=subject,

        recipients=[email],

        body=body,

        subtype="html",

        attachments=[qr_path]
    )

    fm = FastMail(conf)

    await fm.send_message(message)