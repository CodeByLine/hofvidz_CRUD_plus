from .models import Video
from django import forms

#regular

#model-based
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['url']
# customize appearance
        labels = {'url':'YouTube Url'} #capitalize label

# Search

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=225, label="Search for videos: ")