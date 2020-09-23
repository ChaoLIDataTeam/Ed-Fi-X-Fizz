from .request_client import RequestClient


class Users:
    """
    The Users class contains methods to get users' information from Schoology API

    Args:
        SCHOOLOGY_KEY (str): The consumer key given by Schoology
        SCHOOLOGY_SECRET (str): The consumer secret given by Schoology

    Attributes:
        request_client (RequestClient): The client used for authenticate and send requests to Schoology

    """

    def __init__(self, SCHOOLOGY_KEY, SCHOOLOGY_SECRET):
        self.request_client = RequestClient(SCHOOLOGY_KEY, SCHOOLOGY_SECRET)

    def get_all(self):
        response = self.request_client.get("users")
        return response["user"]