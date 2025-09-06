from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama-aplikasi' : 'Football Shop',
        'nama': 'Haru Urara',
        'kelas': 'PBP A'
    }

    return render(request, "main.html", context)