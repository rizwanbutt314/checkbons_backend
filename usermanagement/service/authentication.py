from rest_framework_jwt.authentication import JSONWebTokenAuthentication, BaseAuthentication
import jwt
from checkbonds_backend.settings import JWT_USER_ID_SEPARATER, USER_ID_FAKE_NUM
from usermanagement.models import User
from rest_framework import exceptions
from django.utils.translation import ugettext as _

AUTH_TOKEN_HEADER = 'HTTP_AUTHORIZATION'
AUTH_TOKEN_PREFIX = 'Token '

class JWTAuthentication(JSONWebTokenAuthentication):

    def authenticate(self, request):
        auth = request.META.get(AUTH_TOKEN_HEADER)
        if not auth or not auth.startswith(AUTH_TOKEN_PREFIX):
            return None

        try:
            token = auth.split(AUTH_TOKEN_PREFIX)[1]
        except:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)
        return self.authenticate_credentials(token)

    def authenticate_credentials(self, payload):

        token = payload.split(JWT_USER_ID_SEPARATER)[0]
        user_id = (int(payload.split(JWT_USER_ID_SEPARATER)[1]) - USER_ID_FAKE_NUM)
        msg = _('Invalid token')

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed(msg)


        try:
            decoded_dict = jwt.decode(token, str(user.jwt_secret_key))
        except:
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)

    def authenticate_header(self, request):
        return 'Token'
