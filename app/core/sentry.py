import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from core.config import settings

def configure_sentry(app):
    if settings.SENTRY_DSN:
        sentry_sdk.init(
            dsn=settings.SENTRY_DSN,
            environment=settings.ENVIRONMENT,
            integrations=[SentryAsgiMiddleware()]
        )