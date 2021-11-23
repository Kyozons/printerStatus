from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class BuscarForm(forms.Form):
    ingresar_fecha = forms.DateField(widget=DateInput)
