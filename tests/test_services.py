import unittest
import requests_mock
from unittest import skip

from appscanner.services import create_api_client, get_application_id_by_name,\
    application_exists, assessment_exists, get_assessment_id_by_name,\
    get_assessment_status


class TestServices(unittest.TestCase):
    protocol = 'https'
    server = 'my_server'
    client = 'my_client'
    customer = 'my_customer'
    application_id = 'dcb434b9-8101-4a85-9bf5-57396b283c7e'
    assessment_id = 'bb8c6a5d-b1fc-40ea-9c58-1d58efbdb023'
    assessment_name = 'E-commerce'
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

    def test_assessment_exists(self):
        service_path = '/application/{application_id}/assessment/' \
                       '{assessment_id}/exists'
        service_uri = self.base_uri + service_path

        with requests_mock.Mocker() as m:
            m.get(service_uri.format(application_id=self.application_id,
                                     assessment_id=self.assessment_id),
                  text='{"status-code":0,"assessment-exists":true}')
            self.assertEqual(True, assessment_exists(
                self.api, self.application_id, self.assessment_id))

    def test_get_assessment_id_by_name(self):
        service_path = '/application/{application_id}/assessment/' \
                       '{assessment_name}/id'
        service_uri = self.base_uri + service_path

        with requests_mock.Mocker() as m:
            m.get(service_uri.format(application_id=self.application_id,
                                     assessment_name=self.assessment_name),
                  text='{"status-code":0,"assessment-id":"9861f163-d26e-4c93-a3f1-ce37798fe88e"}')
            self.assertEqual(
                '9861f163-d26e-4c93-a3f1-ce37798fe88e',
                get_assessment_id_by_name(self.api, self.application_id,
                                          self.assessment_name)
            )

    def test_get_assessment_status(self):
        service_path = '/application/{application_id}/assessment/' \
                       '{assessment_id}/status'
        service_uri = self.base_uri + service_path

        with requests_mock.Mocker() as m:
            m.get(service_uri.format(application_id=self.application_id,
                                     assessment_id=self.assessment_id),
                  text='{"status-code":0,"assessment-status":"running"}')
            self.assertEqual(
                'running',
                get_assessment_status(self.api, self.application_id,
                                      self.assessment_id))

    @skip("Not ready yet")
    def test_get_current_assessment_run_id(self):
        service_path = '/application/{application_name}/id'
        service_uri = self.base_uri + service_path
        with requests_mock.Mocker() as m:
            with open('tests/test_files/assessment_runs.json') as f:
                m.get(service_uri.format(application_name='my_application'),
                      text=f.read())

            self.assertEqual(
                'dcb434b9-8101-4a85-9bf5-57396b283c7e',
                get_application_id_by_name(self.api, 'my_application')
            )

    @skip("Not ready yet")
    def test_get_assessment_run_status(self):
        service_path = '/application/{application_id}/assessmentrun/' \
                       '{assessment_run_id}/status'
        service_uri = self.base_uri + service_path
        with requests_mock.Mocker() as m:
            with open('tests/test_files/assessment_runs.json') as f:
                m.get(service_uri.format(application_name='my_application'),
                      text=f.read())
