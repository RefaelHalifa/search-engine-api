# app/auth/routes.py
from fastapi import APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

from app.auth.jwt_handler import create_access_token
from app.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> dict[str, str]:
    """Authenticate the admin user and issue a JWT access token.

    Args:
        form_data: Username and password submitted via OAuth2 password flow.

    Returns:
        A dict with the access token and token type.

    Raises:
        HTTPException: 401 if the credentials don't match the configured admin user.
    """
    is_valid_user = (
        form_data.username == settings.admin_username
        and form_data.password == settings.admin_password
    )
    if not is_valid_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}