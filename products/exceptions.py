import logging

logger = logging.getLogger(__name__)


class VKontakte_GroupAuthorizationFailed(Exception):
    def __init__(self, text):
        self.text = text
