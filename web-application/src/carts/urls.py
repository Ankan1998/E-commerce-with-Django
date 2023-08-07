from django.urls import path, include


from .views import (
    cart_home,
    cart_update,
    checkout_home,
    checkout_done_view
)

urlpatterns = [
    path(r'^$', cart_home, name='home'),
    path(r'^checkout/$', checkout_home, name='checkout'),
    path(r'^update/$', cart_update, name='update'),
    path(r'^checkout/success$', checkout_done_view, name='success'),

]
