from django.urls import path

from . import views

# One can take advantage of 'app_name' to set the application namespace
#   (since a project can contain ten or even more apps in it):
app_name = "polls"

urlpatterns = [
  # ex: /polls/
  path("", views.index, name="index"),
  # ex: /polls/5/
  path("<int:question_id>/", views.detail, name="detail"),
  # ex: /polls/5/results/
  path("<int:question_id>/results/", views.results, name="results"),
  # ex: /polls/5/vote/
  path("<int:question_id>/vote/", views.vote, name="vote"),
]
