from django.urls import path
from .views import home, tutorials, techtrends, videogames, postDetail

urlpatterns = [
    path('', home, name='index'),
    path('tutorials/', tutorials, name='tutorials'),
    path('techtrends/', techtrends , name='techtrends'),
    path('videogames/', videogames , name='videogames'),
    path('<slug:slug>/', postDetail, name='postDetail'),
]