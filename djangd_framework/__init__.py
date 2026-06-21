"""djangd-framework

A Django component library built on Material Design (MDC Web) primitives.

Public API:
- ``Component`` base class to define new components.
- ``register`` decorator / function to add components to the registry.
- ``registry`` global registry instance.
"""

from .registry import Component, registry, register

__all__ = ["Component", "registry", "register"]
__version__ = "0.1.0"

default_app_config = "djangd_framework.apps.DjangdFrameworkConfig"
