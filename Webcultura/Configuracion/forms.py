from django.forms import ModelForm
from.models import Pagina

class PaginaForm(ModelForm):
    class Meta:
        model = Pagina
        fields = ['titulo','descripcion','slug','image']