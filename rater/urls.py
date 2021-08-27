# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import include
# from raterapi.views import register_user, login_user

# urlpatterns = [
#     # Requests to http://localhost:8000/register will be routed to the register_user function
#     path('register', register_user),
#     # Requests to http://localhost:8000/login will be routed to the login_user function
#     path('login', login_user),
#     path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from raterapi.views import register_user, login_user
from raterapi.views import GameView, CategoryView, ReviewView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GameView, 'game')
router.register(r'categories', CategoryView, 'category')
router.register(r'reviews', ReviewView, 'review')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls)
]
