from sqlalchemy import event
from models.audit import AuditLog

def audit_listener(mapper, connection, target):
    if hasattr(target, '__audit_ignore__'):
        return
    
    db_session = connection.session
    current_user = get_current_user_from_context()
    
    log = AuditLog(
        user_id=current_user.id if current_user else None,
        action=db_session.info.get('audit_action'),
        parameters=db_session.info.get('audit_params'),
        ip_address=db_session.info.get('client_ip'),
        user_agent=db_session.info.get('user_agent')
    )
    db_session.add(log)

event.listen(AuditLog, 'after_insert', audit_listener)