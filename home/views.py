from django.shortcuts import render,redirect
from bokeh.plotting import figure
from bokeh.embed import components
from django.forms import ModelForm
from .models import Team,GroupOfTeams
from django.contrib.auth.decorators import login_required


class TeamForm(ModelForm):
    class Meta:
        model=Team
        fields=[
            'name',
            'nb_match',
            'totale_points',
            'nb_victoir',
            'nb_defait',
            'nb_match_null',
            'but_marque',
            'but_concede'
            ]

class GroupOfTeamsForm(ModelForm):
    class Meta:
        model=GroupOfTeams
        fields=['name','teams']
        # fields=['name','teams','date']




@login_required(login_url='/accounts/Login/')
def Create_Team_Handler(request):
    if request.method=="GET":
        form=TeamForm()
        for _ in form.fields:
            form.fields[_].widget.attrs={'maxlength': '200',"class":"form-control"}
        context={"form":form}
        return render(request,'home/team.djt',context=context)
    elif request.method=="POST":
        form=TeamForm(request.POST)
        if form.is_valid():
            form.save()
            print('form saved and valid')
            return redirect('home')
        else: 
           return redirect('create-team')


@login_required(login_url='/accounts/Login/')
def Create_Group_Handler(request):
    if request.method=="GET":
        form=GroupOfTeamsForm()
        for _ in form.fields:
            form.fields[_].widget.attrs={'maxlength': '200',"class":"form-control"}
        context={"form":form}
        return render(request,'home/group.djt',context=context)
    elif request.method=="POST":
        form=GroupOfTeamsForm(request.POST)
        if form.is_valid():
            form.save()
            print('form saved and valid')
            return redirect('home')
        else: 
           return redirect('create-group')


def Index_Handler(request):
    if request.user.is_active:
        return redirect('home')
    else:
        return render(request,'home/index.djt')



@login_required(login_url='/accounts/Login/')
def Home_Hnadler(request):
    groups=GroupOfTeams.objects.all()
    teams=Team.objects.all()
    def count(obj):
        x= obj
        print("")
    pouels = ['A', 'B', 'C', 'D', 'E', 'F','G','H']
    counts=[
        GroupOfTeams.objects.filter(name="A").count() if  Exception  else 0, 
        GroupOfTeams.objects.filter(name="B").count() if  Exception  else 0,
        GroupOfTeams.objects.filter(name="C").count() if  Exception  else 0,
        GroupOfTeams.objects.filter(name="D").count() if  Exception  else 0,
        GroupOfTeams.objects.filter(name="E").count() if  Exception  else 0,
        GroupOfTeams.objects.filter(name="F").count() if  Exception  else 0,
        GroupOfTeams.objects.filter(name="G").count() if  Exception  else 0,
        GroupOfTeams.objects.filter(name="H").count() if  Exception  else 0
        ]
    p = figure(x_range=pouels, plot_height=250, title="Groups",toolbar_location=None, tools="")
    p.vbar(x=pouels, top=counts, width=0.9)
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.plot_width = 800
    script,div=components(p)
    disk = psutil.disk_usage('/')
    print(disk.total / (1024.0 ** 3))
    context={
        "groups":groups,
        "teams":len(teams),
        "group_teams":len(groups),
        "tournaments":0,
        "script":script,
        "div":div
    }

    return render(request,'home/home.djt',context=context)

def More_Handler(request,id):
    if request.method=="GET":
        group=GroupOfTeams.objects.get(pk=id)
        team=Team.objects.get(name=group.teams)
        context={
        "group":group,
        "team":team
        }
        return render(request,'home/more.djt',context=context)
    elif request.method=="POST":
        group=GroupOfTeams.objects.get(pk=id)           
        team=Team.objects.get(name=group.teams)
        group.delete()
        team.delete()

        return redirect('home')