from django.shortcuts import render
from .models import Suvu


def joint(request):
    tacolnames = Suvu.get_column_names()
    tarows = Suvu.objects.all()
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'joint/joint.html',data)
