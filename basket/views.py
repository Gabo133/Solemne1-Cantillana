from django.shortcuts import render
from basket.models import Player
from basket.forms import PlayerForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/login')
def index(request):
    data = {}

    # SELECT * FROM player
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


def add(request):
    data = {}
    if request.method == "POST":
        data['form'] = PlayerForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('player_list')

    else:
        data['form'] = PlayerForm()

    template_name = 'player/add_player.html'
    return render(request, template_name, data)


def detail(request, player_id):

    data = {}
    template_name = 'player/detail_player.html'

    # SELECT * FROM player WHERE id = player_id
    data['player'] = Player.objects.get(pk=player_id)
    # import pdb;pdb.set_trace()

    return render(request, template_name, data)


