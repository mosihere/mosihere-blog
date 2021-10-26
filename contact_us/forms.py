from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'input100', 'id':'name', 'placeholder':'First name'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'input100', 'id':'name', 'placeholder':'Last name'}))
    email_address = forms.EmailField(max_length=150, required=True, widget=forms.EmailInput(attrs={'class':'input100', 'id':'email', 'placeholder':'Email'}))
    message = forms.CharField(max_length=2000, required=True, widget=forms.Textarea(attrs={'class':'input100', 'id':'message', 'placeholder':'Your message...'}))