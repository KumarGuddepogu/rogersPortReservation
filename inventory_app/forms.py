from django import forms
from django.forms import ModelForm

from .models import *


class CgwReservationForm(ModelForm):
    Router_Ports = forms.ModelChoiceField(queryset=CGW.objects.filter(Port_Status='Available'))
    class Meta:
        model = CgwReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Ports',
        ]

        widgets = {
            'target_date': forms.DateInput(format=('%m/%d/%Y'),
                                           attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                  'type': 'date'}),
            'order_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'})
        }


class CsdeReservationForm(ModelForm):
    Router_Ports = forms.ModelChoiceField(queryset=cSDE.objects.filter(Port_Status='Available'))
    class Meta:
        model = CsdeReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Ports'
        ]
        widgets = {
            'target_date': forms.DateInput(format=('%m/%d/%Y'),
                                           attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                  'type': 'date'}),
            'order_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'})
        }


class DgwReservationForm(ModelForm):
    Router_Ports = forms.ModelChoiceField(queryset=DGW.objects.filter(Port_Status='Available'))
    class Meta:
        model = DgwReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Ports',
        ]
        widgets = {
            'target_date': forms.DateInput(format=('%m/%d/%Y'),
                                           attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                  'type': 'date'}),
            'order_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'})
        }


class DsdeReservationForm(ModelForm):
    Router_Ports = forms.ModelChoiceField(queryset=dSDE.objects.filter(Port_Status='Available'))
    class Meta:
        model = DsdeReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Ports',
        ]
        widgets = {
            'target_date': forms.DateInput(format=('%m/%d/%Y'),
                                           attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                  'type': 'date'}),
            'order_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'})
        }


class IgwReservationForm(ModelForm):
    Router_Ports = forms.ModelChoiceField(queryset=IGW.objects.filter(Port_Status='Available'))
    class Meta:
        model = IgwReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Ports',
        ]
        widgets = {
            'target_date': forms.DateInput(format=('%m/%d/%Y'),
                                           attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                  'type': 'date'}),
            'order_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'})
        }


class MxReservationForm(ModelForm):
    Router_Ports = forms.ModelChoiceField(queryset=MX.objects.filter(Port_Status='Available'))
    class Meta:
        model = MxReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Ports',
        ]
        widgets = {
            'target_date': forms.DateInput(format=('%m/%d/%Y'),
                                           attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                  'type': 'date'}),
            'order_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'})
        }


class SigrReservationForm(ModelForm):
    Router_Ports = forms.ModelChoiceField(queryset=SIGR.objects.filter(Port_Status='Available'))
    class Meta:
        model = SigrReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Ports',
        ]
        widgets = {
            'target_date': forms.DateInput(format=('%m/%d/%Y'),
                                           attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                  'type': 'date'}),
            'order_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'})
        }


class WasReservationForm(ModelForm):
    Router_Ports = forms.ModelChoiceField(queryset=WAS.objects.filter(Port_Status='Available'))
    class Meta:
        model = WasReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Ports',
        ]
        widgets = {
            'target_date': forms.DateInput(format=('%m/%d/%Y'),
                                           attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                  'type': 'date'}),
            'order_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'})
        }


class WgrReservationForm(ModelForm):
    Router_Ports = forms.ModelChoiceField(queryset=WGR.objects.filter(Port_Status='Available'))
    class Meta:
        model = WgrReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Ports'
        ]
        widgets = {
            'target_date': forms.DateInput(format=('%m/%d/%Y'),
                                           attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                  'type': 'date'}),
            'order_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'})
        }


class WprReservationForm(ModelForm):
    Router_Ports = forms.ModelChoiceField(queryset=WPR.objects.filter(Port_Status='Available'))
    class Meta:
        model = WprReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Ports',
        ]
        widgets = {
            'target_date': forms.DateInput(format=('%m/%d/%Y'),
                                           attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                  'type': 'date'}),
            'order_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'})
        }


class WrsReservationForm(ModelForm):
    Router_Ports = forms.ModelChoiceField(queryset=WRS.objects.filter(Port_Status='Available'))

    class Meta:
        model = WrsReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Ports',
        ]
        widgets = {
            'target_date': forms.DateInput(format=('%m/%d/%Y'),
                                           attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                  'type': 'date'}),
            'order_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'})
        }
