# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.create_telemetry_data_request import CreateTelemetryDataRequest  # noqa: E501
from swagger_server.models.create_telemetry_data_response import CreateTelemetryDataResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.get_telemetry_data_response import GetTelemetryDataResponse  # noqa: E501
from swagger_server.models.list_telemetry_data_response import ListTelemetryDataResponse  # noqa: E501
from swagger_server.models.update_telemetry_data_request import UpdateTelemetryDataRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTelemetryDataController(BaseTestCase):
    """TelemetryDataController integration test stubs"""

    def test_create_telemetry_data(self):
        """Test case for create_telemetry_data

        Create Telemetry data tracking
        """
        body = CreateTelemetryDataRequest()
        response = self.client.open(
            '/tracking/telemetrydata',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_telemetry_data(self):
        """Test case for delete_telemetry_data

        Delete Telemetry data tracking
        """
        response = self.client.open(
            '/tracking/telemetrydata/{dataId}'.format(data_id='data_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_telemetry_data(self):
        """Test case for get_telemetry_data

        Get a single telemetry Data info
        """
        response = self.client.open(
            '/tracking/telemetrydata/{dataId}'.format(data_id='data_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_telemetry_data(self):
        """Test case for list_telemetry_data

        Retrieve a list of telemetry data sended
        """
        response = self.client.open(
            '/tracking/telemetrydata',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_telemetry_data(self):
        """Test case for update_telemetry_data

        Update Telemetry data tracking
        """
        body = UpdateTelemetryDataRequest()
        response = self.client.open(
            '/tracking/telemetrydata/{dataId}'.format(data_id='data_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
