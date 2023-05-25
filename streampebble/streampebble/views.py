from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import SportStream
from django.shortcuts import redirect
from django.http import HttpResponse  # Add this line
from datetime import datetime

def index(request):
    # Call the update_streams function
    return update_streams(request)



def update_streams(request):
    # Make a request to the website
    url = 'https://crackstreams.biz/watch/38807'
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the sport streams on the page
    streams = soup.find_all('div', class_='listings')

    # Process and update the stream information in the database
    for stream in streams:
        title = stream.find('h3').text.strip()
        category = stream.find('p', class_='cat').text.strip()
        stream_url = stream.find('a')['href']
        description = stream.find('p', class_='desc').text.strip()

        # Check if the stream already exists in the database
        existing_stream = SportStream.objects.filter(title=title).first()

        if existing_stream:
            # Update existing stream
            existing_stream.category = category
            existing_stream.stream_url = stream_url
            existing_stream.description = description
            existing_stream.save()
        else:
            # Create a new stream
            new_stream = SportStream(title=title, category=category, stream_url=stream_url,
                                     description=description)
            new_stream.save()

    return HttpResponse('Stream information updated successfully.')



def video_player(request, video_url):
    if not video_url:
        raise Http404("Invalid video URL")

    context = {'video_url': video_url}

    return render(request, 'streampebble/video.html', context)



def sport_titles(request):
    # Make a request to the website
    url = 'https://crackstreams.biz/watch/38807'
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the sport titles on the page
    sport_titles = []
    stream_titles = soup.find_all('h3', class_='title')
    for title in stream_titles:
        sport_titles.append(title.text.strip())

    # Render a template with the sport titles
    return render(request, 'streampebble/sport_titles.html', {'sport_titles': sport_titles})


from django.shortcuts import render

def nba(request):
    url = "https://crackstreams.biz/nbastreams/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        schedule_elements = soup.find_all('div', class_='media-body')
        schedule = []

        for schedule_element in schedule_elements:
            game_title = schedule_element.find('h4', class_='media-heading').text.strip()
            game_date_time = schedule_element.find('p').text.strip()

            # Check if <a> element exists
            game_link_element = schedule_element.find('a')
            if game_link_element:
                game_link = game_link_element['href']
            else:
                game_link = None

            game_data = {'title': game_title, 'date_time': game_date_time, 'link': game_link}
            schedule.append(game_data)

        context = {'schedule': schedule}

    except AttributeError:
        context = {'schedule': []}

    return render(request, 'streampebble/nba.html', context)


def nfl(request):
    url = "https://crackstreams.biz/nflstreams/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        schedule_elements = soup.find_all('div', class_='media-body')
        schedule = []

        for schedule_element in schedule_elements:
            game_title = schedule_element.find('h4', class_='media-heading').text.strip()
            game_date_time = schedule_element.find('p').text.strip()

            # Check if <a> element exists
            game_link_element = schedule_element.find('a')
            if game_link_element:
                game_link = game_link_element['href']
            else:
                game_link = None

            game_data = {'title': game_title, 'date_time': game_date_time, 'link': game_link}
            schedule.append(game_data)

        context = {'schedule': schedule}

    except AttributeError:
        context = {'schedule': []}

    return render(request, 'streampebble/nfl.html', context)


def nhl(request):
    url = "https://crackstreams.biz/nhlstreams/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        schedule_elements = soup.find_all('div', class_='media-body')
        schedule = []

        for schedule_element in schedule_elements:
            game_title = schedule_element.find('h4', class_='media-heading').text.strip()
            game_date_time = schedule_element.find('p').text.strip()

            # Check if <a> element exists
            game_link_element = schedule_element.find('a')
            if game_link_element:
                game_link = game_link_element['href']
                print(game_link)
            else:
                game_link = None

            game_data = {'title': game_title, 'date_time': game_date_time, 'link': game_link}
            schedule.append(game_data)

        context = {'schedule': schedule}

    except AttributeError:
        context = {'schedule': []}

    return render(request, 'streampebble/nhl.html', context)




