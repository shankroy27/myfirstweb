#I have created this file -Shank
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    print(extraspaceremover)
    charcount = request.POST.get('charcount','off')
    analyzed = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params = {'purpose':'Remove Punctuaions' , 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif fullcaps =="on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalize the stirng', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover =="on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif extraspaceremover =="on":
        analyzed = ""
        for char in djtext:
            if char !=" ":
                analyzed = analyzed + char
        params = {'purpose': 'Remove extra space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif charcount =="on":
        params = {'purpose': 'count char', 'analyzed_text': len(djtext)}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")
# def removepunc(request):
#     print(request.GET.get('text','default'))
#     return HttpResponse('Remove')
#
# def capfirst(request):
#     return HttpResponse('Capitalize First')
#
# def newlineremove(request):
#     return HttpResponse('newlineremove')
#
# def spaceremove(request):
#     return HttpResponse('spaceremove')
#
# def charcount(request):
#     return HttpResponse('charcount')