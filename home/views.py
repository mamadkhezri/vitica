from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from capsules.models import TimeCapsule
from .forms import CapsuleSearchForm


class HomeView(View):
    def get(self, request):
        return render(request, 'home/index_two.html')
    

class ExploreView(View):
    form_class = CapsuleSearchForm

    def get(self, request):
        time_capsules = TimeCapsule.objects.all() 
        form = self.form_class(request.GET)  
        if form.is_valid() and form.cleaned_data['search']:
            search_query = form.cleaned_data['search']
            time_capsules = time_capsules.filter(title__contains=search_query)

        return render(request, 'home/explore.html', {'time_capsules': time_capsules, 'form': form})