import unittest
import requests_mock

from appscanner.services import get_application_id_by_name, create_api_client


class TestServices(unittest.TestCase):
    base_uri = '{protocol}://{server}/Hailstorm.WS/HailstormRESTService.svc/client/{client}/customer/{customer}'

    def test_get_application_id_by_name(self):
        service_path = '/application/{application_name}/id'
        service_uri = self.base_uri + service_path
        api = create_api_client('my_server', 'my_client', 'my_customer')
        with requests_mock.Mocker() as m:
            with open('tests/test_files/application_id_by_name.json') as f:
                m.get('https://my_server/Hailstorm.WS/HailstormRESTService.svc/client/my_client/customer/my_customer/application/my_application/id',
                      text=f.read())

            self.assertEqual('dcb434b9-8101-4a85-9bf5-57396b283c7e',
                             get_application_id_by_name(api, 'my_application'))

