from django.shortcuts import render


def cabin(request):
    return render(request, 'cabin/cabin.html')
