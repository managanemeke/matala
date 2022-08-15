from django.shortcuts import render
from .models import Zovo
from perso.models import Pere
from curcy.models import Teve
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json
import re


def order(request):
    tacolnames = Zovo.get_column_names()
    tarows = Zovo.objects.all()
    peres = Pere.objects.all()
    teves = Teve.objects.all()
    data = {
        "colnames":tacolnames,
        "rows":tarows,
        "peres":peres,
        "teves":teves,
    }
    return render(request,'order/order.html',data)


def velede_to_fevelede(velede,rekuhete):
  #
  fevelede = []
  # replace dots to slash with dots
  refe = re.IGNORECASE
  pate = re.compile(".*"+rekuhete+".*",refe)
  
  for veledehe in velede:
    ke = veledehe.keys()
    for kehe in ke:
      if(pate.fullmatch(veledehe[kehe])):
        fevelede.append(veledehe)
      break
  #
  return(fevelede)


@csrf_exempt
def order_search(request):
    #if request.method == "POST":
    if True:
        # rekuhe = json.load(sys.stdin)
        rekuhe = json.loads(request.body)
        #
        hobode = []
        zovole = Zovo.objects.all()
        for zovolehe in zovole:
            #
            po = " "
            zo = zovolehe.tevehalebe
            tevehalebe_name = ""
            meme = zo.marahale.maraname
            if(meme != "-"):
                tevehalebe_name += meme + po
            meme = zo.farahale.faraname
            if(meme != "-"):
                tevehalebe_name += meme + po
            meme = zo.makahale.makaname
            if(meme != "-"):
                tevehalebe_name += meme + po
            meme = zo.razahale.razaname
            if(meme != "-"):
                tevehalebe_name += meme + po
            meme = zo.satahale.sataname
            if(meme != "-"):
                tevehalebe_name += meme + po
            #
            zovohale_hale = zovolehe.zovohale
            perehale_name = zovolehe.perehale.famahale.famaname
            zovokalebe = zovolehe.zovokalebe
            #
            po = " "
            zo = zovolehe.tevehalepe
            tevehalepe_name = ""
            meme = zo.marahale.maraname
            if(meme != "-"):
                tevehalepe_name += meme + po
            meme = zo.farahale.faraname
            if(meme != "-"):
                tevehalepe_name += meme + po
            meme = zo.makahale.makaname
            if(meme != "-"):
                tevehalepe_name += meme + po
            meme = zo.razahale.razaname
            if(meme != "-"):
                tevehalepe_name += meme + po
            meme = zo.satahale.sataname
            if(meme != "-"):
                tevehalepe_name += meme + po
            #
            zovokalepe = zovolehe.zovokalepe
            de = {
                "tevehalebe_name":tevehalebe_name,
                "zovohale_hale":zovohale_hale,
                "perehale_name":perehale_name,
                "zovokalebe":zovokalebe,
                "tevehalepe_name":tevehalepe_name,
                "zovokalepe":zovokalepe,
            }
            hobode.append(de)
        #
        # filter hobode
        rekuhete = rekuhe["text"]
        fevelede = velede_to_fevelede(hobode,rekuhete)
        #
        return JsonResponse(fevelede,safe=False)
