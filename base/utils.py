import logging
import random
import string


from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

logger = logging.getLogger(__name__)


class PhoneNumber:
    def __init__(self, country_code, national, international):
        self.country_code = country_code
        self.national = national
        self.international = international

    def __str__(self):
        return f"{self.country_code}, {self.national}"


# Download the file from `url` and save it locally under `file_name`:

def key_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def send_email_test(subject, message, from_email, to_emails: list):
    send_mail(subject, message, from_email, to_emails, fail_silently=False)


def email_account_verification(to_email, code):
    from django.core.mail import EmailMultiAlternatives
    from django.template.loader import render_to_string

    context = {"subject": "Email Verification", "code": f"{code}"}
    subject = render_to_string(
        "emails/verification/non_individuals_subject.html", context
    ).strip()
    text_body = render_to_string(
        "emails/verification/non_individuals_body.txt", context
    )
    html_body = render_to_string(
        "emails/verification/non_individuals_body.html", context
    )
    msg = EmailMultiAlternatives(
        subject=subject,
        from_email=f"{settings.EMAIL_HOST_USER}",
        to=[f"{to_email}"],
        body=text_body,
    )
    msg.attach_alternative(html_body, "text/html")
    msg.send()
