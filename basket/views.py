from django.shortcuts import render
from basket.models import *
from basket.forms import *
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

#este decorador funciona como filtro para ver si el coach puede ingresar a dicha pagina
def decorador(user,coach):
    if(coach):
        try:
            Coach.objects.get(user=user)
            return False
        except Exception as e:
            return True
    else:
        try:
            Coach.objects.get(user=user)
            return True
        except Exception as e:
            return False

@login_required(login_url='/auth/login')
def index(request):
    data = {}

    try:
        
        Coach.objects.get(user=request.user)
        
        coach = Coach.objects.get(user=request.user)
        # SELECT * FROM player
        object_list = Player.objects.filter(team = coach.team).order_by('-id')

        paginator = Paginator(object_list, 10)
        page = request.GET.get('page')

        try:
            data['object_list'] = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            data['object_list'] = paginator.page(1)
        except EmptyPage:
            data['object_list'] = paginator.page(paginator.num_pages)
        data["request"] = request
        template_name = 'player/index_coach.html'
        return render(request, template_name, data)
        
    except Exception as e:
        data["request"] = request
        template_name = 'player/index_superuser.html'
        return render(request, template_name, data)


@login_required(login_url='/auth/login')
def list_player(request):
    #si es false el super admin no podra entrar
    if(decorador(request.user,False)):
        return redirect('index')
    data= {}
    data["request"] = request
    object_list = Player.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)
    template_name = 'player/list_player.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def list_coach(request):
    if(decorador(request.user,False)):
        return redirect('index')
    data = {}
    data["request"] = request

    object_list = Coach.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)
    template_name = 'player/list_coach.html'
    return render(request, template_name, data) 

@login_required(login_url='/auth/login')
def list_team(request):
    if(decorador(request.user,False)):
        return redirect('index')
    data = {}
    data["request"] = request
    object_list = Team.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)
    template_name = 'player/list_team.html'
    return render(request, template_name, data)

def list_match(request):
    
    data = {}
    
    matchs = Match.objects.all()
    # players = matchs.Player_set.all()
    for i in matchs:
        print(i.players.all())

    data["objects_list"] = matchs
    template_name = 'player/list_match.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def add_player(request):
    if(decorador(request.user,False)):
        return redirect('index')
    data = {}

    if request.method == "POST":
        data['form'] = PlayerForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('player_list')

    else:
        data['form'] = PlayerForm()
        data['Tittle'] = "Add Player"
    template_name = 'player/add.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def add_coach(request):
    if(decorador(request.user,False)):
        return redirect('index')
    data = {}
    if request.method == "POST":
        data['form'] = CoachForm(request.POST, request.FILES)
        use = User.objects.all()
        users = User.objects.get(pk = len(use))
        teams = Team.objects.get(pk=request.POST["team"])

        print(users)
        if (data['form'].is_valid()):
            # aca el formulario valido
            us = Coach(name=request.POST["name"],age = request.POST["age"], email=request.POST["email"],
            nickname=request.POST["nickname"],rut=request.POST["rut"], dv=request.POST["dv"])
            us.team = teams
            us.user = users
            us.save()
            return redirect('index')
            
    else:
        data['form'] = CoachForm()

        data['Tittle'] = "Add Coach"
    template_name = 'player/add.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def add_user(request):
    if(decorador(request.user,False)):
        return redirect('index')
    data = {}
    if request.method == "POST":
        data['form'] = CoachUserForm(request.POST, request.FILES)

        if (data['form'].is_valid()):
            # aca el formulario valido
            data['form'].save()
            return redirect('add_user')
    else:
        data['form'] = UserCreationForm()

        data['Tittle'] = "Add Coach"
    template_name = 'player/add.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def add_team(request):
    if(decorador(request.user,True)):
        return redirect('index')
    data = {}
    if request.method == "POST":
        data['form'] = TeamForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('list_team', args=request.POST["username"])

    else:
        data['form'] = TeamForm()
        data['Tittle'] = "Add Team"


    template_name = 'player/add.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def add_match(request):
    if(decorador(request.user,True)):
        return redirect('index')
    data = {}
    if request.method == "POST":
        data['form'] = MatchForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('index')

    else:
        data['form'] = MatchForm()
        data['Tittle'] = "Add Match"
    template_name = 'player/add.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def edit_player(request, player_id):
    if(decorador(request.user,False)):
        return redirect('index')
    data = {}
    if request.POST:
        formPlayer = EditPlayer(request.POST, request.FILES, instance=Player.objects.get(pk=player_id))
        if formPlayer.is_valid():
            formPlayer.save()
            return HttpResponseRedirect(reverse('list_player'))
    template_name = 'player/edit.html'
    data['dat'] = EditPlayer(instance=Player.objects.get(pk=player_id))
    data['Tittle'] = "Edit Player"


    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def edit_team(request, team_id):
    if(decorador(request.user,False)):
        return redirect('index')
    data = {}
    if request.POST:
        formPlayer = EditTeam(request.POST, request.FILES, instance=Team.objects.get(pk=team_id))
        if formPlayer.is_valid():
            formPlayer.save()
            return HttpResponseRedirect(reverse('list_team'))
    template_name = 'player/edit.html'
    data['dat'] = EditTeam(instance=Team.objects.get(pk=team_id))
    data['Tittle'] = "Edit Team"


    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def edit_coach(request, coach_id):
    if(decorador(request.user,False)):
        return redirect('index')
    data = {}
    if request.POST:
        formPlayer = EditCoach(request.POST, request.FILES, instance=Coach.objects.get(pk=coach_id))
        if formPlayer.is_valid():
            formPlayer.save()
            return HttpResponseRedirect(reverse('list_coach'))
    template_name = 'player/edit.html'
    data['dat'] = EditCoach(instance=Coach.objects.get(pk=coach_id))
    data['Tittle'] = "Edit Coach"

    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def Delete(request, id):

    try:
        Coach.objects.get(pk=id).delete()
        return HttpResponseRedirect(reverse('list_coach'))

    except Exception as e:
        try:
            Team.objects.get(pk=id).delete()
            return HttpResponseRedirect(reverse('list_team'))

        except Exception as e:
            Player.objects.get(pk=id).delete()
            return HttpResponseRedirect(reverse('list_player'))
    
    