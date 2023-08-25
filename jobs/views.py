from django.shortcuts import render
from django.http import JsonResponse
import feedparser
import os
import re
from .models import Job
from django.core import serializers



def fetch_jobs(request):
    rss_url = 'https://www.rotanacareers.com/rss/all/'
    feed = feedparser.parse(rss_url)

    for item in feed.entries:
        title = item.title
        country = item.country
        pattern = r'Job Location:</b></td>\n<td width=\"75%\">(.*?)</td>'
        location = re.search(pattern, item['summary_detail']['value']).group(1) 

        job = Job(title=title, location=location, country=country)
        job.save()

    return JsonResponse({'message': 'Jobs fetched successfully'})


def table_view(request):
    jobs = Job.objects.all()
    return render(request, 'table.html', {'jobs': jobs})

def map_view(request):
    jobs = Job.objects.all()
    jobs = serializers.serialize('json', jobs)
    api_key =  os.getenv("GOOGLE_MAPS_API_KEY")
    return render(request, 'map.html', {'jobs': jobs, 'api_key': api_key})
