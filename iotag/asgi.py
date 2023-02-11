"""
ASGI config for iotag project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iotag.settings')

from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from iotag.middlewaretokenauth import CustomUserAuthMiddleware
from django.urls import path
from iotapp.consumer import DashConsumer
websocket_urlPattern=[
    path('dashboard',DashConsumer.as_asgi()),
]
application=ProtocolTypeRouter({
    # 'http':
    'websocket':CustomUserAuthMiddleware(AuthMiddlewareStack(URLRouter(websocket_urlPattern)))

})