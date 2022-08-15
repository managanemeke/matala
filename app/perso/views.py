from django.shortcuts import render
from .models import Pere


def perso(request):
    tacolnames = Pere.get_column_names()
    tarows = Pere.objects.all()
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'perso/perso.html',data)
