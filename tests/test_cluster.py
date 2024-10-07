import unittest
from unittest.mock import patch, MagicMock
from kind_cluster_setup.cluster.kind_cluster import KindCluster

class TestKindCluster(unittest.TestCase):
    def setUp(self):
        self.cluster_config = {"name": "test-cluster", "worker_nodes": 2}
        self.env_config = {"environment": "dev"}
        self.kind_cluster = KindCluster(self.cluster_config, self.env_config)

    @patch('subprocess.run')
    def test_create_cluster(self, mock_run):
        self.kind_cluster.create()
        mock_run.assert_called_with("kind create cluster --name test-cluster-dev --config kind_config.yaml", shell=True, check=True)

    @patch('subprocess.run')
    def test_delete_cluster(self, mock_run):
        self.kind_cluster.delete()
        mock_run.assert_called_with("kind delete cluster --name test-cluster-dev", shell=True, check=True)

if __name__ == '__main__':
    unittest.main()