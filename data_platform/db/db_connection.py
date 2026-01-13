# src/db_connection.py
import os
import logging
from typing import Optional
import oracledb

logger = logging.getLogger(__name__)

def _env_prefix() -> str:
    return os.getenv("APP_ENV", "test").strip().upper()

def get_connection(
    user: Optional[str] = None,
    password: Optional[str] = None,
    dsn: Optional[str] = None,
):
    prefix = _env_prefix()

    user = user or os.getenv(f"{prefix}_DB_USER")
    password = password or os.getenv(f"{prefix}_DB_PASSWORD")
    dsn = dsn or os.getenv(f"{prefix}_DB_DSN")

    missing = [k for k, v in {
        "user": user,
        "password": password,
        "dsn": dsn
    }.items() if not v]

    if missing:
        raise ValueError(
            f"Missing {', '.join(missing)} for {prefix} environment "
            f"(check {prefix}_DB_USER / {prefix}_DB_PASSWORD / {prefix}_DB_DSN)"
        )

    logger.info("Creating Oracle DB connection (%s)", prefix)
    try:
        return oracledb.connect(user=user, password=password, dsn=dsn)
    except oracledb.DatabaseError:
        logger.exception("Failed to connect to Oracle database")
        raise
