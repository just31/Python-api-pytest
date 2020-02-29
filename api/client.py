import requests


class RestfulDoorwayClient:

    _s = requests.session()
    host = None

    def __init__(self, host):
        self.host = host

    # post методы
    def create_corporate(self):
        return self._s.post(self.host + "/api/v1/corporate/?email=test@test.com&phone=00000000000&comment=Test")

    def create_corporate_empty(self):
        return self._s.post(self.host + "/api/v1/corporate/")

    def getting_authorization_token(self, given):
        return self._s.post(self.host + "/api-token-auth/", data=given)

    # get методы
    def get_add_certificates(self):
        return self._s.get(self.host + f"/api/gifts/")

    def get_add_certificates_limit_offset(self):
        return self._s.get(self.host + f"/api/gifts/?limit=2&offset=3")

    def get_best_events(self):
        return self._s.get(self.host + f"/api/v1/best_events/")

    def get_halls(self):
        return self._s.get(self.host + f"/api/v1/places/?host_name=testsite.com")

    def get_CRUD_main_pahe_halls(self):
        return self._s.get(self.host + f"/api/v1/places/25/?host_name=testsite.com")
