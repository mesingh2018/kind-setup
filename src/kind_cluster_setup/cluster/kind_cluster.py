import subprocess
from typing import Dict
from kind_cluster_setup.utils.logging import get_logger
from kind_cluster_setup.utils.yaml_handler import dump_yaml

logger = get_logger(__name__)

class KindCluster:
    def __init__(self, cluster_config: Dict[str, any], env_config: Dict[str, any]):
        self.cluster_config = cluster_config
        self.env_config = env_config
        self.cluster_name = f"{cluster_config['name']}-{env_config['namespace']}"  # Use 'namespace' instead of 'environment'

    def create(self) -> None:
        """Create a Kind cluster."""
        kind_config = {
            "kind": "Cluster",
            "apiVersion": "kind.x-k8s.io/v1alpha4",
            "nodes": [{"role": "control-plane"}] + [{"role": "worker"} for _ in range(self.cluster_config['worker_nodes'])]
        }
        
        try:
            with open("kind_config.yaml", "w") as f:
                dump_yaml(kind_config, f)

            cmd = f"kind create cluster --name {self.cluster_name} --config kind_config.yaml"
            subprocess.run(cmd, shell=True, check=True)
            logger.info(f"Kind cluster '{self.cluster_name}' created successfully.")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to create Kind cluster: {e}")
            raise
        finally:
            subprocess.run("rm kind_config.yaml", shell=True, check=False)

    def delete(self) -> None:
        """Delete the Kind cluster."""
        try:
            cmd = f"kind delete cluster --name {self.cluster_name}"
            subprocess.run(cmd, shell=True, check=True)
            logger.info(f"Kind cluster '{self.cluster_name}' deleted successfully.")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to delete Kind cluster: {e}")
            raise

    def get_info(self) -> str:
        """Get information about the Kind cluster."""
        try:
            cmd = f"kubectl cluster-info --context kind-{self.cluster_name}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to get Kind cluster info: {e}")
            raise
