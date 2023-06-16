#!/usr/bin/env python3

import os
import os.path
import mimetypes
import smtplib
import email.message


def generate_email(sender, recipient, subject, body, attachment):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] =  subject
    message.set_content(body)

    attachment_name = os.path.basename(attachment)
    mime_type, _ = mimetypes.guess_type(attachment)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment, 'rb') as path:
        message.add_attachment(path.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=attachment_name)
        return message

def generate_error(sender, recipient, subject, body):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] =  subject
    message.set_content(body)

    return message

def email_send(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

