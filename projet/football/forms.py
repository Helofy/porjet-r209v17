from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models



class ClubForm(ModelForm):
    class Meta:

        model = models.Club
        fields = ('nom', 'fondateur', 'date_creation', 'nombre_titre','classement')
        labels = {
                'nom' : _('Nom'),
                'fondateur' : _('Fondateur') ,
                'date_creation' : _('date de creation'),
                'nombre_titre' : _('nombres de titre'),
                'classement' : _('Classement')
        }
