from django.urls import path, include


from .views import (
        SearchProductView
        )

urlpatterns = [
    path(r'^$', SearchProductView.as_view(), name='query'),
]

