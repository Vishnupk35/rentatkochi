from django.forms import ModelForm
from customer.models import Car,CarImage,CarFeature

class CarForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'type':'text','id':'nameLarge','class':'form-control','placeholder':'Enter Name','required':'required'
        })
        self.fields['brand'].widget.attrs.update({
            'type':'text','id':'nameLarge','class':'form-control','placeholder':'Enter brand Name','required':'required'
        })
        self.fields['image'].widget.attrs.update({
            'type':'file','id':'car-image','class':'form-control','required':'required'
        })
        self.fields['description'].widget.attrs.update({
            'type':'text','id':'description','class':'form-control','required':'required','rows':'3'
        })
        self.fields['capacity'].widget.attrs.update({
            'type':'number','id':'car-capacity','class':'form-control','required':'required','placeholder':'Enter seating capacity'
        })
        self.fields['color'].widget.attrs.update({
            'type':'text','id':'car-color','class':'form-control','required':'required','placeholder':'Color of the car'
        })
        self.fields['price'].widget.attrs.update({
            'type':'number','id':'car-price','class':'form-control','required':'required','placeholder':'Enter per day rent'
        })
        self.fields['transmission'].widget.attrs.update({
            'type':'text','id':'car-transmission','class':'form-control','required':'required'
        })
        self.fields['mileage'].widget.attrs.update({
            'type':'number','id':'car-mileage','class':'form-control','required':'required','placeholder':'Mileage of the vehicle'
        })
        self.fields['fuel'].widget.attrs.update({
            'type':'text','id':'car-fuel','class':'form-control','required':'required','placeholder':'Fuel of the vehicle'
        })
        self.fields['status'].widget.attrs.update({
            'type':'text','id':'car-status','class':'form-control','required':'required'
        })
        self.fields['features'].widget.attrs.update({
            'type':'text','id':'car-features','class':'form-control',
        })
    class Meta:
        model = Car
        exclude=('created',)

class CarImageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car'].widget.attrs.update({
            'type':'text','id':'nameLarge','class':'form-control','required':'required'
        })
        self.fields['image'].widget.attrs.update({
            'type':'file','id':'car-image','class':'form-control','required':'required'
        })
    class Meta:
        model=CarImage
        exclude=('created','status')

class CarFeatureForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'type':'text','id':'feature-name','class':'form-control','required':'required','placeholder':'Feature Name'
        })
    class Meta:
        model=CarFeature
        exclude=("status",)