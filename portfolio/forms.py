from django import forms
from portfolio.models import send_a_query, newsletteremail


class SendQueryForm(forms.ModelForm):
    class Meta:
        model = send_a_query
        fields = ['name', 'email', 'mobile', 'query', 'query_answered']
        
        
class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = newsletteremail
        fields = ['email']