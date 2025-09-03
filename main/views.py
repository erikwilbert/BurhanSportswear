from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi' : 'Burhan Sportswear',
        'name': 'Erik Wilbert',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)