from django.contrib.admin import forms


class CustomUserSignUpForm(forms.ModelForm):
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(CustomUserSignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user