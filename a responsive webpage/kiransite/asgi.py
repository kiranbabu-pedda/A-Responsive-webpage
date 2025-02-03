import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from kiransapp import consumers  # Import the chat consumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kiranproject.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handles HTTP requests
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/chat/', consumers.ChatConsumer.as_asgi()),  # WebSocket route
        ])
    ),
})
