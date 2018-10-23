import jwt, json
import checkbonds_backend.settings as settings

from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from usermanagement.models import User


# class LoginView(views.APIView):
#
#     permission_classes = (AllowAny,)
#
#     def post(self, request, *args, **kwargs):
#         if not request.data:
#             return Response({'Error': "Please provide username/password"}, status="400")
#
#         username = request.data['username']
#         password = request.data['password']
#         try:
#             user = User.objects.get(username=username, is_active=True)
#             if not user.check_password(password):
#                 return Response({'Error': "Invalid username/password"}, status="400")
#         except User.DoesNotExist:
#             return Response({'Error': "Invalid username/password"}, status="400")
#
#         if user:
#             user.update_user_secret_key()
#             payload = {
#                 'id': user.id,
#                 'email': user.email,
#             }
#
#             token = jwt.encode(payload, str(user.jwt_secret_key)).decode('utf-8')
#             jwt_token = {'token': token + settings.JWT_USER_ID_SEPARATER + str(user.id + settings.USER_ID_FAKE_NUM)}
#             return Response(
#                 jwt_token,
#                 status=200,
#                 content_type="application/json"
#             )
#         else:
#             return Response(
#                 {'Error': "Invalid credentials"},
#                 status=400,
#                 content_type="application/json"
#             )


class LogoutView(views.APIView):
    """
    Use this endpoint to log out all sessions for a given user.
    """

    def post(self, request, *args, **kwargs):
        user = request.user
        return Response({'success': True}, status=200)
