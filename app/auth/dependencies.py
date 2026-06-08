# app/auth/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.auth.jwt_handler import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    """Resolve the authenticated username from a Bearer token.

    Args:
        token: The JWT extracted from the Authorization header by FastAPI.

    Returns:
        The username encoded in the token's "sub" claim.

    Raises:
        HTTPException: 401 if the token is missing, invalid, or expired.
    """
    credentials_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_access_token(token)
    if payload is None:
        raise credentials_error

    username = payload.get("sub")
    if username is None:
        raise credentials_error

    return username