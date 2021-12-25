from django.urls import path
from .views import ArticleListView, Blogcreateview,Deatilview,Editblog,Deleteblog




urlpatterns = [

    path('home', ArticleListView.as_view(), name='/home'),
    path('post', Blogcreateview.as_view(),name='post_new'),
    path('post/<int:pk>/', Deatilview.as_view(),name='detail'),
    path('post/<slug:pk>/edit/', Editblog.as_view(),name='edit_blog'),
    path('post/<slug:pk>/delete/', Deleteblog.as_view(),name='delete_blog'),

]

