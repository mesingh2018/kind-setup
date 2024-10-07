from kind_cluster_setup.commands.base import Command
from kind_cluster_setup.cluster.kind_cluster import KindCluster
from kind_cluster_setup.deployment.helm import HelmDeploymentStrategy
from kind_cluster_setup.deployment.kubernetes import KubernetesDeploymentStrategy
from kind_cluster_setup.config.config_loader import load_cluster_config, get_environment_config
from kind_cluster_setup.utils.logging import get_logger

logger = get_logger(__name__)

class StatusCommand(Command):
    def execute(self, args):
        logger.info(f"Checking status for environment: {args.environment}")
        env_config = get_environment_config(args.environment)
        cluster_config = load_cluster_config(args.environment)
        
        cluster = KindCluster(cluster_config, env_config)
        cluster_info = cluster.get_info()
        logger.info(f"Cluster info:\n{cluster_info}")
        
        if args.apps:
            for app, deployment_method in zip(args.apps, args.deployments):
                if deployment_method == "helm":
                    strategy = HelmDeploymentStrategy()
                elif deployment_method == "kubernetes":
                    strategy = KubernetesDeploymentStrategy()
                else:
                    raise ValueError(f"Unsupported deployment method: {deployment_method}")
                
                app_status = strategy.check_status(app, env_config)
                logger.info(f"Status for {app} ({deployment_method}):\n{app_status}")
