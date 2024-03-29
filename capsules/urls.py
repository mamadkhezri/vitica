from django.urls import path
from . import views


app_name ='capsules'

urlpatterns = [
    path('capsule/create', views.PostcreateView.as_view(), name='capsules_create'),
    path('capsule/<int:cap_id>/<slug:cap_slug>/', views.PostDetailView.as_view(), name='capsules_detail'),
    path('like/<int:timecapsule_id>/', views.LikePostView.as_view(), name='post_like'),
    path('unlike/<int:timecapsule_id>/', views.UnlikePostView.as_view(), name='post_unlike'),

]