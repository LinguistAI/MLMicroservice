
from django.contrib import admin
from django.urls import include, path
from chat.views.create_conversation import create_conversation

from chat.views.generate_chat_response import generate_chat_response
from chat.views.get_conversation_messages import get_last_conversation_messages
from chat.views.get_all_conversation_messages import get_all_conversation_messages
from chat.views.get_user_conversations import get_user_conversations
from chat.views.bots.get_all_bots import get_all_bots
from chat.views.get_message_count_aggregate import get_message_count_aggregate
from chat.views.get_message_count_by_bot import get_message_count_by_bot

urlpatterns = [
    path('chat/send/<str:conversation_id>', generate_chat_response),
    path('chat/all/<str:conversation_id>', get_all_conversation_messages),
    path('chat/latest/<str:conversation_id>', get_last_conversation_messages),
    path('chat/count', get_message_count_by_bot, name="get_message_count_by_bot"),
    path('chat/count/aggregate', get_message_count_aggregate, name="get_message_count_aggregate"),
    path("create", create_conversation, name="create_conversation"),
    path("user", get_user_conversations, name="get_user_conversations"),
    path("bots", get_all_bots),
]
