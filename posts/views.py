from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from pprint import pprint
import json

# keeping sample data ready for temp purpose will be replaced with actual data once database ready
SAMPLE_POSTS = json.loads(open(fr"posts\sample_data.json", "r").read())
# SAMPLE_POSTS = []

# Create your views here.

def simple_view(requests):
    #pprint(requests.__dict__)
    return render(requests, fr"posts/home.html", {"project_name" : 'Django Basics', 'posts' : SAMPLE_POSTS})


# Sample view to check if same route used which view will be called first
def simple_view2(requests):
    #pprint(requests.__dict__)
    return HttpResponse("Simple view - 2")


# sample view to understand how to send HTML response
def sample_html_resp_view(requests):
    html = ""
    for post in SAMPLE_POSTS[:5]:
        html += f"""
        <div>
            <span>
            <a href="/posts/{post.get('id')}">
                <h2> {post.get('id')}.) {post.get('title')} </h2>
            </a>
            </span>
            <h4> {post.get('content')} </h4>
        </div>
        """
    return HttpResponse(html)

def get_post_by_id(requests, id:int=-1):
    print(f"Requested id -> {id}")
    total_posts = len(SAMPLE_POSTS)
    if id > 0 and id < total_posts:
        post = [post for post in SAMPLE_POSTS if post.get('id') == id][0]
        html = f"""
        <div>
            <span>
            <h2> {post.get('id')}.) {post.get('title')} </h2>
            </span>
            <h4> {post.get('content')} </h4>
        </div>
        """
        return HttpResponse(html)
    else:
        return HttpResponseNotFound("Post not available 🥲")

def google_view(requests, id:int=-1):
    print(f"Redirected to -> {reverse('post_by_id', args=[id])}")
    redirect_url = reverse('post_by_id', args=[id])
    return HttpResponseRedirect(redirect_to=redirect_url)
