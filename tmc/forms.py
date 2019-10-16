from django import forms
from tmc.models import Tmc



class TmcForm(forms.ModelForm):
    """Formulario para la TMC
    
    Arguments:
        forms {Object}
    """

    class Meta:
        model = Tmc
        fields = ('plazo', 'monto', 'fecha_tmc')

    def __init__(self, *args, **kwargs):
        super(TmcForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': self.fields[field].label 
            }) 
            self.fields[field].label = ''
