from user.models import Profile
from decouple import config
from datetime import datetime
from common.exceptions import WaitAssholeException
# from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


class MailingInterface:
    template_dir = 'emails/%s.html'
    # EMAIL ONE MINUTE TIME LIMITATION IS FOR ALL USERS
    # MAKE IT USER SPECIFIC
    last_email_date = datetime(1970, 1, 1)
    MIN_EMAIL_TIME_DIFFERENCE = 60  # secs

    @staticmethod
    def SendMessage(request, target_email, subject, template_name, dict_content):
        user = request.user
        time_passed_from_last_email, profile = Profile.get_email_time_passed(user)

        if 0 <= time_passed_from_last_email <= MailingInterface.MIN_EMAIL_TIME_DIFFERENCE:
            raise WaitAssholeException(time_passed_from_last_email)

        dict_content['user'] = user
        dict_content['domain'] = get_current_site(request)
        body = render_to_string(MailingInterface.template_dir % template_name, dict_content)
        MailingInterface.SendBySMTP(target_email, subject, body)
        if profile:
            profile.last_email_date = datetime.now()
            profile.save()

    @staticmethod
    def SendSignedMessage(request, user, target_email, subject, template_name):
        time_passed_from_last_email, profile = Profile.get_email_time_passed(user)

        if 0 <= time_passed_from_last_email <= MailingInterface.MIN_EMAIL_TIME_DIFFERENCE:
            raise WaitAssholeException(time_passed_from_last_email)

        body = render_to_string(MailingInterface.template_dir % template_name, {
            'user': user,
            'domain': get_current_site(request),
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user)
        })
        MailingInterface.SendBySMTP(target_email, subject, body)
        if profile:
            profile.last_email_date = datetime.now()
            profile.save()

    @staticmethod
    def SendBySMTP(target, subject, body):
        try:
            email = EmailMessage(subject, body, to=[target, ])
            email.content_subtype = 'html'
            res = email.send()
            if not res:
                raise Exception('Failed sending email due to unknwon reason!')
        except Exception as ex:
            print("Sending smtp email failed because: ", ex)
