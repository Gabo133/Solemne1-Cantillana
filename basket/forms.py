from django.forms import ModelForm
from basket.models import *


class PlayerForm(ModelForm):
    
    class Meta:
        model = Player
        fields = ['rut', 'dv', 'name', 'nickname', 'birthday', 'age', 'email', 'height', 'weight', 'picture', 'position', 'team']

class CoachForm(ModelForm):
    
    class Meta:
        model = Coach
        fields = ['name', 'age', 'email', 'nickname', 'rut', 'dv']
        
class TeamForm(ModelForm):
    
    class Meta:
        model = Team
        fields = ['name', 'logo', 'description']
        
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