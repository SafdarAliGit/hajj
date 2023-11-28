from django import forms

from hajj_application.models import HajjApplication


class HajjApplicationForm(forms.ModelForm):
    class Meta:
        model = HajjApplication
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'present_postal_address': forms.Textarea(attrs={'rows': 4}),
            'date_of_expiry': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(HajjApplicationForm, self).__init__(*args, **kwargs)

        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = "form-control"

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        obj = super(HajjApplicationForm, self).save(*args, **kwargs)
        if self.request:
            obj.user = self.request.user
            obj.save()
        return obj
