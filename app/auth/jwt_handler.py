# app/auth/jwt_handler.py
from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt

from app.config import settings

ALGORITHM = "HS256"


def create_access_token(data: dict) -> str:
    """Create a signed JWT containing the given claims plus an expiry.

    Args:
        data: Claims to encode into the token (e.g. {"sub": username}).

    Returns:
        The encoded JWT as a string.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode["exp"] = expire
    return jwt.encode(to_encode, settings.secret_key, algorithm=ALGORITHM)


def decode_access_token(token: str) -> dict | None:
    """Decode and verify a JWT, returning its claims.

    Args:
        token: The encoded JWT string.

    Returns:
        The decoded claims if the token is valid, None if invalid or expired.
    """
    try:
        return jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
    except JWTError:
        return None