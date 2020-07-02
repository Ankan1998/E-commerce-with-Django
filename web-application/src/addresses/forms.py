from django import forms

from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            #'billing_profile',
            #'address_type',
            'address_line_1',
            'address_line_2',
            'city',
            'country',
            'state',
            'postal_code'
        ]

    address_line_1 = forms.CharField(label='         ',widget=forms.TextInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "Address 1"
                    }
                    )
            )
    address_line_2 = forms.CharField(label='         ',widget=forms.TextInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "Address 2"
                    }
                    )
            )
    city = forms.CharField(label='         ',widget=forms.TextInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "City"
                    }
                    )
            )
    country = forms.CharField(label='         ',widget=forms.TextInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "Country"
                    }
                    )
            )
    state = forms.CharField(label='         ',widget=forms.TextInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "State"
                    }
                    )
            )
    postal_code = forms.IntegerField(label='         ',widget=forms.TextInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "Postal Code"
                    }
                    )
            )

