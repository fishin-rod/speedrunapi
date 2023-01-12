class URLerror(Exception):
    def __init__(self, message):
        """This error is thrown when the url is invalid.
        This replaces http.client.InvalidURL errors."""
        self.message = message