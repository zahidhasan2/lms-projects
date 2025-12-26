from django.contrib.auth.tokens import PasswordResetTokenGenerator

class UserResetTokenGenerator(PasswordResetTokenGenerator):
    pass

reset_token_generator = UserResetTokenGenerator()
