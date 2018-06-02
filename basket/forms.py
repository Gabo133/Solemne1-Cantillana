from django.forms import ModelForm
from basket.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime


from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_PREFIX, identify_hasher,
)
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.forms.utils import flatatt
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.html import format_html, format_html_join
from django.utils.http import urlsafe_base64_encode
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _
class PlayerForm(ModelForm):
    
    class Meta:
        model = Player

        fields = ['rut', 'dv', 'name','birthday', 'nickname', 'age', 'email', 'height', 'weight', 'picture', 'position', 'team']

class CoachForm(ModelForm):
    
    class Meta:
        model = Coach
        fields = ['name', 'age', 'email', 'nickname', 'rut', 'dv','team']


class TeamForm(ModelForm):
    
    class Meta:
        model = Team
        fields = ['name', 'logo', 'description']

class MatchForm(ModelForm):
    
    class Meta:
        model = Match
        fields = ['name', 'date',]
        
class EditPlayer(ModelForm):
    
    def init(self, args, kwargs):
        super(EditPlayer, self).init(args, kwargs)
        self.fields['picture'].required = False

    class Meta:
        model = Player
        fields = ['rut', 'dv', 'name', 'nickname', 'birthday', 'age', 'email', 'height', 'weight', 'picture', 'position', 'team']
        
class EditTeam(ModelForm):
    def init(self, args, kwargs):
        super(EditTeam, self).init(args, kwargs)
        self.fields['logo'].required = False

    class Meta:
        model = Team
        fields = ['name','description','logo','code']
        
class EditCoach(ModelForm):

    class Meta:
        model = Coach
        fields = ['name','age', 'email','nickname','rut','dv']


class MatchForm(ModelForm):
    date = forms.DateTimeField(initial=datetime.datetime.now(), required=False)
    class Meta:
        model = Match
        fields = ['name','date', 'players']
    
class CoachUserForm(ModelForm):

    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','password1', 'password2', )