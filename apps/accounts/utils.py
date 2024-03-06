from django.core.mail import EmailMessage
import os
from os import getenv
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from django.conf import settings

User = settings.AUTH_USER_MODEL

class EmailAccount:
    """
    This class helps with the distribution of
    Sending email based on contactus.
    """

    def __init__(
        self,
        account: User = None,
        from_email: str = getenv("EMAIL_HOST_USER"),
        type_content: str = "text/html",
    ):
        self.account = account
        self.from_email = from_email
        self.type_content = type_content

    def _send_email_in_batches(self, recipients_content_list: list):
        """Sends emails to a list of recipients in batches of 50 with HTML content."""
        batch_size = 50
        for i in range(0, len(recipients_content_list), batch_size):
            batch_recipients = recipients_content_list[i : i + batch_size]
            for recipient in batch_recipients:
                msg = EmailMultiAlternatives(
                    subject=recipient["subject"],
                    from_email=self.from_email,
                    to=[recipient["email"]],
                )
                msg.attach_alternative(recipient["text_content"], self.type_content)
                msg.send()

    def send_email_registre(self):
        if self.account:
            account_email = self.account.email
            account_name = self.account.name

            recipients_content_dict = [
                {
                    "email": account_email,
                    "subject": _("Bienvenido a Cleopath-ra"),
                    "text_content": render_to_string(
                        "account/register_confirmation.html",
                        context={
                            "name": account_name,
                        },
                    ),
                }
            ]

            self._send_email_in_batches(recipients_content_dict)

    def send_email_reset_password(self, reset_link):
        recipients_content_dict = [
            {
                "email": self.account.email,
                "subject": _("Reset Your Password"),
                "text_content": f"Haz click en el siguiente enlace para restablecer tu contraseña: {reset_link}",
            }
        ]

        self._send_email_in_batches(recipients_content_dict)
