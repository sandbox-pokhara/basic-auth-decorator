# django-basic-auth-decorator

Basic auth decorator for Django.

## Installation

You can install the package via pip:

```
pip install django-basic-auth-decorator
```

## Usage

```python
from django_basic_auth_decorator.decorators import basic_auth

# Define your allowed credentials
CREDENTIALS = [
    ("admin", "adminpass"),
    ("user", "userpass"),
]

# Apply the decorator on a view function
@basic_auth(CREDENTIALS)
def my_view(request):
    ...

```

## License

This project is licensed under the terms of the MIT license.
