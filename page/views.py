from django.shortcuts import render
from django.shortcuts import redirect
from django.views import generic

from story.forms import StoryForm,ChapterForm
from story.models import Chapters,Storys
from account.models import account


def Home(request, pk=-1):

    storys = Storys.objects.all()

    try:

        if pk == -1:
            StoryTitel = Storys.objects.all().first()
        else:
            StoryTitel = Storys.objects.get(pk=pk)

        summery = Chapters.objects.filter(ForStory=StoryTitel)

        return render(request, 'page/main.html',context={'Storys': storys, 'StoryTitel': StoryTitel, 'summery': summery})

    except Storys.DoesNotExist:
        pass

        return render(request, 'page/main.html',context={'Storys': storys, 'StoryTitel': StoryTitel, 'summery': summery})


def chapters(request,storytitel,pk=-1):
    
    storys = Storys.objects.all()
    chapters = Chapters.objects.all()
    s = Storys.objects.get(StoryTitel=storytitel)
    try:

        if pk == -1:
            StoryTitel = Storys.objects.all().first()
            chapter_titel = Chapters.objects.all().first()
        else:
            StoryTitel = Storys.objects.get(pk=pk)
            chapter_titel = Chapters.objects.get(pk=pk)

        
        story_filter = Storys.objects.filter(StoryTitel = storytitel)
        chapter_filter = Chapters.objects.filter(ForStory=s)
        
        return render(request, "page/chapters.html",  context={ 'story_filter':story_filter, 'Storys': storys,'chapter_titel':chapter_titel, 'StoryTitel':StoryTitel ,'Chapters':chapters,'storytitel':storytitel ,'chapter_filter':chapter_filter} )


    except Storys.DoesNotExist:
        pass


    return render(request, "page/chapters.html",  context={ 'story_filter':story_filter, 'Storys': storys,'chapter_titel':chapter_titel, 'StoryTitel':StoryTitel ,'Chapters':chapters,'storytitel':storytitel ,'chapter_filter':chapter_filter} )


def UserInfo(request,userinfo ):

    selectuser = account.objects.get(username = userinfo)
    selectstory = Storys.objects.filter(Writer = selectuser)

    return render(request, 'page/Userinfo.html' , context={'userinfo':userinfo , 'Storys':Storys , 'selectstory':selectstory , 'Account':account })

