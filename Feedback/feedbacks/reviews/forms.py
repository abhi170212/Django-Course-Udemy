from django import forms
from .models import Review 

# class ReviewForm(forms.Form):
#      user_name = forms.CharField(label="Your name",max_length=100,error_messages={
#           "required":"Your name must not be empty",
#           "max_length":"Please enter a shorter name!"
#      })
#      review_text=forms.CharField(label="Your Feedback",widget=forms.Textarea,max_length=200)
#      rating = forms.IntegerField(label="Your Rating",min_value=1,max_value=5)
     
class ReviewForm(forms.ModelForm):
     class Meta:
          model=Review
          fields="__all__" # ['text_fields_name','name_of_fields'], __all__
          # exclude=['jo nhi rakhna hai']
          labels={
               "user_name":"Your Name",
               "review_text":"Your Feedback",
               "rating":"Your rating",
          }
          error_messages={
               "user_name":{
                    "required":"Your name must not be empty",
                    "max_length":"Please enter a short name!"
               }
          }