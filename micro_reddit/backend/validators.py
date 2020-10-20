from django.core.exceptions import ValidationError

def validate_password(string):
    if len(string) < 6 or len(string) > 12:
        raise ValidationError('Password must be 6-12 characters')
