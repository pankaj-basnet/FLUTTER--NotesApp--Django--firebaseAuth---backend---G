# from django.http import JsonResponse

# from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import NotesListSerializer
from .models import Note
#sn= ----------------------
from rest_framework.generics import ListAPIView
import requests

# requests.get(url, params, *args, **kwargs)

import json

from rest_framework.views import APIView       # isn=
from rest_framework import generics, mixins

#sn= ----------------------


from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

# from .models import Note
# from .serializers import NoteSerializer

class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    
    serializer_class = NotesListSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        user_id = serializer.validated_data.get('user_id')
        text = serializer.validated_data.get('text') or None
        is_synced_with_cloud = serializer.validated_data.get('is_synced_with_cloud')
        if text is None:
            text = user_id
        serializer.save(text=text)
        # send a Django signal

    def get_queryset(self):

        # queryset = Note.objects.all()[:4] # five notes on top in django database
        queryset = Note.objects.all().filter().order_by('updated_at' )
        return queryset

note_list_create_view = NoteListCreateAPIView.as_view()


######################################################

class NoteDetailAPIView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NotesListSerializer


note_detail_view = NoteDetailAPIView.as_view()



######################################################

class NoteUpdateAPIView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NotesListSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.text:
            instance.text = instance.user_id
            ## 

note_update_view = NoteUpdateAPIView.as_view()



class NoteDestroyAPIView(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NotesListSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

note_destroy_view = NoteDestroyAPIView.as_view()


##############################################################


class NotePinnedAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    
    serializer_class = NotesListSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        user_id = serializer.validated_data.get('user_id')
        text = serializer.validated_data.get('text') or None
        is_synced_with_cloud = serializer.validated_data.get('is_synced_with_cloud')
        if text is None:
            text = user_id
        serializer.save(text=text)
        # send a Django signal

    def get_queryset(self):

        # queryset = Note.objects.all()[4:] #didnot work
        # queryset = Note.objects.all() # five notes on top in django database
        queryset = Note.objects.filter(text__icontains = 'pin')

        return queryset

note_pinned_view = NotePinnedAPIView.as_view()
