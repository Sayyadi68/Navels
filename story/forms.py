from django import forms

from . import models

class StoryForm(forms.Form):
    class Meta:
        model = models.account
        fields = ['Writer','StoryTitel','ganer','ChapterOne', 'summary','Section']


class ChapterForm(forms.Form):
    class Meta:
        model = models.account
        fields = ['ForStory','ChapterTitel','Section']

