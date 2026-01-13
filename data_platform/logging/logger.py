
import logging
import os
import sys

def setup_logger(log_level: str, log_file: str | None, app_name: str = "hbs_daily_data_scan") -> None:
    # Normalize level
    level = getattr(logging, str(log_level).upper(), None)
    if level is None or not isinstance(level, int):
        raise ValueError(f"Invalid log level: {log_level!r}")
    
    
    # Resolve environment name (default to 'prod' if not set)
    env = os.getenv("APP_ENV", "prod").lower()

    
    # If no explicit log_file provided, build from APP_ENV
    if not log_file:
        log_file = f"logs/{app_name}_{env}.log"

    
    # Resolve to an absolute path
    log_file = os.path.abspath(log_file)

    # Ensure directory exists if provided
    dir_name = os.path.dirname(log_file)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    # Configure logging (force reconfigure if needed)
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler(log_file, mode="a", encoding="utf-8"),
            logging.StreamHandler(sys.stderr),
        ],
         force = True  # Uncomment if you need to reconfigure in long-running apps
    )

    root = logging.getLogger()
    logging.info("Root handlers: %s", root.handlers)
    
    # Sanity line so you can see config details at the top of the log
    logging.info("Logging initialized | level=%s | file=%s | env=%s",
                 logging.getLevelName(level), log_file, env)
