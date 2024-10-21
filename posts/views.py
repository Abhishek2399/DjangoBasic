from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint
import json

# keeping sample data ready for temp purpose will be replaced with actual data once database ready
sample_posts = json.loads(open(fr"posts\sample_data.json", "r").read())

# Create your views here.

def simple_view(requests):
    #pprint(requests.__dict__)
    return HttpResponse("Simple view - 1")


# Sample view to check if same route used which view will be called first
def simple_view2(requests):
    #pprint(requests.__dict__)
    return HttpResponse("Simple view - 2")


# sample view to understand how to send HTML response
def sample_html_resp_view(requests):
    html = ""
    for post in sample_posts[:5]:
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
    if id > 0:
        post = [post for post in sample_posts if post.get('id') == id][0]
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
        return "Pass a valid 'id'"
