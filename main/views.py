from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'namaApp' : 'Football Shop',
        'nama': 'Haru Urara',
        'kelas': 'PBP A'
    }

    return render(request, "main.html", context)