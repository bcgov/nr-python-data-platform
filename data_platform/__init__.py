
# data_platform/__init__.py
from .db.db_connection import get_connection
from .db.executor import run_query
from .logging.logger import setup_logger
