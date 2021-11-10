from django.urls import path
from .views.index import index
from .views.contact import contact
from .views.sent_email import sent_email


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('sent-email/', sent_email, name='sent-email')
]
