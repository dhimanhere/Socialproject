from django.urls import path
from myapp import views

urlpatterns = [
	path("", views.dashboard, name = "dashboard"),
	path("facebook/comment/", views.post_comment_fb, name="facebook-comment"),
	path("facebook/like/", views.like_fb_post, name = "facebook-like"),
	path("twitter/tweet/", views.post_tweet, name = "post-tweet"),
	path("authentication-error/", views.auth_error, name = "auth-error"),
	path("failed/", views.publish_f, name = "post-err"),
	path("success/", views.success_p, name = "post-succ"),
	path("social/", views.social, name = "social"),
]