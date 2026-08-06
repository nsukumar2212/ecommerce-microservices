from shared.config.settings import get_settings

settings = get_settings()

print(settings.APP_NAME)
print(settings.APP_VERSION)
print(settings.API_PREFIX)
print(settings.DATABASE_URL)