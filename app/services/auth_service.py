from itsdangerous import URLSafeTimedSerializer

def generate_password_reset_token(email: str) -> str:
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
    return serializer.dumps(email, salt="password-reset")

def verify_password_reset_token(token: str, max_age: int = 3600) -> Optional[str]:
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
    try:
        email = serializer.loads(
            token,
            salt="password-reset",
            max_age=max_age
        )
        return email
    except:
        return None