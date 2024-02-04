from django.shortcuts import render, redirect
import tweepy
from tweepy.auth import OAuthHandler
from django.conf import settings
import facebook
from django.contrib.auth.decorators import login_required

API_KEY_T= settings.API_KEY_T
API_SECRET_T= settings.API_SECRET_T
ACCESS_KEY= settings.ACCESS_KEY
ACCESS_SECRET = settings.ACCESS_SECRET

GRAPH_TOKEN = settings.GRAPH_TOKEN
API_KEY_F= settings.API_KEY_F
API_SECRET_F= settings.API_SECRET_F

@login_required(login_url = "/profile/login/")
def dashboard(request):
	#Facebook authentication
	try:
		graph = facebook.GraphAPI(access_token=GRAPH_TOKEN, version="2.12")
		
		allposts = graph.get_connections(id='me',connection_name='posts')
		
		mylikes = graph.get_connections(id='me',connection_name='likes')
		

		myfriends = graph.get_connections(id='me', connection_name='friends')
	except:
		return redirect('auth-error')

	#Twitter Authentication
	try:
		auth = tweepy.OAuth1UserHandler(API_KEY_T, API_SECRET_T, ACCESS_KEY, ACCESS_SECRET)
		
		api = tweepy.API(auth)

		user_tweets = api.user_timeline(count=10)
	except:
		return redirect('auth-error')

	context = {
		'user_tweets':user_tweets,
		'allposts':allposts,
		'mylikes':mylikes,
		'myfriends':myfriends,
	}
	return render(request, 'myapp/dashboard.html', context)

@login_required(login_url = "/profile/login/")
def post_comment_fb(request):
	if request.method == "POST":
		post_id = request.POST['post_id']
		comment = request.POST['comment']
		try:
			graph.put_comment(object_id=post_id, message=comment)
		except:
			return redirect("post-err")
	return render(request, 'myapp/facebook-comment.html')

@login_required(login_url = "/profile/login/")
def like_fb_post(request):
	if request.method == "POST":
		post_id = request.POST['post_id']
		try:
			graph.put_like(object_id=post_id)
		except:
			return redirect("post-err")
	return render(request, 'myapp/facebook-like.html')

@login_required(login_url = "/profile/login/")
def post_tweet(request):
	if request.method == "POST":
		try:
			auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_KEY, ACCESS_SECRET)
			api = tweepy.API(auth)
		except:
			return redirect("post-tweet")
		tweet = request.POST['comment']
		try:
			api.update_status(tweet)
		except:
			return redirect('post-err')
	return render(request, 'myapp/tweet.html')

@login_required(login_url = "/profile/login/")
def social(request):
	return render(request, 'myapp/social.html')

@login_required(login_url = "/profile/login/")
def auth_error(request):
	return render(request, 'myapp/auth-error.html')

@login_required(login_url = "/profile/login/")
def publish_f(request):
	return render(request, 'myapp/fail.html')

@login_required(login_url = "/profile/login/")
def success_p(request):
	return render(request, 'myapp/success.html')