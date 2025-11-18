from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "brand", "thumbnail", "price", "rating", "description"]

    def clean_title(self):
        title = self.cleaned_data["name"]
        return strip_tags(title)

    def clean_content(self):
        content = self.cleaned_data["description"]
        return strip_tags(content)