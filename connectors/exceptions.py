class ConnectorError(Exception):
    """Base connector exception."""


class ConnectionFailed(ConnectorError):
    """Unable to connect."""


class CollectionFailed(ConnectorError):
    """Unable to collect evidence."""
