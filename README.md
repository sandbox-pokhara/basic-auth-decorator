# basic-auth-decorator

Basic auth decorator for Django Ninja.

## Installation

You can install the package via pip:

```
pip install basic-auth-decorator
```

## Usage

```python
from basic_auth_decorator import basic_auth_decorator
api = NinjaAPI()

# Define your allowed credentials
CREDENTIALS = [
    ("admin", "adminpass"),
    ("user", "userpass"),
]

# Apply the decorator on a view function
@api.get("/protected")
@basic_auth_decorator(CREDENTIALS)
def protected_endpoint(request):
    return JsonResponse({"message": "You have access!"})

```

## License

This project is licensed under the terms of the MIT license.
