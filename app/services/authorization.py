from typing import Final


SUPPORTED_ROLES: Final = {
    "support",
    "technical",
    "admin",
}


def is_authorized(user_role: str) -> bool:
    """Check whether a user role is allowed to access support workflows."""
    return user_role.lower() in SUPPORTED_ROLES