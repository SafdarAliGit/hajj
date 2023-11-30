from django import forms

from package_making.models import PackageHotelItem


class PackageHotelItemForm(forms.ModelForm):
    class Meta:
        model = PackageHotelItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['meal'].widget.attrs['class'] = "meal"
        self.fields['cost'].widget.attrs['class'] = "cost"