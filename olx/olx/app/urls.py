from django.urls import path
from .views import (
    MainPageView, UserLoginView, RegisterView, UserLogoutView,
    AdListView, AdDetailView, AdCreateView, AdListByUserView, AdsByCategoryView
)
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('reg/', RegisterView.as_view(), name='reg'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('category/<int:category_id>/', AdsByCategoryView.as_view(), name='ads_by_category'),
    path('ads/', AdListView.as_view(), name='ad_list'),
    path('ads/new/', AdCreateView.as_view(), name='ad_create'),
    path('ads/<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('ads/user/<int:user_id>/', AdListByUserView.as_view(), name='ads_by_user'),
    path('ads/<int:pk>/delete/', views.ad_delete, name='ad_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
