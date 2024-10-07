from kind_cluster_setup.commands.base import Command
from kind_cluster_setup.cluster.kind_cluster import KindCluster
from kind_cluster_setup.config.config_loader import load_cluster_config, get_environment_config
from kind_cluster_setup.utils.logging import get_logger

logger = get_logger(__name__)

class DeleteCommand(Command):
    def execute(self, args):
        logger.info(f"Deleting Kind cluster for environment: {args.environment}")
        env_config = get_environment_config(args.environment)
        cluster_config = load_cluster_config(args.environment)
        
        cluster = KindCluster(cluster_config, env_config)
        cluster.delete()
