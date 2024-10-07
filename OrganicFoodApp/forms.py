from django import forms
from . models import Subscription,Contact


#SubscriptionsForm
class SubscriptionsForm(forms.Form):
      email = forms.EmailField(required=True, label='Your Email')
      
      class Meta:
          method = Subscription
          fields =('email',)
          
class ContactForm(forms.Form):
    name=forms.CharField(max_length=200,required=True,label='Your Name')
    email = forms.EmailField(required=True, label='Your Email')
    subject=forms.CharField(max_length=300,required=True,label="Subject")
    message=forms.CharField(widget=forms.Textarea,required=True,label='Message')


    
