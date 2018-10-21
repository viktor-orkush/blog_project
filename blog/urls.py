from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^$', views.AboutView.as_view(), name='about'),
    url(r'^post/draft/$', views.DraftListView.as_view(), name = 'post_draft_list'),
    url(r'^posts$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name = 'post_new'),
    url(r'^post/update/(?P<pk>\d+)$', views.UpdatePostView.as_view(), name = 'post_edit'),
    url(r'^post/delete/(?P<pk>\d+)$', views.DeletePostView.as_view(), name = 'post_remove'),
    url(r'^post/(?P<pk>\d+)$', views.DetailPostView.as_view(), name = 'post_detail'),
    url(r'^post/(?P<pk>\d+)/comment/$', view=views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', view=views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/delete/$', view=views.comment_remove, name='comment_remove' ),
    url(r'^post/publish/(?P<pk>\d+)$', view=views.post_publish, name='post_publish' ),
]
