from django import forms
from .models import TimeCapsule, Video, Document, Sound, Message, Photo, Comment
from django.forms.widgets import ClearableFileInput

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class PostUpdateCreateForm(forms.ModelForm):
    photo = forms.FileField(widget=MultipleFileInput(attrs={'class': 'form-control'}), required=False)
    video = forms.FileField(widget=MultipleFileInput(attrs={'class': 'form-control'}), required=False)
    sound = forms.FileField(widget=MultipleFileInput(attrs={'class': 'form-control'}), required=False)
    document = forms.FileField(widget=MultipleFileInput(attrs={'class': 'form-control'}), required=False)
    

    
    class Meta:
        model = TimeCapsule
        fields = ('photo', 'video', 'sound','document', 'title', 'message_related', 'tags')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'message_related': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Message'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter tags'})
        }

    def save(self, commit=True):
        TimeCapsule = super().save(commit=commit)

        photo_files = self.cleaned_data.get('photo')
        video_files = self.cleaned_data.get('video')
        sound_files = self.cleaned_data.get('sound')
        document_files = self.cleaned_data.get('document')

        if photo_files:
            for photo in photo_files:
                Photo.objects.create(timecapsule=TimeCapsule, photo=photo)
        if video_files:
            for video in video_files:
                Video.objects.create(timecapsule=TimeCapsule, video=video)
        if sound_files:
            for sound in sound_files:
                Sound.objects.create(timecapsule=TimeCapsule, sound=sound)
        if document_files:
            for document in document_files:
                Document.objects.create(timecapsule=TimeCapsule, document=document)
        return TimeCapsule


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
	


class CommentReplyForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']