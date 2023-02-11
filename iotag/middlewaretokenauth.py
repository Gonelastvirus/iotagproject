import urllib.parse
from django.contrib.auth import get_user_model
import urllib.parse
from channels.db import database_sync_to_async
@database_sync_to_async
def get_user(token):
    User = get_user_model()
    try:
        return User.objects.get(token=token)
    except User.DoesNotExist:
        return None

class CustomUserAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope,receive,send):
        # Get the token from the query string
        token = urllib.parse.parse_qs(scope["query_string"])[b'token'][0].decode('utf-8')
        # Get the user using the token
        user = await get_user(token)
        print(user.is_superuser)
        if user is None:
            # If no user was found, return a 401 Unauthorized response
            return {
                "close": True,
                "headers": [
                    (b"status", b"401 Unauthorized"),
                ],
            }
        else:

        # If a user was found, set the user on the scope so that it can be accessed
        # by the inner application
            scope["user"] = user
        

        return await self.inner(scope,receive,send)
