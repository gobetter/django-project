from django import forms
from .models import Destination

class DestinationModelForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    # email = forms.EmailField()
    content = forms.CharField(
            required=False,
            widget=forms.Textarea(
                attrs={
                    "placeholder": "Your content",
                    "class": "new-class-name two",
                    "id": "my-id-for-textarea",
                    "rows": 20,
                    "cols": 120
                    }
                )
            )

    class Meta:
        model = Destination
        fields = [
                'title',
                'content',
                'active'
                ]

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if title.lower() == 'abc':
    #         raise forms.ValidationError("This is not a valid title")
    #     return title

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "CFE" in title:
    #         raise forms.ValidationError("This is not a valid title")
    #     if not "news" in title:
    #         raise forms.ValidationError("This is not a valid title")
    #     return title

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("This is not a valid email")
    #     return email
