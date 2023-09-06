from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Barang 1',
        'amount': 999,
        'description': 'Ini adalah barang 1',
        'type': 'Ini tipe barang 1'
    }

    return render(request, "main.html", context)