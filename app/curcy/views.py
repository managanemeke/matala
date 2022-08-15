from decimal import Decimal
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from index.models import Hala
from order.models import Zovo
from perso.models import Pere
from .forms import *
from metele.functions import generate_hale


import requests
from lxml import html
from lxml import etree
from html.parser import HTMLParser
import csv
from itertools import chain
#
def tree_to_str(tere):
    tasa = etree.tostring(tere)
    tasaba = tasa.decode('utf-8')
    tasa = HTMLParser().unescape(tasaba)
    return(tasa)
#
def file_to_text(falo):
    with open(falo,'r') as fo:
        te = fo.read()
    return(te)
#
def url_to_str(huru):
    he = requests.get(huru)
    #
    te = he.text.encode('utf-8').decode('utf-8')
    #
    return(te)
#
def url_to_file(huru,falo):
    he = requests.get(huru)
    #
    with open(falo,'wb') as fo:
        fo.write(he.text.encode('utf-8'))
    #
#
def lele_to_csv(lele,falo):
    #
    with open(falo,"w",newline="") as fo:
        vo = csv.writer(fo)
        vo.writerows(lele)
#
def galaka_url_to_zovosade(huru):
    #
    text = url_to_str(huru)
    #
    #print(text)
    #
    tree = html.fromstring(text)
    #
    xp = ""
    xp += r'//html/body/div[@class="center_area"]/'
    xp += r'div[@class="cera_area"]/'
    xp += r'div[@class="content_area"]/'
    xp += r'form[@class="save_order"]/'
    xp += r'table[@class="sklad_table"]/'
    xp += r'tr'
    #
    trli = []
    #
    trs = tree.xpath(xp)
    #
    '''
    if(len(trs)>0):
        print(tree_to_str(trs[0]))
    else:
        print("pusto")
    '''
    #
    #exit()
    #
    for tr in trs:
        xp = 'td'
        tds = tr.xpath(xp)
        tdli = []
        for td in tds:
            xp = 'b/text()'
            texts = td.xpath(xp)
            if(len(texts)>0):
                text = texts[0].strip()
                text = text.replace("\n","")
                tdli.append(text)
            else:
                xp = 'text()'
                texts = td.xpath(xp)
                if(len(texts)>0):
                    text = texts[0].strip()
                    text = text.replace("\n","")
                    if(text != ""):
                        tdli.append(text)
                else:
                    tdli.append("-")
        #
        trli.append(tdli)
    #
    #print(trli)
    #
    zovosade = [{'savanamebe':te[1],'zovokalebe':1,'tevehalepe':'tulutulu','zovokalepe':te[2]} for te in trli]
    #
    return(zovosade)
#
def galaka_urls_to_zovosade(hurule):
    #
    bonobo = []
    for huru in hurule:
        bonobo = list(chain(bonobo,galaka_url_to_zovosade(huru)))
    #
    return(bonobo)
#
def galaka_get_savale():
    #
    ro = r'https://www.galakmet.ru/sklad/'
    #
    hurule = []
    rohe = ''
    rohe += ro+'aluminijevaja-truba-kruglaya/'
    hurule.append(rohe)
    rohe = ''
    rohe += ro+'truba-aluminievaya-profilnaya-'
    rohe += 'pryamougolnaya-kvadratnaya/'
    hurule.append(rohe)
    #
    savale = galaka_urls_to_savale(hurule)
    #
    return(savale)
#
def galaka_urls_to_savale(hurule):
    zovosade = galaka_urls_to_zovosade(hurule)
    savale = [zo.savanamebe for zo in zovosade]
    return(savale)
#
def galaka_get_zovosade():
    #
    ro = r'https://www.galakmet.ru/sklad/'
    #
    hurule = []
    rohe = ''
    rohe += ro+'aluminijevaja-truba-kruglaya/'
    hurule.append(rohe)
    rohe = ''
    rohe += ro+'truba-aluminievaya-profilnaya-'
    rohe += 'pryamougolnaya-kvadratnaya/'
    hurule.append(rohe)
    #
    zovosade = galaka_urls_to_zovosade(hurule)
    #
    return(zovosade)
