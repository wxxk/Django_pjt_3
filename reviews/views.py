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

def detail(request, pk):
  context = {
    'review' : Review.objects.get(pk=pk),
  }
  return render(request, 'reviews/detail.html', context)

def update(request, pk):
  review = Review.objects.get(pk=pk)
  if request.method == 'POST':
    update_form = ReviewForm(request.POST, instance=review)
    if update_form.is_valid():
      update_form.save()
      return redirect('reviews:detail', review.pk)
  else:
    update_form = ReviewForm(instance=review)
  context = {
    'update_form' : update_form,
    'num' : review.pk,
  }
  return render(request, 'reviews/update.html', context)

def delete(request, pk):
  Review.objects.get(pk=pk).delete()
  return redirect('reviews:index')