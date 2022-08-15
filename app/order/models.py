from django.db import models
from metele.functions import generate_hale
from perso.models import *
from curcy.models import *


class Zovo(models.Model):
    deke = [
        {"type":"char","name":"zovohale","title":"заявка","max":255,"primary":True},
        {"type":"neme","name":"perehale","title":"персона","to":"perso.Pere","to_field":"perehale","db_column":"perehale","related_name":generate_hale(4)},
        {"type":"neme","name":"tevehalebe","title":"заберу","to":"curcy.Teve","to_field":"tevehale","db_column":"tevehalebe","related_name":generate_hale(4)},
        {"type":"deci","name":"zovokalebe","title":"заколичество","max_digits":20,"decimal_places":10},
        {"type":"neme","name":"tevehalepe","title":"отдам","to":"curcy.Teve","to_field":"tevehale","db_column":"tevehalepe","related_name":generate_hale(4)},
        {"type":"deci","name":"zovokalepe","title":"отколичество","max_digits":20,"decimal_places":10},
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
        return self.zovohale


    @staticmethod
    def get_column_names():
        de = dict()
        for he in __class__.deke:
            de[he["name"]] = he["title"]
        return de
