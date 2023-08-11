import api.views as apiViews
from rest_framework import routers
from django.urls import path

router = routers.SimpleRouter(trailing_slash=False)

# router.register(r'test', apiViews.TestViewSet, basename='test')

router.register(r'user', apiViews.UserChatViewSet,
    basename='users'
)
urlpatterns = router.urls

# URLconf
urlpatterns = [
    # path(
    #     'register', 
    #     apiViews.ClientAccountRegisterViewSet.as_view(),
    #     name='clients->register'
    # ),

] + router.urls