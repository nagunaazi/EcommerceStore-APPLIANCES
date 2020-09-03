from django import forms
from mainapp.models import ProductModel

class ProductForm(forms.ModelForm):
    product_no = forms.IntegerField(min_value=101)
    class Meta:
        model = ProductModel
        fields = "__all__"

    def clean_price(self):
        price = self.cleaned_data["product_price"]
        if price >= 1000:
            return price
        else:
            raise forms.ValidationError("Price Minimum of RS:1000 are ALLOWED")
