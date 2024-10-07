import argparse
from kind_cluster_setup.commands.base import Command
from kind_cluster_setup.cluster.kind_cluster import KindCluster
from kind_cluster_setup.config.config_loader import load_cluster_config, get_environment_config
from kind_cluster_setup.utils.logging import get_logger

logger = get_logger(__name__)

class CreateCommand(Command):
    """Command to create a Kind cluster."""

    def execute(self, args: argparse.Namespace) -> None:
        """
        Execute the create command.

        Args:
            args (argparse.Namespace): The command-line arguments.
        """
        try:
            logger.debug(f"Arguments received in CreateCommand: {vars(args)}")
            environment: str = getattr(args, 'environment', 'dev')
            logger.info(f"Creating Kind cluster for environment: {environment}")
            env_config: dict = get_environment_config(environment)
            cluster_config: dict = load_cluster_config(environment)
            
            cluster: KindCluster = KindCluster(cluster_config, env_config)
            cluster.create()
        except Exception as e:
            logger.error(f"Failed to create Kind cluster: {e}")
            raise
