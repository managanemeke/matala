from django.db import models
from metele.functions import generate_hale
from perso.models import *
from order.models import *


class Suvu(models.Model):
    deke = [
        {"type":"char","name":"suvuhale","title":"связка","max":255,"primary":True},
        {"type":"neme","name":"perehale","title":"персона","to":"perso.Pere","to_field":"perehale","db_column":"perehale","related_name":generate_hale(4)},
        {"type":"neme","name":"zovohalebe","title":"зазаявка","to":"order.Zovo","to_field":"zovohale","db_column":"zovohalebe","related_name":generate_hale(4)},
        {"type":"neme","name":"zovohalepe","title":"отзаявка","to":"order.Zovo","to_field":"zovohale","db_column":"zovohalepe","related_name":generate_hale(4)},
    ]
    lo = locals()
    for he in deke:
        if(he["type"] == "char"):
            if("primary" in set(he.keys())):
                if(he["primary"] == True):
                    lo[he["name"]] = models.CharField(
                        he["title"],
                        max_length=he["max"],
                        primary_key=True
                    )
            else:
                lo[he["name"]] = models.CharField(
                    he["title"],
                    max_length=he["max"],
                    unique=True
                )
        if(he["type"] == "text"):
            lo[he["name"]] = models.TextField(he["title"], unique=True)
        if(he["type"] == "deci"):
            lo[he["name"]] = models.DecimalField(
                he["title"],
                max_digits=he["max_digits"],
                decimal_places=he["decimal_places"],
            )
        if(he["type"] == "neme"):
            lo[he["name"]] = models.ForeignKey(
                to=he["to"],
                to_field=he["to_field"],
                on_delete=models.CASCADE,
                verbose_name=he["title"],
                db_column=he["db_column"],
                related_name=he["related_name"],
            )
    # 


    def __str__(self):
        return self.suvuhale


    @staticmethod
    def get_column_names():
        de = dict()
        for he in __class__.deke:
            de[he["name"]] = he["title"]
        return de
