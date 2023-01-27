from django import forms
from django.forms import ModelForm

from .models import *


class CgwReservationForm(ModelForm):
    class Meta:
        model = CgwReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Port_id',
        ]

        widgets = {
            'Router_Port_id': forms.SelectMultiple(),
            'target_date': forms.DateInput(format=('%m/%d/%Y'),
                                           attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                  'type': 'date'}),
            'order_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'})
        }



class CsdeReservationForm(ModelForm):
    class Meta:
        model = CsdeReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Port_id'
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
    class Meta:
        model = DgwReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Port_id',
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
    class Meta:
        model = DsdeReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Port_id',
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
    class Meta:
        model = IgwReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Port_id',
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
    class Meta:
        model = MxReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Port_id',
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
    class Meta:
        model = SigrReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Port_id',
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
    class Meta:
        model = WasReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Port_id',
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
    class Meta:
        model = WgrReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Port_id'
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
    class Meta:
        model = WprReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Port_id',
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
    class Meta:
        model = WrsReservations
        fields = [
            'user',
            'project_number',
            'project_name',
            'target_date',
            'order_date',
            'Router_Port_id',
        ]
        widgets = {
            'target_date': forms.DateInput(format=('%m/%d/%Y'),
                                           attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                  'type': 'date'}),
            'order_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'})
        }
