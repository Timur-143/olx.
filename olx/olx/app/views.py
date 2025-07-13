# views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Ad, Category
from .forms import AdForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


class MainPageView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['ads'] = Ad.objects.all()
        ctx['categories'] = Category.objects.all()
        return ctx


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('main')


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/reg.html'
    success_url = reverse_lazy('main')


class UserLogoutView(LogoutView):
    next_page = 'main'


class AdListView(ListView):
    model = Ad
    template_name = 'ad_list.html'
    context_object_name = 'ads'

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))
        return qs


class AdDetailView(DetailView):
    model = Ad
    template_name = 'ad_detail.html'
    context_object_name = 'ad'


class AdCreateView(LoginRequiredMixin, CreateView):
    model = Ad
    form_class = AdForm
    template_name = 'ad_create.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdListByUserView(ListView):
    model = Ad
    template_name = 'ads_by_user.html'
    context_object_name = 'ads'



class AdsByCategoryView(ListView):
    model = Ad
    template_name = 'ads_by_category.html'
    context_object_name = 'ads'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['category_id'])
        return Ad.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


@login_required
def ad_delete(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if request.user != ad.author:
        return HttpResponseForbidden("Вы не можете удалить это объявление.")

    if request.method == "POST":
        ad.delete()
        return redirect('main')

    return redirect('ad_detail', pk=pk)