#
def str_to_decimal(sa):
    sa = str(sa)
    sa = sa.replace(",",".")
    sa = sa.replace(" ","")
    de = Decimal(sa)
    return(de)
#
def zovosade_to_zovode(zovosade):
    for zo in zovosade:
        ke = set(zo.keys())
        if("savanamebe" in ke):
            bulo = Sava.objects.get(savaname = zo["savanamebe"])
            buko = Solo.objects.get(savahale = bulo.savahale)
            zo["tevehalebe"] = buko.tevehale
            zo["zovokalebe"] = str_to_decimal(zo["zovokalebe"])
            zo["zovokalepe"] = str_to_decimal(zo["zovokalepe"])
    return(zovosade)
#


def galaka_sava(request):
    #
    savale = galaka_get_savale()
    #
    for savahe in savale:
        #
        sava = Sava()
        #
        hale = generate_hale(4)
        while(Hala.objects.filter(halahale = hale).exists()):
            hale = generate_hale(4)
        hala = Hala()
        hala.halahale = hale
        hala.save()
        #
        sava.savahale = hale
        sava.savaname = savahe
        sava.save()
    #
    return HttpResponse("I get it!")


def galaka_zovo(request):
    #
    zovosade = galaka_get_zovosade()
    #
    '''
    bala = zovosade[0].keys()
    satara = "\n".join(list(bala))
    open("zovosade.txt","w").write(satara)
    '''
    #
    zovode = zovosade_to_zovode(zovosade)
    #
    '''
    bala = [str(zo["tevehalebe"])+","+str(zo["zovokalebe"])+","+str(zo["tevehalepe"])+","+str(zo["zovokalepe"]) for zo in zovode]
    satara = "\n".join(list(bala))
    open("zovode.txt","w").write(satara)
    '''
    #
    for zo in zovode:
        #
        zovo = Zovo()
        #
        hale = generate_hale(4)
        while(Hala.objects.filter(halahale = hale).exists()):
            hale = generate_hale(4)
        hala = Hala()
        hala.halahale = hale
        hala.save()
        #
        zovo.zovohale = hale
        zovo.perehale = Pere.objects.get(perehale = "galagala")
        zovo.tevehalebe = Teve.objects.get(tevehale = zo["tevehalebe"])
        zovo.zovokalebe = zo["zovokalebe"]
        zovo.tevehalepe = Teve.objects.get(tevehale = zo["tevehalepe"])
        zovo.zovokalepe = zo["zovokalepe"]
        zovo.save()
    #
    return HttpResponse("I get it!")


def curcy(request):
    tacolnames = Teve.get_column_names()
    tarows = Teve.objects.all()
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/curcy.html',data)


def saha(request, pk):
    tacolnames = Teve.get_column_names()
    tarows = [get_object_or_404(Teve, pk=pk)]
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/curcy.html',data)


def kara(request):
    if request.method == "POST":
        form = TeveForm(request.POST)
        if form.is_valid():
            teve = form.save(commit=False)
            #
            hale = generate_hale(4)
            while(Hala.objects.filter(halahale = hale).exists()):
                hale = generate_hale(4)
            hala = Hala()
            hala.halahale = hale
            hala.save()
            #
            teve.tevehale = hale
            teve.save()
            return redirect('teve_saha', pk=teve.pk)
    else:
        fo = TeveForm()
        data = {
            "form": fo,
        }
        return render(request, 'curcy/kara.html', data)


def hapa(request, pk):
    if request.method == "POST":
        form = TeveForm(request.POST)
        if form.is_valid():
            teve = form.save(commit=False)
            nuteve = Teve.objects.get(pk=pk) 
            #
            nuteve.marahale = teve.marahale
            nuteve.farahale = teve.farahale
            nuteve.makahale = teve.makahale
            nuteve.razahale = teve.razahale
            nuteve.satahale = teve.satahale
            nuteve.matahale = teve.matahale
            nuteve.save()
            return redirect('teve_saha', pk=pk)
    else:
        nuteve = Teve.objects.get(pk=pk)
        hama = {
            "marahale": nuteve.marahale,
            "farahale": nuteve.farahale,
            "makahale": nuteve.makahale,
            "razahale": nuteve.razahale,
            "satahale": nuteve.satahale,
            "matahale": nuteve.matahale,
        }
        fo = TeveForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/hapa.html', data)


