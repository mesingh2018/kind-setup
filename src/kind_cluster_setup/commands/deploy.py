from kind_cluster_setup.commands.base import Command
from kind_cluster_setup.deployment.helm import HelmDeploymentStrategy
from kind_cluster_setup.deployment.kubernetes import KubernetesDeploymentStrategy
from kind_cluster_setup.config.config_loader import load_app_config, get_environment_config
from kind_cluster_setup.utils.logging import get_logger

logger = get_logger(__name__)

class DeployCommand(Command):
    def execute(self, args):
        logger.info(f"Deploying apps to {args.environment} environment")
        env_config = get_environment_config(args.environment)

        for app, deployment_method in zip(args.apps, args.deployments):
            logger.info(f"Deploying {app} using {deployment_method}")
            app_config = load_app_config(app, args.environment)
            
            if deployment_method == "helm":
                strategy = HelmDeploymentStrategy()
            elif deployment_method == "kubernetes":
                strategy = KubernetesDeploymentStrategy()
            else:
                raise ValueError(f"Unsupported deployment method: {deployment_method}")
            
            strategy.deploy(app, app_config, env_config)

