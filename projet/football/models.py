from django.db import models


class Club(models.Model):
    nom = models.CharField(max_length=100)
    fondateur = models.CharField(max_length=100)
    date_creation = models.DateField(blank=True, null=True)
    nombre_titre = models.IntegerField(blank=False)
    classement = models.TextField(null=True, blank=True)

    def __str__(self):
        chaine = f"{self.nom} fondée par {self.fondateur} le {self.date_creation}"
        return chaine
    def dico(self):

        return{"nom" : self.nom, "fondateur":self.fondateur,"date_creation":self.date_creation,"nombre_titre":self.nombre_titre,'classement':self.classement}