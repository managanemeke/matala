from django.db import models


class Hala(models.Model):
    deke = [
        {"type":"char","name":"halahale","title":"хна","max":255,"primary":True},
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
        return self.halahale


    @staticmethod
    def get_column_names():
        de = dict()
        for he in __class__.deke:
            de[he["name"]] = he["title"]
        return de
