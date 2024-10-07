import sys
from kind_cluster_setup.cli.parser import create_parser
from kind_cluster_setup.utils.logging import setup_logging, get_logger

logger = get_logger(__name__)

def main() -> None:
    """Main entry point for the kind-cluster-setup CLI."""
    setup_logging()
    parser = create_parser()
    args = parser.parse_args()

    logger.info(f"Starting Action: {args.action}")
    logger.debug(f"Parsed arguments: {vars(args)}")  # Add this line for debugging

    try:
        args.func(args)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        logger.info("Action completed")

if __name__ == "__main__":
    main()
