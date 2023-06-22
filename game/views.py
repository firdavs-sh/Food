from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from game.forms import RestaurantCreateForm
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from game.models import Reklama, Restaurant1,Comment1



class Restaurant1ListView(ListView):
    queryset = Restaurant1.objects.all()
    paginate_by = 6
    template_name = 'game/music.html'
    

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('qq')
        cat = self.request.GET.get('cat')
        author = self.request.GET.get('author')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(details__icontains=q)
            ).distinct()
        if cat:
            queryset = queryset.filter(categories__icontains=cat)

        if author:
            queryset = queryset.filter(user__username=author)
        return queryset[::-1]

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('unlike')
        post_id2 = request.POST.get('like')
        if post_id is not None:
            post = get_object_or_404(Restaurant1, id=post_id)
            post.likes.remove(request.user)
        if post_id2 is not None:
            post_id2 = request.POST.get('like')
            post = get_object_or_404(Restaurant1, id=post_id2)
            post.likes.add(request.user)
        return redirect('music1')


class Restaurant1DetailView(DetailView):
    queryset = Restaurant1.objects.all()
    
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        comment = request.POST.get('comment')
        c_slug = request.POST.get('slug')
        if c_slug:
                post = get_object_or_404(Restaurant1, slug=c_slug)
                comment = Comment1.objects.create(
                    user=request.user, post=post, text=comment)
                comment.save()
                return redirect('game', c_slug)
        return render('game', c_slug)

def reklama(request):
    data=Reklama.objects.all()
    context={
        "data":data
    }
    return render(request,'game/games.html',context)


def g1(request):
    return render(request,"games/g1.html")

def g2(request):
    return render(request,"games/g2.html")

def g3(request):
    return render(request,"games/g3.html")

def g4(request):
    return render(request,"games/g4.html")

def g5(request):
    return render(request,"games/g5.html")

def g6(request):
    return render(request,"games/g6.html")

def gbase(request):
    return render(request,"games/gbase.html")