def dala(request, pk):
    if request.method == "POST":
        form = TeveForm(request.POST)
        #if form.is_valid():
        if True:
            #
            teve = Teve.objects.get(pk=pk)
            teve.delete()
            #
            hala = Hala.objects.get(pk=pk)
            hala.delete()
            #
            return redirect('curcy')
    else:
        nuteve = Teve.objects.get(pk=pk)
        hama = {
            "marahale": nuteve.marahale,
            "farahale": nuteve.farahale,
            "makahale": nuteve.makahale,
            "razahale": nuteve.razahale,
            "satahale": nuteve.satahale,
            "matahale": nuteve.matahale,
        }
        fo = TeveForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/dala.html', data)


def mara_mara(request):
    tacolnames = Mara.get_column_names()
    tarows = Mara.objects.all()
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/mara_saha.html',data)


def mara_saha(request, pk):
    tacolnames = Mara.get_column_names()
    tarows = [get_object_or_404(Mara, pk=pk)]
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/mara_saha.html',data)


def mara_kara(request):
    if request.method == "POST":
        form = MaraForm(request.POST)
        if form.is_valid():
            lema = form.save(commit=False)
            #
            hale = generate_hale(4)
            while(Hala.objects.filter(halahale = hale).exists()):
                hale = generate_hale(4)
            hala = Hala()
            hala.halahale = hale
            hala.save()
            #
            lema.marahale = hale
            lema.save()
            return redirect('mara_saha', pk=lema.pk)
    else:
        fo = MaraForm()
        data = {
            "form": fo,
        }
        return render(request, 'curcy/kara.html', data)


def mara_hapa(request, pk):
    if request.method == "POST":
        form = MaraForm(request.POST)
        if form.is_valid():
            lema = form.save(commit=False)
            nulema = Mara.objects.get(pk=pk) 
            #
            nulema.maraname = lema.maraname
            nulema.save()
            return redirect('mara_saha', pk=pk)
    else:
        nulema = Mara.objects.get(pk=pk)
        hama = {
            "maraname": nulema.maraname,
        }
        fo = MaraForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/hapa.html', data)


def mara_dala(request, pk):
    if request.method == "POST":
        form = MaraForm(request.POST)
        #if form.is_valid():
        if True:
            #
            lema = Mara.objects.get(pk=pk)
            lema.delete()
            #
            hala = Hala.objects.get(pk=pk)
            hala.delete()
            #
            return redirect('mara_mara')
    else:
        nulema = Mara.objects.get(pk=pk)
        hama = {
            "maraname": nulema.maraname,
        }
        fo = MaraForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/dala.html', data)


def fara_fara(request):
    tacolnames = Fara.get_column_names()
    tarows = Fara.objects.all()
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/fara_saha.html',data)


def fara_saha(request, pk):
    tacolnames = Fara.get_column_names()
    tarows = [get_object_or_404(Fara, pk=pk)]
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/fara_saha.html',data)


def fara_kara(request):
    if request.method == "POST":
        form = FaraForm(request.POST)
        if form.is_valid():
            lema = form.save(commit=False)
            #
            hale = generate_hale(4)
            while(Hala.objects.filter(halahale = hale).exists()):
                hale = generate_hale(4)
            hala = Hala()
            hala.halahale = hale
            hala.save()
            #
            lema.farahale = hale
            lema.save()
            return redirect('fara_saha', pk=lema.pk)
    else:
        fo = FaraForm()
        data = {
            "form": fo,
        }
        return render(request, 'curcy/kara.html', data)


def fara_hapa(request, pk):
    if request.method == "POST":
        form = FaraForm(request.POST)
        if form.is_valid():
            lema = form.save(commit=False)
            nulema = Fara.objects.get(pk=pk) 
            #
            nulema.faraname = lema.faraname
            nulema.save()
            return redirect('fara_saha', pk=pk)
    else:
        nulema = Fara.objects.get(pk=pk)
        hama = {
            "faraname": nulema.faraname,
        }
        fo = FaraForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/hapa.html', data)


