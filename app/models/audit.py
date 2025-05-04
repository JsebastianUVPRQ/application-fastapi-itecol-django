class AuditLog(BaseModel):
    __tablename__ = "audit_logs"
    
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String(100), nullable=False)
    endpoint = Column(String(255))
    parameters = Column(JSON)
    ip_address = Column(String(45))
    user_agent = Column(Text)