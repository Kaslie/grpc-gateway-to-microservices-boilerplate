from modules.utils.rest_util import build_url, mirror_request
from modules.api_services.calculate.calculate_interface import CalculateInterface


class Calculate(CalculateInterface):
    def __init__(self, base_url):
        self.base_url = base_url

    @classmethod
    def build(cls, dns, port):
        base_url = build_url(dns, port)
        return cls(base_url)

    def health_check_request(self):
        url = self.base_url + "/health"
        response = mirror_request(url)

        return response

    """Handle Error or Tracking at this level"""
    def calculate_request(self, first_number, second_number):
        url = self.base_url + "/calculate"
        response = mirror_request(url=url)

        return response
