from django.conf.urls import url
from families import views as families_views

urlpatterns = [
    url(
        r'^$',
        families_views.index,
        name='families_index'),
    url(
        r'^(?P<family_id>[0-9]+)/$',
        families_views.family_detail,
        name='families_family_detail'),
]
