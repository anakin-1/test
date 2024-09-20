class RepositoryError(Exception):
    """Base class for other exceptions"""
    pass


class NotFoundError(RepositoryError):
    """Raised when a requested item is not found"""
    pass


class DatabaseConnectionError(RepositoryError):
    """Raised when the database connection fails"""
    pass


class DataValidationError(RepositoryError):
    """Raised when data validation fails"""
    pass
