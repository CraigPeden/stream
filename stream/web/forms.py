from django.contrib.auth.models import User
from django import forms
from web.models import Stream

class StreamForm(forms.ModelForm):
	games = [('Starcraft 2: Heart of the Swarm','Starcraft 2: Heart of the Swarm'),('League of Legends','League of Legends'),('DOTA2','DOTA2'),('Counter Strike: Global Offensive','Counter Strike: Global Offensive')]
	
	stream_game = forms.ChoiceField(choices=games)
	
	class Meta:
		model = Stream
		exclude = ['user',]
