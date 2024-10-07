import argparse
from kind_cluster_setup.commands import CreateCommand, DeleteCommand, DeployCommand, StatusCommand

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Setup and manage Kind Clusters with independent app deployments")
    subparsers = parser.add_subparsers(dest="action", required=True)

    # Create subparser
    create_parser = subparsers.add_parser("create", help="Create a new Kind cluster")
    create_parser.add_argument("--environment", choices=["dev", "qa", "staging", "prod"], default="dev", help="Environment to use")
    create_parser.set_defaults(func=CreateCommand().execute)

    # Delete subparser
    delete_parser = subparsers.add_parser("delete", help="Delete an existing Kind cluster")
    delete_parser.add_argument("--environment", choices=["dev", "qa", "staging", "prod"], default="dev", help="Environment to use")
    delete_parser.set_defaults(func=DeleteCommand().execute)

    # Status subparser
    status_parser = subparsers.add_parser("status", help="Check the status of a cluster or application")
    status_parser.add_argument("--environment", choices=["dev", "qa", "staging", "prod"], default="dev", help="Environment to use")
    status_parser.add_argument("--apps", nargs="+", help="Names of the apps to check status")
    status_parser.add_argument("--deployments", nargs="+", choices=["helm", "kubernetes"], help="Deployment methods used for each app")
    status_parser.set_defaults(func=StatusCommand().execute)

    # Deploy subparser
    deploy_parser = subparsers.add_parser("deploy", help="Deploy an application to the cluster")
    deploy_parser.add_argument("--environment", choices=["dev", "qa", "staging", "prod"], default="dev", help="Environment to use")
    deploy_parser.add_argument("--apps", nargs="+", required=True, help="Names of the apps to deploy")
    deploy_parser.add_argument("--deployments", nargs="+", choices=["helm", "kubernetes"], required=True, help="Deployment methods to use for each app")
    deploy_parser.set_defaults(func=DeployCommand().execute)

    return parser