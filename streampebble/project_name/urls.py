"""project_name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from streampebble.views import sport_titles, index, nba, nfl, nhl, mlb, mma, boxing, cfb, ncaab, wwe, video_player, upcoming_games, past_games

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('sport_titles/', sport_titles, name='sport_titles'),
    path('nba/', nba, name='nba'),
    path('nfl/', nfl, name='nfl'),
    path('nhl/', nhl, name='nhl'),
    path('mlb/', mlb, name='mlb'),
    path('mma/', mma, name='mma'),
    path('boxing/', boxing, name='boxing'),
    path('cfb/', cfb, name='cfb'),
    path('ncaab/', ncaab, name='ncaab'),
    path('wwe/', wwe, name='wwe'),
    path('video/<str:video_url>/', video_player, name='video_player'),
    path('upcoming-games/', upcoming_games, name='upcoming_games'),
    path('past-games/', past_games, name='past_games'),

]

