from django.urls import path

from . import api


urlpatterns = [
    path('', api.note_list_create_view),
    path('<uuid:pk>/update/', api.note_update_view),
    path('<uuid:pk>/delete/', api.note_destroy_view),
    path('<uuid:pk>/', api.note_detail_view),

    #
    path('pinned/', api.note_pinned_view),


]