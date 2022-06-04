from django import forms
from .models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','mobile','msg']
        #labels={'name':'Name','email':'Email','mobile':'Mobile','msg':'Message'}


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'