def fara_dala(request, pk):
    if request.method == "POST":
        form = FaraForm(request.POST)
        #if form.is_valid():
        if True:
            #
            lema = Fara.objects.get(pk=pk)
            lema.delete()
            #
            hala = Hala.objects.get(pk=pk)
            hala.delete()
            #
            return redirect('fara_fara')
    else:
        nulema = Fara.objects.get(pk=pk)
        hama = {
            "faraname": nulema.faraname,
        }
        fo = FaraForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/dala.html', data)


def maka_maka(request):
    tacolnames = Maka.get_column_names()
    tarows = Maka.objects.all()
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/maka_saha.html',data)


def maka_saha(request, pk):
    tacolnames = Maka.get_column_names()
    tarows = [get_object_or_404(Maka, pk=pk)]
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/maka_saha.html',data)


def maka_kara(request):
    if request.method == "POST":
        form = MakaForm(request.POST)
        if form.is_valid():
            lema = form.save(commit=False)
            #
            hale = generate_hale(4)
            while(Hala.objects.filter(halahale = hale).exists()):
                hale = generate_hale(4)
            hala = Hala()
            hala.halahale = hale
            hala.save()
            #
            lema.makahale = hale
            lema.save()
            return redirect('maka_saha', pk=lema.pk)
    else:
        fo = MakaForm()
        data = {
            "form": fo,
        }
        return render(request, 'curcy/kara.html', data)


def maka_hapa(request, pk):
    if request.method == "POST":
        form = MakaForm(request.POST)
        if form.is_valid():
            lema = form.save(commit=False)
            nulema = Maka.objects.get(pk=pk) 
            #
            nulema.makaname = lema.makaname
            nulema.save()
            return redirect('maka_saha', pk=pk)
    else:
        nulema = Maka.objects.get(pk=pk)
        hama = {
            "makaname": nulema.makaname,
        }
        fo = MakaForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/hapa.html', data)


def maka_dala(request, pk):
    if request.method == "POST":
        form = MakaForm(request.POST)
        #if form.is_valid():
        if True:
            #
            lema = Maka.objects.get(pk=pk)
            lema.delete()
            #
            hala = Hala.objects.get(pk=pk)
            hala.delete()
            #
            return redirect('maka_maka')
    else:
        nulema = Maka.objects.get(pk=pk)
        hama = {
            "makaname": nulema.makaname,
        }
        fo = MakaForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/dala.html', data)


def raza_raza(request):
    tacolnames = Raza.get_column_names()
    tarows = Raza.objects.all()
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/raza_saha.html',data)


def raza_saha(request, pk):
    tacolnames = Raza.get_column_names()
    tarows = [get_object_or_404(Raza, pk=pk)]
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/raza_saha.html',data)


def raza_kara(request):
    if request.method == "POST":
        form = RazaForm(request.POST)
        if form.is_valid():
            lema = form.save(commit=False)
            #
            hale = generate_hale(4)
            while(Hala.objects.filter(halahale = hale).exists()):
                hale = generate_hale(4)
            hala = Hala()
            hala.halahale = hale
            hala.save()
            #
            lema.razahale = hale
            lema.save()
            return redirect('raza_saha', pk=lema.pk)
    else:
        fo = RazaForm()
        data = {
            "form": fo,
        }
        return render(request, 'curcy/kara.html', data)


def raza_hapa(request, pk):
    if request.method == "POST":
        form = RazaForm(request.POST)
        if form.is_valid():
            lema = form.save(commit=False)
            nulema = Raza.objects.get(pk=pk) 
            #
            nulema.razaname = lema.razaname
            nulema.save()
            return redirect('raza_saha', pk=pk)
    else:
        nulema = Raza.objects.get(pk=pk)
        hama = {
            "razaname": nulema.razaname,
        }
        fo = RazaForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/hapa.html', data)


