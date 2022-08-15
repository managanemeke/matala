from django.db import models


class Fama(models.Model):
    deke = [
        {"type":"char","name":"famahale","title":"хна","max":255,"primary":True},
        {"type":"char","name":"famaname","title":"фирма","max":255},
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
        return self.famaname


    @staticmethod
    def get_column_names():
        de = dict()
        for he in __class__.deke:
            de[he["name"]] = he["title"]
        return de


class Tafa(models.Model):
    deke = [
        {"type":"char","name":"tafahale","title":"хна","max":255,"primary":True},
        {"type":"char","name":"tafaname","title":"телефон","max":255},
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
        return self.tafaname


    @staticmethod
    def get_column_names():
        de = dict()
        for he in __class__.deke:
            de[he["name"]] = he["title"]
        return de


class Mala(models.Model):
    deke = [
        {"type":"char","name":"malahale","title":"хна","max":255,"primary":True},
        {"type":"char","name":"malaname","title":"email","max":255},
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
        return self.malaname


    @staticmethod
    def get_column_names():
        de = dict()
        for he in __class__.deke:
            de[he["name"]] = he["title"]
        return de


class Hara(models.Model):
    deke = [
        {"type":"char","name":"harahale","title":"хна","max":255,"primary":True},
        {"type":"text","name":"haraname","title":"url"},
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
        return self.haraname


    @staticmethod
    def get_column_names():
        de = dict()
        for he in __class__.deke:
            de[he["name"]] = he["title"]
        return de


class Pere(models.Model):
    deke = [
        {"type":"char","name":"perehale","title":"персона","max":255,"primary":True},
        {"type":"neme","name":"famahale","title":"фирма","to":"Fama","db_column":"famahale"},
        {"type":"neme","name":"tafahale","title":"телефон","to":"Tafa","db_column":"tafahale"},
        {"type":"neme","name":"malahale","title":"email","to":"Mala","db_column":"malahale"},
        {"type":"neme","name":"harahale","title":"url","to":"Hara","db_column":"harahale"},
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
        return self.perehale


    @staticmethod
    def get_column_names():
        de = dict()
        for he in __class__.deke:
            de[he["name"]] = he["title"]
        return de

    # kodopo = models.CharField('код подразделения', max_length=255)

    # perehala = models.CharField("хна персона",max_length=255, primary_key=True)
    # famahala = models.ForeignKey(to="Fama",to_field='famahala',on_delete=models.CASCADE,verbose_name="хна фирма",db_column="famahala")

    # full_text = models.TextField('статья')
    # date = models.DateTimeField('дата публикации')
