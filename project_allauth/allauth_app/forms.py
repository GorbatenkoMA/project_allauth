from allauth.account.forms import LoginForm


class MyCustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):
        return super().login(*args, **kwargs)
