"""Regression tests for the KS nodegroup extensions in botocore models."""

import json
import unittest

from botocore.exceptions import ParamValidationError
from botocore.loaders import Loader
from botocore.model import ServiceModel
from botocore.parsers import create_parser
from botocore.serialize import create_serializer


class TestEKSNodegroupLaunchConfig(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        loader = Loader(
            extra_search_paths=[Loader.BUILTIN_DATA_PATH],
            include_default_search_paths=False,
        )
        cls.models = {
            service: ServiceModel(
                loader.load_service_model(service, 'service-2'),
                service_name=service,
            )
            for service in ('eks', 'eks-internal')
        }

    def serialize_nodegroup(self, fields, operation='UpdateNodegroupConfig'):
        model = self.models['eks']
        params = {
            'clusterName': 'cluster',
            'nodegroupName': 'workers',
            'clientRequestToken': 'test-token',
        }
        if operation == 'CreateNodegroup':
            params['subnets'] = ['subnet']
        params.update(fields)
        request = create_serializer(model.protocol).serialize_to_request(
            params, model.operation_model(operation))
        return json.loads(request['body'])

    def parse_response(self, service, operation, body):
        model = self.models[service]
        return create_parser(model.protocol).parse(
            {
                'status_code': 200,
                'headers': {'content-type': 'application/json'},
                'body': json.dumps(body).encode('utf-8'),
            },
            model.operation_model(operation).output_shape,
        )

    def test_update_serializes_launch_parameters(self):
        for fields in (
                {'instanceTypes': ['m5.xlarge']},
                {'diskSize': 48},
                {'diskType': 'io2'},
                {'instanceTypes': ['m5.xlarge'], 'diskSize': 48,
                 'diskType': 'gp2'},
                {'instanceTypes': ['m5.xlarge'], 'diskSize': 48},
                {}):
            expected = dict(fields, clientRequestToken='test-token')
            self.assertEqual(self.serialize_nodegroup(fields), expected)

    def test_create_serializes_disk_type(self):
        for fields in ({}, {'diskType': 'io2'},
                       {'diskType': 'gp2', 'diskSize': 48}):
            expected = dict(fields, nodegroupName='workers',
                            subnets=['subnet'], clientRequestToken='test-token')
            self.assertEqual(
                self.serialize_nodegroup(fields, operation='CreateNodegroup'),
                expected)

    def test_nodegroup_rejects_wrong_parameter_types(self):
        for fields, parameter in (
                ({'instanceTypes': 'm5.xlarge'}, 'instanceTypes'),
                ({'instanceTypes': [42]}, 'instanceTypes[0]'),
                ({'diskSize': '48'}, 'diskSize'),
                ({'diskSize': 48.5}, 'diskSize'),
                ({'diskType': 42}, 'diskType'),
                ({'diskType': ['io2']}, 'diskType')):
            for operation in ('CreateNodegroup', 'UpdateNodegroupConfig'):
                with self.assertRaises(ParamValidationError) as error:
                    self.serialize_nodegroup(fields, operation=operation)
                self.assertIn('Invalid type for parameter ' + parameter,
                              str(error.exception))

    def test_describe_preserves_launch_parameters(self):
        nodegroup = {
            'nodegroupName': 'workers',
            'instanceTypes': ['m5.xlarge'],
            'diskSize': 48,
            'diskType': 'io2',
        }
        for service in self.models:
            result = self.parse_response(
                service, 'DescribeNodegroup', {'nodegroup': nodegroup})
            self.assertEqual(result['nodegroup'], nodegroup)

    def test_describe_accepts_unknown_custom_launch_template_disk_size(self):
        for service in self.models:
            result = self.parse_response(
                service, 'DescribeNodegroup',
                {'nodegroup': {'instanceTypes': ['m5.large'],
                               'diskSize': None,
                               'diskType': None}})
            self.assertEqual(result['nodegroup']['instanceTypes'],
                             ['m5.large'])
            self.assertIsNone(result['nodegroup'].get('diskSize'))
            self.assertIsNone(result['nodegroup'].get('diskType'))

    def test_update_param_types_include_launch_parameters(self):
        param_types = self.models['eks'].shape_for('UpdateParamType').enum
        self.assertIn('InstanceTypes', param_types)
        self.assertIn('DiskSize', param_types)
        self.assertIn('DiskType', param_types)
        params = [
            {'type': 'InstanceTypes', 'value': '["m5.xlarge"]'},
            {'type': 'DiskSize', 'value': '48'},
            {'type': 'DiskType', 'value': 'io2'},
        ]
        result = self.parse_response(
            'eks', 'UpdateNodegroupConfig', {'update': {'params': params}})
        self.assertEqual(result['update']['params'], params)


if __name__ == '__main__':
    unittest.main()
