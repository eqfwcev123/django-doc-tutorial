from django.urls import path

from .views import index

from polls.views import detail, results, vote

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/detail/', detail, name='detail'),
    path('<int:question_id>/results/', results, name='results'),
    path('<int:question_id>/vote/', vote, name='vote')
]
