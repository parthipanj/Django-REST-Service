from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'snippets'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('exploration', views.ExplorationViewSet.as_view(), name='workaround')
]
