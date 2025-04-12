from django.urls import path
from . import views

# If using class-based views
urlpatterns = [
    # Media Outlet URLs
    path('', views.MediaOutletListView.as_view(), name='home'),
    path('outlets/', views.MediaOutletListView.as_view(), name='media_outlet_list'),
    path('outlets/add/', views.MediaOutletCreateView.as_view(), name='media_outlet_create'),
    path('outlets/<int:pk>/', views.MediaOutletDetailView.as_view(), name='media_outlet_detail'),
    path('outlets/<int:pk>/edit/', views.MediaOutletUpdateView.as_view(), name='media_outlet_update'),
    path('outlets/<int:pk>/delete/', views.MediaOutletDeleteView.as_view(), name='media_outlet_delete'),

    # Article URLs
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('articles/add/', views.ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
]

# # If using function-based views
# """
# urlpatterns = [
#     # Media Outlet URLs
#     path('outlets/', views.media_outlet_list, name='media_outlet_list'),
#     path('outlets/add/', views.media_outlet_create, name='media_outlet_create'),
#     path('outlets/<int:pk>/', views.media_outlet_detail, name='media_outlet_detail'),
#     path('outlets/<int:pk>/edit/', views.media_outlet_update, name='media_outlet_update'),
#     path('outlets/<int:pk>/delete/', views.media_outlet_delete, name='media_outlet_delete'),
#
#     # Article URLs
#     path('articles/', views.article_list, name='article_list'),
#     path('articles/add/', views.article_create, name='article_create'),
#     path('articles/<int:pk>/', views.article_detail, name='article_detail'),
#     path('articles/<int:pk>/edit/', views.article_update, name='article_update'),
#     path('articles/<int:pk>/delete/', views.article_delete, name='article_delete'),
# ]
# """