from django.urls import path
from . import views
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('lessons/', views.LessonList.as_view(), name='lesson-list'),
    path('userlessons/', views.UserLessonList.as_view(), name='user-lesson-list'),
    path('register/', RegisterView.as_view(), name='register'), 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]