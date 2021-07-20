class Error(Exception):
    """Raised to propagate errors to user via main().
    """
    default_message = "unspecified error"

    def __init__(self, message):
        self.message = message or self.default_message
        Exception.__init__(self, message)


class BadConfig(Error):
    """
    """
    default_message = "bad config"


class NoMessage(Error):
    """
    """
    default_message = "no message given"


class NoOutputFile(Error):
    """
    """
    default_message = "no output file found"