def mlb(request):
    url = "https://crackstreams.biz/mlbstreams/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        schedule_elements = soup.find_all('div', class_='media-body')
        schedule = []

        for schedule_element in schedule_elements:
            game_title = schedule_element.find('h4', class_='media-heading').text.strip()
            game_date_time = schedule_element.find('p').text.strip()

            # Extract the <a> element and its 'href' attribute
            game_link_element = schedule_element.find('a')
            game_link = game_link_element['href'] if game_link_element else ''

            # Check if the game is in the past
            current_datetime = datetime.now()
            game_datetime = datetime.strptime(game_date_time, '%Y-%m-%d, %a - %I:%M %p')
            if game_datetime < current_datetime:
                game_status = 'Past'
            else:
                game_status = 'Upcoming'

            game_data = {'title': game_title, 'date_time': game_date_time, 'link': game_link, 'status': game_status}
            schedule.append(game_data)

        context = {'schedule': schedule}

    except AttributeError:
        context = {'schedule': []}

    return render(request, 'streampebble/mlb.html', context)


def mma(request):
    url = "https://crackstreams.biz/mmastreams/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        schedule_elements = soup.find_all('div', class_='media-body')
        schedule = []

        for schedule_element in schedule_elements:
            game_title = schedule_element.find('h4', class_='media-heading').text.strip()
            game_date_time = schedule_element.find('p').text.strip()

            # Check if <a> element exists
            game_link_element = schedule_element.find('a')
            if game_link_element:
                game_link = game_link_element['href']
            else:
                game_link = None

            game_data = {'title': game_title, 'date_time': game_date_time, 'link': game_link}
            schedule.append(game_data)

        context = {'schedule': schedule}

    except AttributeError:
        context = {'schedule': []}

    return render(request, 'streampebble/mma.html', context)


def boxing(request):
    url = "https://crackstreams.biz/boxingstreams/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        schedule_elements = soup.find_all('div', class_='media-body')
        schedule = []

        for schedule_element in schedule_elements:
            game_title = schedule_element.find('h4', class_='media-heading').text.strip()
            game_date_time = schedule_element.find('p').text.strip()

            # Check if <a> element exists
            game_link_element = schedule_element.find('a')
            if game_link_element:
                game_link = game_link_element['href']
            else:
                game_link = None

            game_data = {'title': game_title, 'date_time': game_date_time, 'link': game_link}
            schedule.append(game_data)

        context = {'schedule': schedule}

    except AttributeError:
        context = {'schedule': []}

    return render(request, 'streampebble/boxing.html', context)

def cfb(request):
    url = "https://crackstreams.biz/cfbstreams/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        schedule_elements = soup.find_all('div', class_='media-body')
        schedule = []

        for schedule_element in schedule_elements:
            game_title = schedule_element.find('h4', class_='media-heading').text.strip()
            game_date_time = schedule_element.find('p').text.strip()

            # Check if <a> element exists
            game_link_element = schedule_element.find('a')
            if game_link_element:
                game_link = game_link_element['href']
            else:
                game_link = None

            game_data = {'title': game_title, 'date_time': game_date_time, 'link': game_link}
            schedule.append(game_data)

        context = {'schedule': schedule}

    except AttributeError:
        context = {'schedule': []}

    return render(request, 'streampebble/cfb.html', context)

def ncaab(request):
    url = "https://crackstreams.biz/ncaabstreams/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        schedule_elements = soup.find_all('div', class_='media-body')
        schedule = []

        for schedule_element in schedule_elements:
            game_title = schedule_element.find('h4', class_='media-heading').text.strip()
            game_date_time = schedule_element.find('p').text.strip()

            # Check if <a> element exists
            game_link_element = schedule_element.find('a')
            if game_link_element:
                game_link = game_link_element['href']
            else:
                game_link = None

            game_data = {'title': game_title, 'date_time': game_date_time, 'link': game_link}
            schedule.append(game_data)

        context = {'schedule': schedule}

    except AttributeError:
        context = {'schedule': []}

    return render(request, 'streampebble/ncaab.html', context)

def wwe(request):
    url = "https://crackstreams.biz/wwestreams/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        schedule_elements = soup.find_all('div', class_='media-body')
        schedule = []

        for schedule_element in schedule_elements:
            game_title = schedule_element.find('h4', class_='media-heading').text.strip()
            game_date_time = schedule_element.find('p').text.strip()

            # Check if <a> element exists
            game_link_element = schedule_element.find('a')
            if game_link_element:
                game_link = game_link_element['href']
            else:
                game_link = None

            game_data = {'title': game_title, 'date_time': game_date_time, 'link': game_link}
            schedule.append(game_data)

        context = {'schedule': schedule}

    except AttributeError:
        context = {'schedule': []}

    return render(request, 'streampebble/wwe.html', context)
