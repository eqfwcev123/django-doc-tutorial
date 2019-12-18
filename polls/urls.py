from django.urls import path

from polls.views import vote, DetailView, ResultsView
from polls.views import IndexView

app_name = 'polls'  # This is the application namespace
# as_view() : Returns a callable view that takes a request and returns a response
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/detail/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:pk>/vote/', vote, name='vote'),
]
