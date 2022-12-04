from django.core import exceptions


def validate_letters_only(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Name must contain only letters!')


def validate_phone_number(value):
    for index, ch in enumerate(value):
        if index == 0 and ch != '+' and ch != '0':
            raise exceptions.ValidationError('Phone number must begin with "+" or "0"!')
        if index > 0 and not ch.isnumeric():
            raise exceptions.ValidationError('Phone number must contain only "+" and numeric symbols!')


def validate_file_size(image_object):
    if image_object.size > 5242880:
        raise exceptions.ValidationError('The maximum filesize that can be uploaded is 5Mb!')


def validate_strings_number(value):
    if not 4 <= value <= 12:
        raise exceptions.ValidationError('The strings number must be between 4 and 12!')
