from django.urls import path, include
from . import views

app_name = 'comments'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('comment/<int:comment_id>/', views.edit_comment, name="edit_comment"),
]