from django.contrib.auth.backends import BaseBackend

from .models import account


class OtpBackend(BaseBackend):

    def authenticate(self, request, **kwargs):
        phone_number = kwargs.get('phone_number')
        if not phone_number:
            return None

        otp = kwargs.get('otp')
        if not otp:
            return None

        try:
            user = account.objects.get(phone_number=phone_number, otp=otp)
            if user.otp_valid(otp):
                return user
            return None
        except account.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = account.objects.get(pk=user_id)
        except account.DoesNotExist:
            return None

        return user
