import subprocess
from typing import Dict
from kind_cluster_setup.deployment.base import DeploymentStrategy
from kind_cluster_setup.utils.logging import get_logger
from kind_cluster_setup.utils.constants import K8S_MANIFEST_PATH

logger = get_logger(__name__)

class KubernetesDeploymentStrategy(DeploymentStrategy):
    def deploy(self, app: str, app_config: Dict[str, any], env_config: Dict[str, any]) -> None:
        logger.info(f"Deploying Kubernetes manifests for {app}")
        
        namespace = f"{app}-{env_config['environment']}"
        manifest_dir = K8S_MANIFEST_PATH.format(app=app)

        try:
            # Create namespace
            subprocess.run(f"kubectl create namespace {namespace} --dry-run=client -o yaml | kubectl apply -f -", shell=True, check=True)
            
            # Apply manifests
            subprocess.run(f"kubectl apply -f {manifest_dir} -n {namespace}", shell=True, check=True)
            logger.info(f"Kubernetes manifests for {app} deployed successfully")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to deploy Kubernetes manifests for {app}: {e}")
            raise

    def check_status(self, app: str, env_config: Dict[str, any]) -> str:
        logger.info(f"Checking status of Kubernetes deployment for {app}")
        namespace = f"{app}-{env_config['environment']}"
        
        try:
            result = subprocess.run(f"kubectl get pods -n {namespace} -l app={app}", shell=True, capture_output=True, text=True, check=True)
            logger.info(f"Kubernetes deployment status for {app} checked successfully")
            return result.stdout
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to check status of Kubernetes deployment for {app}: {e}")
            raise
