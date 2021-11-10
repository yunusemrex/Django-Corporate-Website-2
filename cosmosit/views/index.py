from django.shortcuts import render, redirect
from cosmosit.models import detail
from cosmosit.models.hero import Hero
from cosmosit.models.about import About
from cosmosit.models.detail import Detail
from cosmosit.models.features import Features
from cosmosit.models.services_headers import ServiceHeaders
from cosmosit.models.call_action import CallAction
from cosmosit.models.team import TeamMembers
from cosmosit.models.testimionals import Testimionals



def index(request):
    hero1 = Hero.objects.all()
    about = About.objects.get(header='About')
    details_a = Detail.objects.all()[0:6] # ilk 6 about details
    details_f = Detail.objects.all()[6:13] # 6-12 arası features details
    details_s = Detail.objects.all()[13:19] # 12-19 arası service details
    features = Features.objects.get(content='Features')
    counts = Features.objects.get(content='Counts')
    services = ServiceHeaders.objects.all()
    call_action = CallAction.objects.all()
    testimionals = Testimionals.objects.all()
    team1 =  TeamMembers.objects.get(id=1)
    team2 =  TeamMembers.objects.get(id=2)
    team3 =  TeamMembers.objects.get(id=3)
    team4 =  TeamMembers.objects.get(id=4)


    return render(request, 'sections/index.html', context={
        'hero1': hero1,
        'about': about,
        'features': features,
        'services': services,
        'call_action':call_action, 
        'details_a' :details_a,
        'details_f': details_f,
        'details_s': details_s,
        'testimionals': testimionals,
        'counts': counts,
        'team1': team1,
        'team2': team2,
        'team3': team3,
        'team4': team4,
        # 'team5': team5,
        # 'team6': team6,
        # 'team7': team7,
        # 'team8': team8,


    })

