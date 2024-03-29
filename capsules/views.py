from django.shortcuts import render
from typing import Any
from django import http
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import TimeCapsule, Photo, Sound, Document, Video, Message, vote
from django.http import JsonResponse
from .forms import PostUpdateCreateForm, CommentCreateForm, CommentReplyForm
from taggit.models import Tag
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PostcreateView(LoginRequiredMixin, View):
    form_class = PostUpdateCreateForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        tags = Tag.objects.all()
        return render(request, 'capsules/create_cap.html', {'form': form, 'tags': tags})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(request.user)

        if form.is_valid():
            new_capsule = form.save(commit=False)
            new_capsule.slug = slugify(form.cleaned_data['title'][:30])
            new_capsule.creator = request.user
            new_capsule.save()

            Photo_files = request.FILES.getlist('photo')  # Retrieve a list of uploaded image files
            video_files = request.FILES.getlist('video')  # Retrieve a list of uploaded video files
            Sound_files = request.FILES.getlist('sound')  # Retrieve a list of uploaded audio files
            document_file = request.FILES.getlist('document')

            try:
                for photo_file in Photo_files:
                    Photo.objects.create(time_capsule=new_capsule, photo=photo_file)
                for video_file in video_files:
                    Video.objects.create(time_capsule=new_capsule, video=video_file)
                for sound_file in Sound_files:
                    Sound.objects.create(time_capsule=new_capsule, sound=sound_file)
                for document_file in document_file:
                    Document.objects.create(time_capsule=new_capsule, document=document_file)
                
            except Exception as e:
                print("Error during file creation:", e)

            form.save_m2m()

            messages.success(request, 'You created a new post', 'success')
            return redirect('capsules:capsules_detail', new_capsule.id, new_capsule.slug)

        return render(request, 'capsules/create_cap.html', {'form': form, 'tags': Tag.objects.all()})
    
class PostDetailView(View):
    form_class = CommentCreateForm
    form_class_reply = CommentReplyForm

    def get(self, request, cap_id, cap_slug):
        time_capsule_instance = get_object_or_404(TimeCapsule, pk=cap_id, slug=cap_slug)
        comments = time_capsule_instance.time_capsule_comments().filter(is_reply=False)
        can_like = False
        if request.user.is_authenticated and time_capsule_instance.user_can_like(request.user):
            can_like = True

        can_unlike = False
        if request.user.is_authenticated and vote.objects.filter(creator=request.user, time_capsule=time_capsule_instance).exists():
            can_unlike = True

        form = self.form_class()
        reply_form = self.form_class_reply()

        likes_count = vote.objects.filter(time_capsule=time_capsule_instance).count()
        tags = time_capsule_instance.tags.all()

        return render(request, 'capsules/detail.html', {
            'time_capsule': time_capsule_instance,
            'comments': comments,
            'form': form,
            'reply_form': reply_form,
            'can_like': can_like,
            'can_unlike': can_unlike,
            'likes_count': likes_count,
            'tags': tags,
        })

    @method_decorator(login_required)
    def post(self, request, cap_id, cap_slug):
        time_capsule_instance = get_object_or_404(TimeCapsule, pk=cap_id, slug=cap_slug)
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.creator = request.user
            new_comment.time_capsule = time_capsule_instance
            new_comment.save()
            messages.success(request, 'Your comment has been submitted successfully.', extra_tags='success')
            

            form = self.form_class()
        
        comments = time_capsule_instance.time_capsule_comments.filter(is_reply=False)
        reply_form = self.form_class_reply()

        return render(request, 'capsules/detail.html', {
            'time_capsule': time_capsule_instance,
            'comments': comments,
            'form': form,
            'reply_form': reply_form,
            
        })
    
class LikePostView(LoginRequiredMixin, View):
    def get(self, request, timecapsule_id):
        timecapsule = get_object_or_404(TimeCapsule, id=timecapsule_id)
        like, created = vote.objects.get_or_create(creator=request.user, timecapsule=timecapsule)
        if not created:
            like.delete()
        return redirect('capsules:post_detail', timecapsule.id, timecapsule.slug)
    
class UnlikePostView(LoginRequiredMixin, View):
    def unlike_post(self, request, timecapsule):
        try:
            existing_like = vote.objects.get(creator=request.user, timecapsule=timecapsule)
            existing_like.delete()
        except vote.DoesNotExist:
            pass
    def get(self, request, timecapsule_id):
        post = get_object_or_404(TimeCapsule, id=timecapsule_id)
        if request.method == "GET" and request.user.is_authenticated:
            self.unlike_post(request, post)
            return redirect('posts:post_detail', timecapsule_id=timecapsule_id, timecapsule_slug=TimeCapsule.slug)
        return redirect('posts:post_detail', timecapsule_id=timecapsule_id, timecapsule_slug=TimeCapsule.slug)
