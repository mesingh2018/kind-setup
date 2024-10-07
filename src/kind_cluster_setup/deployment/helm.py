import subprocess
from typing import Dict
from kind_cluster_setup.deployment.base import DeploymentStrategy
from kind_cluster_setup.utils.logging import get_logger
from kind_cluster_setup.utils.constants import HELM_CHART_PATH

logger = get_logger(__name__)

class HelmDeploymentStrategy(DeploymentStrategy):
    def deploy(self, app: str, app_config: Dict[str, any], env_config: Dict[str, any]) -> None:
        logger.info(f"Deploying Helm chart for {app}")
        
        helm_command = [
            "helm", "upgrade", "--install",
            app, HELM_CHART_PATH.format(app=app),
            "--namespace", f"{app}-{env_config['environment']}",
            "--create-namespace",
            "--values", f"{HELM_CHART_PATH.format(app=app)}/values.yaml",
            "--set", f"environment={env_config['environment']}"
        ]

        for key, value in app_config.items():
            helm_command.extend(["--set", f"{key}={value}"])

        logger.info(f"Executing Helm command: {' '.join(helm_command)}")
        try:
            subprocess.run(helm_command, check=True)
            logger.info(f"Helm chart for {app} deployed successfully")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to deploy Helm chart for {app}: {e}")
            raise

    def check_status(self, app: str, env_config: Dict[str, any]) -> str:
        logger.info(f"Checking status of Helm chart for {app}")
        helm_command = [
            "helm", "status", app,
            "--namespace", f"{app}-{env_config['environment']}",
        ]
        
        try:
            result = subprocess.run(helm_command, check=True, capture_output=True, text=True)
            logger.info(f"Helm chart for {app} status checked successfully")
            return result.stdout
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to check status of Helm chart for {app}: {e}")
            raise