def raza_dala(request, pk):
    if request.method == "POST":
        form = RazaForm(request.POST)
        #if form.is_valid():
        if True:
            #
            lema = Raza.objects.get(pk=pk)
            lema.delete()
            #
            hala = Hala.objects.get(pk=pk)
            hala.delete()
            #
            return redirect('raza_raza')
        else:
            return HttpResponseNotFound('404')
    else:
        nulema = Raza.objects.get(pk=pk)
        hama = {
            "razaname": nulema.razaname,
        }
        fo = RazaForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/dala.html', data)


def sata_sata(request):
    tacolnames = Sata.get_column_names()
    tarows = Sata.objects.all()
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/sata_saha.html',data)


def sata_saha(request, pk):
    tacolnames = Sata.get_column_names()
    tarows = [get_object_or_404(Sata, pk=pk)]
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/sata_saha.html',data)


def sata_kara(request):
    if request.method == "POST":
        form = SataForm(request.POST)
        if form.is_valid():
            lema = form.save(commit=False)
            #
            hale = generate_hale(4)
            while(Hala.objects.filter(halahale = hale).exists()):
                hale = generate_hale(4)
            hala = Hala()
            hala.halahale = hale
            hala.save()
            #
            lema.satahale = hale
            lema.save()
            return redirect('sata_saha', pk=lema.pk)
    else:
        fo = SataForm()
        data = {
            "form": fo,
        }
        return render(request, 'curcy/kara.html', data)


def sata_hapa(request, pk):
    if request.method == "POST":
        form = SataForm(request.POST)
        if form.is_valid():
            lema = form.save(commit=False)
            nulema = Sata.objects.get(pk=pk) 
            #
            nulema.sataname = lema.sataname
            nulema.save()
            return redirect('sata_saha', pk=pk)
    else:
        nulema = Sata.objects.get(pk=pk)
        hama = {
            "sataname": nulema.sataname,
        }
        fo = SataForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/hapa.html', data)


def sata_dala(request, pk):
    if request.method == "POST":
        form = SataForm(request.POST)
        #if form.is_valid():
        if True:
            #
            lema = Sata.objects.get(pk=pk)
            lema.delete()
            #
            hala = Hala.objects.get(pk=pk)
            hala.delete()
            #
            return redirect('sata_sata')
    else:
        nulema = Sata.objects.get(pk=pk)
        hama = {
            "sataname": nulema.sataname,
        }
        fo = SataForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/dala.html', data)


def mata_mata(request):
    tacolnames = Mata.get_column_names()
    tarows = Mata.objects.all()
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/mata_saha.html',data)


def mata_saha(request, pk):
    tacolnames = Mata.get_column_names()
    tarows = [get_object_or_404(Mata, pk=pk)]
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/mata_saha.html',data)


def mata_kara(request):
    if request.method == "POST":
        form = MataForm(request.POST)
        if form.is_valid():
            lema = form.save(commit=False)
            #
            hale = generate_hale(4)
            while(Hala.objects.filter(halahale = hale).exists()):
                hale = generate_hale(4)
            hala = Hala()
            hala.halahale = hale
            hala.save()
            #
            lema.matahale = hale
            lema.save()
            return redirect('mata_saha', pk=lema.pk)
    else:
        fo = MataForm()
        data = {
            "form": fo,
        }
        return render(request, 'curcy/kara.html', data)


def mata_hapa(request, pk):
    if request.method == "POST":
        form = MataForm(request.POST)
        if form.is_valid():
            lema = form.save(commit=False)
            nulema = Mata.objects.get(pk=pk) 
            #
            nulema.mataname = lema.mataname
            nulema.save()
            return redirect('mata_saha', pk=pk)
    else:
        nulema = Mata.objects.get(pk=pk)
        hama = {
            "mataname": nulema.mataname,
        }
        fo = MataForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/hapa.html', data)


def mata_dala(request, pk):
    if request.method == "POST":
        form = MataForm(request.POST)
        #if form.is_valid():
        if True:
            #
            lema = Mata.objects.get(pk=pk)
            lema.delete()
            #
            hala = Hala.objects.get(pk=pk)
            hala.delete()
            #
            return redirect('mata_mata')
    else:
        nulema = Mata.objects.get(pk=pk)
        hama = {
            "mataname": nulema.mataname,
        }
        fo = MataForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/dala.html', data)


