from django.db import models


class Mara(models.Model):
    deke = [
        {"type":"char","name":"marahale","title":"хна","max":255,"primary":True},
        {"type":"char","name":"maraname","title":"мера","max":255},
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
        if(he["type"] == "neme"):
            lo[he["name"]] = models.ForeignKey(
                to=he["to"],
                to_field=he["name"],
                on_delete=models.CASCADE,
                verbose_name=he["title"],
                db_column=he["db_column"],
            )
    # 


    def __str__(self):
        return self.maraname


    @staticmethod
    def get_column_names():
        de = dict()
        for he in __class__.deke:
            de[he["name"]] = he["title"]
        return de


class Fara(models.Model):
    deke = [
        {"type":"char","name":"farahale","title":"хна","max":255,"primary":True},
        {"type":"char","name":"faraname","title":"форма","max":255},
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
        if(he["type"] == "neme"):
            lo[he["name"]] = models.ForeignKey(
                to=he["to"],
                to_field=he["name"],
                on_delete=models.CASCADE,
                verbose_name=he["title"],
                db_column=he["db_column"],
            )
    # 


    def __str__(self):
        return self.faraname


    @staticmethod
    def get_column_names():
        de = dict()
        for he in __class__.deke:
            de[he["name"]] = he["title"]
        return de


class Maka(models.Model):
    deke = [
        {"type":"char","name":"makahale","title":"хна","max":255,"primary":True},
        {"type":"char","name":"makaname","title":"марка","max":255},
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
        if(he["type"] == "neme"):
            lo[he["name"]] = models.ForeignKey(
                to=he["to"],
                to_field=he["name"],
                on_delete=models.CASCADE,
                verbose_name=he["title"],
                db_column=he["db_column"],
            )
    # 


    def __str__(self):
        return self.makaname


    @staticmethod
    def get_column_names():
        de = dict()
        for he in __class__.deke:
            de[he["name"]] = he["title"]
        return de


class Raza(models.Model):
    deke = [
        {"type":"char","name":"razahale","title":"хна","max":255,"primary":True},
        {"type":"char","name":"razaname","title":"размеры","max":255},
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
        if(he["type"] == "neme"):
            lo[he["name"]] = models.ForeignKey(
                to=he["to"],
                to_field=he["name"],
                on_delete=models.CASCADE,
                verbose_name=he["title"],
                db_column=he["db_column"],
            )
    # 


    def __str__(self):
        return self.razaname


    @staticmethod
    def get_column_names():
        de = dict()
        for he in __class__.deke:
            de[he["name"]] = he["title"]
        return de


class Sata(models.Model):
    deke = [
        {"type":"char","name":"satahale","title":"хна","max":255,"primary":True},
        {"type":"char","name":"sataname","title":"стандарт","max":255},
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
        if(he["type"] == "neme"):
            lo[he["name"]] = models.ForeignKey(
                to=he["to"],
                to_field=he["name"],
                on_delete=models.CASCADE,
                verbose_name=he["title"],
                db_column=he["db_column"],
            )
    # 


    def __str__(self):
        return self.sataname


    @staticmethod
    def get_column_names():
        de = dict()
        for he in __class__.deke:
            de[he["name"]] = he["title"]
        return de


class Mata(models.Model):
    deke = [
        {"type":"char","name":"matahale","title":"хна","max":255,"primary":True},
        {"type":"char","name":"mataname","title":"материал","max":255},
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
        if(he["type"] == "neme"):
            lo[he["name"]] = models.ForeignKey(
                to=he["to"],
                to_field=he["name"],
                on_delete=models.CASCADE,
                verbose_name=he["title"],
                db_column=he["db_column"],
            )
    # 


    def __str__(self):
        return self.mataname


    @staticmethod
    def get_column_names():
        de = dict()
        for he in __class__.deke:
            de[he["name"]] = he["title"]
        return de


class Teve(models.Model):
    deke = [
        {"type":"char","name":"tevehale","title":"тэвалюта","max":255,"primary":True},
        {"type":"neme","name":"marahale","title":"мера","to":"Mara","db_column":"marahale"},
        {"type":"neme","name":"farahale","title":"форма","to":"Fara","db_column":"farahale"},
        {"type":"neme","name":"makahale","title":"марка","to":"Maka","db_column":"makahale"},
        {"type":"neme","name":"razahale","title":"размеры","to":"Raza","db_column":"razahale"},
        {"type":"neme","name":"satahale","title":"стандарт","to":"Sata","db_column":"satahale"},
        {"type":"neme","name":"matahale","title":"материал","to":"Mata","db_column":"matahale"},
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
        if(he["type"] == "neme"):
            lo[he["name"]] = models.ForeignKey(
                to=he["to"],
                to_field=he["name"],
                on_delete=models.CASCADE,
                verbose_name=he["title"],
                db_column=he["db_column"],
            )
    # 
    '''
    class Meta:
        ordering = ['tevehale']
    '''


    def __str__(self):
        return self.tevehale


    @staticmethod
    def get_column_names():
        de = dict()
        for he in __class__.deke:
            de[he["name"]] = he["title"]
        return de


class Sava(models.Model):
    deke = [
        {"type":"char","name":"savahale","title":"хна","max":255,"primary":True},
        {"type":"char","name":"savaname","title":"сэвалюта","max":255},
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
        if(he["type"] == "neme"):
            lo[he["name"]] = models.ForeignKey(
                to=he["to"],
                to_field=he["name"],
                on_delete=models.CASCADE,
                verbose_name=he["title"],
                db_column=he["db_column"],
            )
    # 


    def __str__(self):
        return self.savaname


    @staticmethod
    def get_column_names():
        de = dict()
        for he in __class__.deke:
            de[he["name"]] = he["title"]
        return de


class Solo(models.Model):
    deke = [
        {"type":"char","name":"solohale","title":"сэляви","max":255,"primary":True},
        {"type":"neme","name":"savahale","title":"сэвалюта","to":"Sava","db_column":"savahale"},
        {"type":"neme","name":"tevehale","title":"тэвалюта","to":"Teve","db_column":"tevehale"},
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
        if(he["type"] == "neme"):
            lo[he["name"]] = models.ForeignKey(
                to=he["to"],
                to_field=he["name"],
                on_delete=models.CASCADE,
                verbose_name=he["title"],
                db_column=he["db_column"],
            )
    # 


    def __str__(self):
        return self.solohale


    @staticmethod
    def get_column_names():
        de = dict()
        for he in __class__.deke:
            de[he["name"]] = he["title"]
        return de

