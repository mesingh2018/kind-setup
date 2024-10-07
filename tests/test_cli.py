import unittest
from argparse import Namespace
from kind_cluster_setup.cli.parser import create_parser

class TestCLIParser(unittest.TestCase):
    def setUp(self):
        self.parser = create_parser()

    def test_create_command(self):
        args = self.parser.parse_args(['create', '--environment', 'dev'])
        self.assertEqual(args.action, 'create')
        self.assertEqual(args.environment, 'dev')

    def test_delete_command(self):
        args = self.parser.parse_args(['delete', '--environment', 'qa'])
        self.assertEqual(args.action, 'delete')
        self.assertEqual(args.environment, 'qa')

    def test_deploy_command(self):
        args = self.parser.parse_args(['deploy', '--environment', 'staging', '--apps', 'app1', 'app2', '--deployments', 'helm', 'kubernetes'])
        self.assertEqual(args.action, 'deploy')
        self.assertEqual(args.environment, 'staging')
        self.assertEqual(args.apps, ['app1', 'app2'])
        self.assertEqual(args.deployments, ['helm', 'kubernetes'])

if __name__ == '__main__':
    unittest.main()