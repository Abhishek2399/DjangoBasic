from django.urls import path
from . import views

urlpatterns = [
    path('simpleview/', views.simple_view), # URL and the view that will run once URL called
    path('simpleview/', views.simple_view2),
    path('htmlresponse/', views.sample_html_resp_view),
    path('<int:id>/', views.get_post_by_id, name='post_by_id'), # dynamic header syntax
]
