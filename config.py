import os
from typing import get_type_hints

from dotenv import load_dotenv

load_dotenv()


class AppConfigError(Exception):
    pass


class AppConfig:
    ENV: str = 'development'
    COHERE_API_KEY: str
    HOSTNAME: str
    PORT: int

    def __init__(self, env):
        for field in self.__annotations__:
            # Field will be skipped if not in all caps
            if not field.isupper():
                continue

            # sets default_value to none if no field
            default_value = getattr(self, field, None)

            if default_value is None and env.get(field) is None:
                raise AppConfigError('The {} field is required'.format(field))

            # Cast env var value to expected type and raise AppConfigError on failure
            try:
                var_type = get_type_hints(AppConfig)[field]
                value = var_type(env.get(field, default_value))

                self.__setattr__(field, value)
            except ValueError:
                raise AppConfigError('Unable to cast value of "{}" to type "{}" for "{}" field'.format(
                    env[field],
                    var_type,
                    field
                )
                )

    def __repr__(self):
        return str(self.__dict__)


Config = AppConfig(os.environ)
