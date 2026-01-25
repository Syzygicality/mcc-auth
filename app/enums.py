from enum import Enum

class AuthStatus(str, Enum):
    UNAUTHORIZED = "unauthorized"
    REQUESTED = "requested"
    APPROVED = "approved"
    DENIED = "denied"
    ADMIN = "admin"