from django.conf.urls import include, url
from post.views import LocationList, CategoryList, CreatePost

urlpatterns = [
    url(r'^locations/', LocationList.as_view(), name='location_list'),
    url(r'^category/',CategoryList.as_view(), name='category_list'),
    url(r'^create/$', CreatePost.as_view(), name='posting'),

]
