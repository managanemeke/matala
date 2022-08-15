from django import forms

from .models import *

from django.db.models import Q

class TeveForm(forms.ModelForm):
    class Meta:
        model = Teve
        fields = ('marahale','farahale','makahale','razahale','satahale','matahale',)
        widgets = {
            'marahale': forms.Select(attrs={'class': 'form-control',}),
            'farahale': forms.Select(attrs={'class': 'form-control',}),
            'makahale': forms.Select(attrs={'class': 'form-control',}),
            'razahale': forms.Select(attrs={'class': 'form-control',}),
            'satahale': forms.Select(attrs={'class': 'form-control',}),
            'matahale': forms.Select(attrs={'class': 'form-control',}),
        }


class MaraForm(forms.ModelForm):

    class Meta:
        model = Mara
        fields = ('maraname',)
        widgets = {
            'maraname': forms.TextInput(attrs={'class': 'form-control',}),
        }


class FaraForm(forms.ModelForm):

    class Meta:
        model = Fara
        fields = ('faraname',)
        widgets = {
            'faraname': forms.TextInput(attrs={'class': 'form-control',}),
        }


class MakaForm(forms.ModelForm):

    class Meta:
        model = Maka
        fields = ('makaname',)
        widgets = {
            'makaname': forms.TextInput(attrs={'class': 'form-control',}),
        }


class RazaForm(forms.ModelForm):

    class Meta:
        model = Raza
        fields = ('razaname',)
        widgets = {
            'razaname': forms.TextInput(attrs={
                'class': 'form-control',
                'pattern': '^([0-9,x]|БТ|НД)+$',
            }),
        }


class SataForm(forms.ModelForm):

    class Meta:
        model = Sata
        fields = ('sataname',)
        widgets = {
            'sataname': forms.TextInput(attrs={'class': 'form-control',}),
        }


class MataForm(forms.ModelForm):

    class Meta:
        model = Mata
        fields = ('mataname',)
        widgets = {
            'mataname': forms.TextInput(attrs={'class': 'form-control',}),
        }


class SavaForm(forms.ModelForm):

    class Meta:
        model = Sava
        fields = ('savaname',)
        widgets = {
            'savaname': forms.TextInput(attrs={'class': 'form-control',}),
        }


class SoloForm(forms.ModelForm):

    class Meta:
        model = Solo
        fields = ('savahale','tevehale',)
        widgets = {
            'savahale': forms.Select(attrs={'class': 'form-control',}),
            'tevehale': forms.Select(attrs={'class': 'form-control',}),
        }
    def __init__(self, *args, **kwargs):
        super(SoloForm, self).__init__(*args, **kwargs)
        self.fields['tevehale'].queryset = self.fields['tevehale'].queryset.order_by('tevehale')


class SoloSmartForm(forms.ModelForm):

    class Meta:
        model = Solo
        fields = ('savahale','tevehale',)
        widgets = {
            'savahale': forms.Select(attrs={'class': 'form-control',}),
            'tevehale': forms.Select(attrs={'class': 'form-control',}),
        }
    def __init__(self, *args, **kwargs):
        super(SoloSmartForm, self).__init__(*args, **kwargs)
        #
        #
        benele = Solo.objects.all()
        bese = set(benele.values_list('savahale'))
        bala = [be[0] for be in bese]
        #
        #satara = "\n".join(list(bala))
        #open("savas.txt","w").write(satara)
        #
        mele = Sava.objects.all()
        for me in bala:
            mele = mele.filter(~Q(savahale = me))
        self.fields['savahale'].queryset = mele
        #
        #
        '''
        benele = Solo.objects.all()
        bese = set(benele.values_list('tevehale'))
        bala = [be[0] for be in bese]
        #
        #satara = "\n".join(list(bala))
        #open("savas.txt","w").write(satara)
        #
        mele = Teve.objects.all()
        for me in bala:
            mele = mele.filter(~Q(tevehale = me))
        self.fields['tevehale'].queryset = mele
        '''
        #
        self.fields['tevehale'].queryset = self.fields['tevehale'].queryset.order_by('tevehale')
