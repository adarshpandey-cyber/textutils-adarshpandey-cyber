# I have created this file

from django.shortcuts import render
from time import time


def index(request):
    return render(request, 'index.html')


def analyze(request):
    init = time()
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    purpose = "Your analyzed text is:-"

    # Remove Punctuations
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\|,<>./?@#$%^&*_`~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        djtext = analyzed

    # Capitalize
    if fullcaps == "on":
        analyzed = djtext.upper()
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        djtext = analyzed

    # Remove new Lines
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        djtext = analyzed

    # Remove spaces
    if spaceremover == "on":
        analyzed = ""
        for char in djtext:
            if char != " ":
                analyzed += char
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        djtext = analyzed

    # Check for all off
    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and removepunc != "on" and spaceremover != "on":
        analyzed = djtext
        purpose = "All operations are turned off. Your text has not been analyzed"
        params = {'purpose': 'All operations are turned off. Your text has not been analyzed', 'analyzed_text': analyzed}

    time_taken = time() - init
    time_taken = str(time_taken)
    time_taken = time_taken[:6]
    params = {'purpose': purpose, 'analyzed_text': analyzed, "time": time_taken}

    return render(request, 'analyze.html', params)
