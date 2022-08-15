from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from jinja2 import Environment

import re
from decimal import Decimal

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    env.filters['tafaname'] = tafaname
    env.filters['haraname'] = haraname
    env.filters['zovokale'] = zovokale
    env.filters['tevehale'] = tevehale
    return env

def tafaname(va):
    vala = va.tafaname
    resu = "wrong_format"
    if(len(vala)==12):
        be=vala[0:2]
        pe=vala[2:5]
        ge=vala[5:8]
        ke=vala[8:10]
        ve=vala[10:12]
        fe=" "
        ze="-"
        resu = be+fe+pe+fe+ge+ze+ke+ze+ve
    return resu


def haraname(va):
    vala = va.haraname
    resu = "wrong_format"
    pa = re.compile(r'(\w+):\/\/(www\.|)([\w.]+)\/.*')
    ma = re.fullmatch(pa,vala)
    if(ma):
        resu = ma[3]
    return resu


def zovokale(va):
    vala = va
    #resu = vala.normalize()
    resu = vala.quantize(Decimal('1000000'))
    return resu


def tevehale(va):
    vala = va
    resu ="wrong_format"
    po = " "
    resu = ""
    if(False):
        ...
    if(vala.marahale.maraname!="-"):
        resu += vala.marahale.maraname+po
    if(vala.farahale.faraname!="-"):
        resu += vala.farahale.faraname+po
    if(vala.makahale.makaname!="-"):
        resu += vala.makahale.makaname+po
    if(vala.razahale.razaname!="-"):
        resu += vala.razahale.razaname+po
    if(vala.satahale.sataname!="-"):
        resu += vala.satahale.sataname
    return resu
