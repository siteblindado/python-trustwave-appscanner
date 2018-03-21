import unittest
import requests_mock

from appscanner.services import create_api_client, get_application_id_by_name,\
    application_exists


class TestServices(unittest.TestCase):
    protocol = 'https'
    server = 'my_server'
    client = 'my_client'
    customer = 'my_customer'
    application_id = 'dcb434b9-8101-4a85-9bf5-57396b283c7e'
    base_uri = '{protocol}://{server}/Hailstorm.WS/HailstormRESTService.svc/' \
               'client/{client}/customer/{customer}'.format(
        protocol=protocol, server=server, client=client, customer=customer)

    def setUp(self):
        self.api = create_api_client(self.server, self.client, self.customer)

    def test_aplication_exists(self):
        service_path = '/application/{application_id}/exists'
        service_uri = self.base_uri + service_path

        with requests_mock.Mocker() as m:
            m.get(service_uri.format(application_id=self.application_id),
                  text='{"status-code":0,"application-exists":true}')
            self.assertEqual(True, application_exists(
                self.api, 'dcb434b9-8101-4a85-9bf5-57396b283c7e'))

    def test_get_application_id_by_name(self):
        service_path = '/application/{application_name}/id'
        service_uri = self.base_uri + service_path
        with requests_mock.Mocker() as m:
            with open('tests/test_files/application_id_by_name.json') as f:
                m.get(service_uri.format(application_name='my_application'),
                      text=f.read())

            self.assertEqual(
                'dcb434b9-8101-4a85-9bf5-57396b283c7e',
                get_application_id_by_name(self.api, 'my_application')
            )

