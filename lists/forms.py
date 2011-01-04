import datetime
from django import forms

class ListCreateForm(forms.Form):
    date = forms.DateField(initial=datetime.date.today())
    from_date = forms.DateField(initial=datetime.date.today())
    to_date = forms.DateField(initial=datetime.date.today()+datetime.timedelta(days=7))
    override = forms.CharField(widget=forms.widgets.HiddenInput(), required=False)

    def clean(self):
        fro = self.cleaned_data.get('from_date')
        to = self.cleaned_data.get('to_date')

        if fro and to and fro > to:
            raise forms.ValidationError('Invalid range')

        return self.cleaned_data
