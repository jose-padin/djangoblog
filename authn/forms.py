from pprint import PrettyPrinter

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    UsernameField
)

print = PrettyPrinter(indent=4).pprint
User = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("username", "email", "password1", "password2")
        field_classes = {"username": UsernameField}
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].required = True