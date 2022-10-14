from django.shortcuts import render,redirect
from .forms import ReviewForm
from .models import Review

# Create your views here.
def index(request):
  context = {
    'reviews' : Review.objects.all()
  }
  return render(request, 'reviews/index.html', context)

def create(request):
  if request.method == 'POST':
    create_form = ReviewForm(request.POST)
    if create_form.is_valid():
      create_form.save()
      return redirect('reviews:index')
  else:
    create_form = ReviewForm()
  context = {
    'create_form': create_form,
  }
  return render(request, 'reviews/create.html', context)