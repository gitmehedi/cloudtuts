from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from restapi.views import RestaurantView,UserView,LogoutView

urlpatterns = [
    path('api/restaurants/', RestaurantView.as_view()),
    path('api/restaurants/<int:pk>/', RestaurantView.as_view()),
    path('register/', UserView.as_view()),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view()),
]
