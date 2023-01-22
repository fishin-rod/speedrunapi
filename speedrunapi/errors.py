"""Custom errors for the library."""

class URLerror(Exception):
    def __init__(self, message):
        """This error is thrown when the url is invalid.
        This replaces http.client.InvalidURL errors."""
        self.message = message

class Region_Length_Error(Exception):
    def __init__(self, message):
        """This error is thrown when there is more then 1 region
        provided when calling the region module. Or there is 0
        regions provided"""
        self.message = message