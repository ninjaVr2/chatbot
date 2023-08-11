from rest_framework import serializers
from chat.models.users.main import UserChatModel

class UserChatReadModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChatModel
        fields = '__all__'