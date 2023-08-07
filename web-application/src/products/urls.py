from django.urls import path, include


from .views import (
        ProductListView, 
        ProductDetailSlugView, 
        )

urlpatterns = [
    path(r'^$', ProductListView.as_view(), name='list'),
    path(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]

