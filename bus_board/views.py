from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html')

def search_results(request):
  return render(request, 'search.html')
