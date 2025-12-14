# Middlewares/jwt_logging_middleware.py
from typing import Optional

from fastapi import Request
from jose import jwt, JWTError

# Ye values tumhare auth_service / auth_routes ke barabar honi chahiye
SECRET_KEY = "super_secret_key"
ALGORITHM = "HS256"


def _get_bearer_token(request: Request) -> Optional[str]:
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return None

    parts = auth_header.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        return None

    return parts[1]


async def jwt_logging_middleware(request: Request, call_next):
    """
    Har request ke liye:
    - Authorization header se JWT token read karega
    - Token decode karke 'sub' (email) nikaalega
    - Console me user + path log karega
    """
    token = _get_bearer_token(request)
    user_email: Optional[str] = None

    if token:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_email = payload.get("sub")
        except JWTError:
            # Invalid token ho to sirf log, decision get_current_user lega
            user_email = None

    method = request.method
    path = request.url.path

    if user_email:
        print(f"[JWT] {method} {path} by {user_email}")
    else:
        print(f"[JWT] {method} {path} (no valid user)")

    response = await call_next(request)
    return response
