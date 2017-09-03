from django import forms
from .models import *

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()


class OrderDetailsForm(forms.ModelForm):

    class Meta:
        model = User
        exclude = ('is_admin', 'is_active', 'is_superuser', 'last_login', 'user_permissions', 'groups', 'date_joined', 'is_staff')