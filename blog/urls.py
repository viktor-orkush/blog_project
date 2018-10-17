from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^/', views.PostListView.as_view(), name='list_post'),
    url(r'^post/about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name = 'create_post'),
    url(r'^post/update/(?P<pk>\d+)$', views.UpdatePostView.as_view(), name = 'update_post'),
    url(r'^post/delete/(?P<pk>\d+)$', views.DeletePostView.as_view(), name = 'delete_post'),
    url(r'^post/draft/(?P<pc>\d+)$', views.DraftListView.as_view(), name = 'draft_post_list'),
    url(r'^post/(?P<pk>\d+)$', views.DetailPostView.as_view(), name = 'detail_post')
]
