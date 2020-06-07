from django.db import models

# Create your models here.


class Team(models.Model):
        name=models.CharField(max_length=200)
        nb_match=models.IntegerField()
        totale_points=models.IntegerField()
        nb_victoir=models.IntegerField()
        nb_defait=models.IntegerField()
        nb_match_null=models.IntegerField()
        but_marque=models.IntegerField()
        but_concede=models.IntegerField()
        
        def __str__(self):
        
            return self.name
    

class GroupOfTeams(models.Model):
    
    name=models.CharField(max_length=200)
    teams=models.ForeignKey(Team,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

    