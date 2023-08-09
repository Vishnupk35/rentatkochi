from django.forms import ModelForm
from customer.models import Address,Contact

class AddressForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category_name'].widget.attrs.update({
            'onkeydown':"return /[a-z, space]/i.test(event.key)",'type':"text", 'placeholder':"", 'name':"category_name", 'id':"category_name", 'required':"required", 'autofocus':"autofocus", 'autocapitalize':"none", 'class':"form-control"})
    
    class Meta:
        model=Address
        fields="__all__"

class ContactForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'type':'text','class':'form-control','placeholder':'Your Name'})
        self.fields['email'].widget.attrs.update({
            'type':'email','class':'form-control','placeholder':'Your Email'})
        self.fields['subject'].widget.attrs.update({
            'type':'text','class':'form-control','placeholder':'Subject'})
        self.fields['message'].widget.attrs.update({
            'type':'text','class':'form-control','placeholder':'Message',"cols":"30",'rows':"7"})
    
    class Meta:
        model=Contact
        exclude=('status',)