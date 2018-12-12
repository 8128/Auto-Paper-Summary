from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ShortInputForm(forms.Form):
    short_input = forms.CharField(widget=forms.Textarea(
        attrs={'cols': '30', 'rows': '8',
               'placeholder': 'If you cannot get satisfying result, maybe you are not entering meaningful sentences.',
               'required': True}), min_length=400, max_length=3000)


class ContactForm(forms.Form):
    user_name = forms.CharField(required=True, max_length=50)
    user_email = forms.EmailField(required=True)
    user_message = forms.CharField(widget=forms.Textarea(attrs={'rows': '6'}), required=True )
