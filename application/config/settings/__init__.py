from os import environ

from split_settings.tools import include, optional

environ.setdefault("DJANGO_ENV", "development")
_ENV = environ["DJANGO_ENV"]

_base_settings = (
    "components/common.py",
    "components/storage.py",
    "components/logging.py",
    "components/i18n.py",
    "components/security.py",
    "components/extra.py",
    f"environments/{_ENV}.py",
    optional("environments/local.py"),
)

include(*_base_settings)
