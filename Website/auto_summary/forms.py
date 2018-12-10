from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ShortTextForm(forms.Form):
    short_input = forms.CharField(widget=forms.Textarea(
        attrs={'cols': '30', 'rows': '6', 'placeholder': 'If you cannot get satisfying result, maybe you are not entering meaningful sentences.', 'required': True}), min_length=400, max_length=3000)
