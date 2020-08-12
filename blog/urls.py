from django.urls import path
from .views import (
    SessionListView,
    SessionDetailView,
    SessionCreateView,
    UidSessionListView,
    QidSessionListView,
    CidSessionListView,
    DateSessionListView,
    AidSessionListView,
)
from . import views

urlpatterns = [
    path('', SessionListView.as_view(), name='blog-home'),
    path('uid/<str:uid>', UidSessionListView.as_view(), name='uid-sessions'),
    path('qid/<str:qid>', QidSessionListView.as_view(), name='qid-sessions'),
    path('cid/<str:cid>', CidSessionListView.as_view(), name='cid-sessions'),
    path('aid/<str:aid>', AidSessionListView.as_view(), name='aid-sessions'),
    path('date/<str:session_date>', DateSessionListView.as_view(), name='date-sessions'),
    path('session/<int:pk>/', SessionDetailView.as_view(), name='session-detail'),  # <pk> = model's id number
    path('session/new/', SessionCreateView.as_view(), name='session-create'),
    path('session/submit', views.form_submit, name='session-submit'),
    path('about/', views.about, name='blog-about'),
    path('other/', views.other, name='blog-other'),
]
