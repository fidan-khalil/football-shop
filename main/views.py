from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406408501',
        'name': 'Fidan Khalil Salman',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)