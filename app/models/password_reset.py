class PasswordResetToken(BaseModel):
    __tablename__ = "password_reset_tokens"
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    token = Column(String(255), unique=True, index=True)
    expires_at = Column(DateTime, nullable=False)
    used = Column(Boolean, default=False)