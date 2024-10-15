from rest_framework import serializers

from .models import Note


class NotesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id',
            'user_id',
            'text',
            'is_synced_with_cloud',
        )