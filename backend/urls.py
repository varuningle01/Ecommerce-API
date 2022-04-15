"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# from api.views import RegistrationAPIView
# from api.views import LogoutAPIView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api/user/', include('account.urls')),
    path('api/user-wishlist/', include('wishlist.urls')),
    path('api/user-cart/', include('cart.urls')),
    path('api/user-details/', include('details.urls')),



    #  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('auth/register/', RegistrationAPIView.as_view(), name='register'),
    # path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    # path('auth/logout/', LogoutAPIView.as_view(), name='logout'),
    # path('auth/refresh-token', TokenRefreshView.as_view(), name='refreshtoken'),
]
