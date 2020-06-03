from django.conf.urls import url

from .views import TopPostView, FilterSearchView

urlpatterns = [
    url(r'^toppost$', TopPostView.as_view(), name='toppost'),
    url(r'^comments$', FilterSearchView.as_view(), name='comments'),
]
