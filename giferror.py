import re
import webbrowser


class GIFError(Exception):
    """Exception class which displays GIFs in a web browser."""

    def __init__(self, message=""):
        self.message = message
        match = re.search("(?P<url>https?://[^\s]+\.gif+)", message)
        if match:
            webbrowser.open(match.group("url"))
        super(Exception, self).__init__(message)
