from django.shortcuts import render

dogs = [
  {'Name': 'Milo', 'Breed': 'Husky', 'Description': 'Adventurous and annoying', 'Age': 3},
  {'Name': 'Hamburger', 'Breed': 'Schnauzer', 'Description': 'Hamburger consumption is unhealthy most of the time', 'Age': 2},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })