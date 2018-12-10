from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ContactForm(forms.Form):
    short_input = forms.CharField(widget=forms.Textarea)
