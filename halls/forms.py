from .models import Video
from django import forms

#regular

#model-based
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'url', 'youtube_id']
# customize appearance
        labels = {'youtube_id':'YouTube Id'} #capitalize label

# Search

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=225, label="Search for videos: ")