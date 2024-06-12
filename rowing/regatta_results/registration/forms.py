#forms for registration
from django import forms
from django.contrib.auth.models import User
from .models import Profile

// registration form 
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput) 
    password2 = forms.CharField(widget=forms.PasswordInput, label="Please repeat password")
    user_type = forms.ChoiceField(choices=Profile.USER_TYPES) #this is WIP

    #this class is for fields to include in the field
    class Meta:
        model = User #This uses the built in User model
        fields = ("username", "first_name", "last_name", "email") #these are the fields I'll include
        help_texts = {
            "username": "", #to remove nonsense
        }

    #this is to make sure both passwords match
    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Your passwords do not match!")
        return cd["password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.set_password(self.cleaned_data["password"])
            user.save()
            Profile.objects.create(user=user, user_type=self.cleaned_data["user_type"])
        return user


