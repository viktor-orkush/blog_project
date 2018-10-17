from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^/', views.PostListView.as_view(), name='list_post'),
    url(r'^post/about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name = 'create_post'),
    url(r'^post/update/(?P<pk>\d+)$', views.UpdatePostView.as_view(), name = 'update_post'),
    url(r'^post/delete/(?P<pk>\d+)$', views.DeletePostView.as_view(), name = 'delete_post'),
    url(r'^draft/(?P<pc>\d+)$', views.DraftListView.as_view(), name = 'draft_post_list'),
    url(r'^post/(?P<pk>\d+)$', views.DetailPostView.as_view(), name = 'detail_post'),
    url(r'^post/(?P<pk>/d+)/comment/$', view=views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>/d+)/approve/$', view=views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>/d+)/delete/$', view=views.comment_remove, name='comment_remove' ),
    url(r'^post/(?P<pk>/d+)/publish/$', view=views.post_publish, name='post_publish' ),
]
