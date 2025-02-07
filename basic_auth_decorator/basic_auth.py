import base64
from functools import wraps
from typing import Any
from typing import Callable
from typing import TypeVar

from django.http import HttpRequest
from django.http import HttpResponse

F = TypeVar("F", bound=Callable[..., Any])


def basic_auth_decorator(credentials: list[tuple[str, str]]):
    def BasicAuth(view_func: F) -> F:
        @wraps(view_func)
        def _wrapped_view(
            request: HttpRequest, *args: Any, **kwargs: Any
        ) -> HttpResponse:
            if "HTTP_AUTHORIZATION" in request.META:
                auth = request.META["HTTP_AUTHORIZATION"].split()
                if len(auth) == 2 and auth[0].lower() == "basic":
                    try:
                        username, password = (
                            base64.b64decode(auth[1])
                            .decode("utf-8")
                            .split(":", 1)
                        )
                        if (username, password) in credentials:
                            return view_func(request, *args, **kwargs)
                    except (ValueError, UnicodeDecodeError):
                        pass

            response = HttpResponse(status=401)
            response["WWW-Authenticate"] = 'Basic realm="API Docs"'
            return response

        return _wrapped_view  # type: ignore

    return BasicAuth
