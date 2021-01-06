from django import forms
from . import models

class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email") # fetch the data send by a user
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email) # if user does exist
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is incorrect"))
        except models.User.DoesNotExist: # otherwise
            self.add_error("email", forms.ValidationError("User does not exist"))