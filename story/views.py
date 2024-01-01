from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout, login,authenticate
from django.shortcuts import redirect
from django.views import generic
from django.contrib import messages
from django.http import JsonResponse


from .forms import StoryForm,ChapterForm
from .models import Chapters,Storys
from account.models import account
from account.views import Profile

def is_ajax(request):
    """
    :param request: get post request
    :return: True if it was ajax request and False for not ajax
    """
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def ReadStory(request,chaptername,storytitel):

    storys = Storys.objects.all()
    chapters = Chapters.objects.all()
    
    s = Storys.objects.get(StoryTitel=storytitel)

    chapter_filter = Chapters.objects.filter(ForStory=s , ChapterTitel=chaptername)
    show_allChapters  = Chapters.objects.filter(ForStory=s)
   
    return render(request, "story/ReadStory.html" , context={'show_allChapters':show_allChapters,'chapters':Chapters,'chaptername':chaptername,'storytitel':storytitel,'chapter_filter':chapter_filter} )



def WriteStory(request,pk=-1):

    form2 = ChapterForm(request.POST)
    account.objects.all()
    storys = Storys.objects.all()

    if is_ajax(request) and request.method == "POST":

        writer = request.user
        ForStory = form2.data['ForStory']
        Storyname = Storys.objects.get(StoryTitel= ForStory)
        Section = form2.data['Section']
        ChapterTitel = form2.data['ChapterTitel']

        if form2.is_valid():

            Chapters.objects.create(writer = writer ,ForStory=Storyname , ChapterTitel=ChapterTitel, Section=Section)
            messages.success(request, 'داستان شما ذخیره شد.')
            return JsonResponse({"success": 'ok', "success_message": 'داستان شما ذخیره شد.'}, safe=False, status=200)


    try:

        if pk == -1:
            StoryTitel = Storys.objects.all().first()
        else:
            StoryTitel = Storys.objects.get(pk=pk)

        summery = Storys.objects.filter(StoryTitel=StoryTitel)

        return render(request, 'story/WriteStory.html',
                      context={'Storys': storys, 'StoryTitel': StoryTitel, 'summery': summery})

    except Storys.DoesNotExist:
        pass


    return render(request, "story/WriteStory.html" )


