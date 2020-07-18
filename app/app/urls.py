"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from rest_framework.authtoken import views
from app.views import  DatabaesAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from drf_yasg.utils import swagger_auto_schema

class CustomAuthToken(ObtainAuthToken):

    test_param = openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_STRING)

    @swagger_auto_schema(
        operation_description="partial_update description override",
        manual_parameters=[test_param],
        request_body=openapi.Schema(
          type=openapi.TYPE_OBJECT, 
          properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
          }),
        responses={
            '200': "Ok",
            '400': "Bad Request"
        })
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        t = Token.objects.filter(user=user)
        new_key = t[0].generate_key()
        t.update(key=new_key) 



        return Response({
            'token': new_key,
            'user_id': user.pk,
            'email': user.email
        })

api_info = openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   )

schema_view = get_schema_view(
   api_info,
   public=True,
   permission_classes=(permissions.AllowAny,),
)

#router = DefaultRouter()
#router.register('databases', DatabaesAPIView, basename='api/database')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^api-token-auth/', CustomAuthToken.as_view()),
    url(r'^api/databases/', DatabaesAPIView.as_view()),
    url(r'^api/databases/<int:id>/', DatabaesAPIView.as_view()),
    #url(r'^api-token-auth/', views.obtain_auth_token) 
]