def sava_sava(request):
    tacolnames = Sava.get_column_names()
    tarows = Sava.objects.all()
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/sava_saha.html',data)


def sava_saha(request, pk):
    tacolnames = Sava.get_column_names()
    tarows = [get_object_or_404(Sava, pk=pk)]
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/sava_saha.html',data)


def sava_kara(request):
    if request.method == "POST":
        form = SavaForm(request.POST)
        if form.is_valid():
            lema = form.save(commit=False)
            #
            hale = generate_hale(4)
            while(Hala.objects.filter(halahale = hale).exists()):
                hale = generate_hale(4)
            hala = Hala()
            hala.halahale = hale
            hala.save()
            #
            lema.savahale = hale
            lema.save()
            return redirect('sava_saha', pk=lema.pk)
    else:
        fo = SavaForm()
        data = {
            "form": fo,
        }
        return render(request, 'curcy/kara.html', data)


def sava_hapa(request, pk):
    if request.method == "POST":
        form = SavaForm(request.POST)
        if form.is_valid():
            lema = form.save(commit=False)
            nulema = Sava.objects.get(pk=pk) 
            #
            nulema.savaname = lema.savaname
            nulema.save()
            return redirect('sava_saha', pk=pk)
    else:
        nulema = Sava.objects.get(pk=pk)
        hama = {
            "savaname": nulema.savaname,
        }
        fo = SavaForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/hapa.html', data)


def sava_dala(request, pk):
    if request.method == "POST":
        form = SavaForm(request.POST)
        #if form.is_valid():
        if True:
            #
            lema = Sava.objects.get(pk=pk)
            lema.delete()
            #
            hala = Hala.objects.get(pk=pk)
            hala.delete()
            #
            return redirect('sava_sava')
    else:
        nulema = Sava.objects.get(pk=pk)
        hama = {
            "savaname": nulema.savaname,
        }
        fo = SavaForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/dala.html', data)


def solo_solo(request):
    tacolnames = Solo.get_column_names()
    tarows = Solo.objects.all()
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/solo_saha.html',data)


def solo_saha(request, pk):
    tacolnames = Solo.get_column_names()
    tarows = [get_object_or_404(Solo, pk=pk)]
    data = {
        "colnames":tacolnames,
        "rows":tarows,
    }
    return render(request,'curcy/solo_saha.html',data)


def solo_kara(request):
    if request.method == "POST":
        form = SoloSmartForm(request.POST)
        if form.is_valid():
            lema = form.save(commit=False)
            #
            hale = generate_hale(4)
            while(Hala.objects.filter(halahale = hale).exists()):
                hale = generate_hale(4)
            hala = Hala()
            hala.halahale = hale
            hala.save()
            #
            lema.solohale = hale
            lema.save()
            return redirect('solo_saha', pk=lema.pk)
    else:
        fo = SoloSmartForm()
        data = {
            "form": fo,
        }
        return render(request, 'curcy/kara.html', data)


def solo_hapa(request, pk):
    if request.method == "POST":
        form = SoloForm(request.POST)
        if form.is_valid():
            lema = form.save(commit=False)
            nulema = Solo.objects.get(pk=pk) 
            #
            nulema.savahale = lema.savahale
            nulema.tevehale = lema.tevehale
            nulema.save()
            return redirect('solo_saha', pk=pk)
    else:
        nulema = Solo.objects.get(pk=pk)
        hama = {
            "savahale": nulema.savahale,
            "tevehale": nulema.tevehale,
        }
        fo = SoloForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/hapa.html', data)


def solo_dala(request, pk):
    if request.method == "POST":
        form = SoloForm(request.POST)
        #if form.is_valid():
        if True:
            #
            lema = Solo.objects.get(pk=pk)
            lema.delete()
            #
            hala = Hala.objects.get(pk=pk)
            hala.delete()
            #
            return redirect('solo_solo')
    else:
        nulema = Solo.objects.get(pk=pk)
        hama = {
            "savahale": nulema.savahale,
            "tevehale": nulema.tevehale,
        }
        fo = SoloForm(hama)
        data = {
            "form": fo,
        }
        return render(request, 'curcy/dala.html', data)