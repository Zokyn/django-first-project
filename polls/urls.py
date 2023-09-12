from django.urls import path

from . import views 

# verificar sempre se há um contrabarra no final do URL
app_name = "polls"
urlpatterns = [ 
    path("", views.IndexView.as_view(), name='index'),
    path("<int:pk>/", views.DetailView.as_view(), name='detail'),
    path("<int:pk>/results/", views.ResultsView.as_view(), name='results'),
    path("<int:question_id>/vote/", views.vote, name='vote')
]

