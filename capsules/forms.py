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
        model = TimeCapsule  # Specify the model associated with this form
        fields = ('photo', 'video', 'sound', 'document', 'title', 'message_related', 'publication_date', 'tags')

        # Define widgets and any other Meta options you need
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'message_related': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Message'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter tags'}),
            'publication_date': forms.SelectDateWidget(attrs={'class': 'form-control', 'placeholder': 'Enter the date the capsule was opened'}),
        }

    def clean_photo(self):
        photo_files = self.cleaned_data.get('photo')
        # Add validation for photo_files if needed
        return photo_files

    def clean_video(self):
        video_files = self.cleaned_data.get('video')
        # Add validation for video_files if needed
        return video_files

    def clean_sound(self):
        sound_files = self.cleaned_data.get('sound')
        # Add validation for sound_files if needed
        return sound_files

    def clean_document(self):
        document_files = self.cleaned_data.get('document')
        # Add validation for document_files if needed
        return document_files

    def save(self, commit=True):
        time_capsule = super().save(commit=commit)

        photo_files = self.cleaned_data.get('photo')
        video_files = self.cleaned_data.get('video')
        sound_files = self.cleaned_data.get('sound')
        document_files = self.cleaned_data.get('document')

        try:
            if photo_files:
                for photo in photo_files:
                    Photo.objects.create(time_capsule=time_capsule, photo=photo)
            if video_files:
                for video in video_files:
                    Video.objects.create(time_capsule=time_capsule, video=video)
            if sound_files:
                for sound in sound_files:
                    Sound.objects.create(time_capsule=time_capsule, sound=sound)
            if document_files:
                for document in document_files:
                    Document.objects.create(time_capsule=time_capsule, document=document)
        except Exception as e:
            print("Error during file creation:", e)

        return time_capsule


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
	


class CommentReplyForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']