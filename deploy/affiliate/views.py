from django.shortcuts import render


def about_us(request):
    return render(request, 'about/about_us.html')

def why_us(request):
    return render(request, 'whyus/why_us.html')

def team(request):
    return render(request, 'team/team.html')