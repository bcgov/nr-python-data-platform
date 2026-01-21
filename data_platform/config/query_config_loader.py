from pathlib import Path
import yaml
import logging

logger = logging.getLogger(__name__)


def load_query_config(yaml_path: Path) -> dict:
    """
    Load query configuration YAML and resolve SQL definitions.

    Supports:
    - Inline SQL (sql)
    - SQL file references (sql_file)

    Returns:
        dict structured by category
    """
    if not yaml_path.exists():
        raise FileNotFoundError(f"Query config not found: {yaml_path}")

    logger.debug("Loading query config from %s", yaml_path)

    with yaml_path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    queries = config.get("queries", {})
    base_dir = yaml_path.parent

    for category, query_list in queries.items():
        for q in query_list:
            name = q.get("name", "<unnamed>")

            # Inline SQL (data scan project)
            if "sql" in q:
                q["sql"] = q["sql"].strip()

            # SQL file reference (report project)
            elif "sql_file" in q:
                sql_path = (base_dir / q["sql_file"]).resolve()
                if not sql_path.exists():
                    raise FileNotFoundError(
                        f"SQL file not found for query '{name}': {sql_path}"
                    )
                q["sql"] = sql_path.read_text(encoding="utf-8").strip()

            else:
                raise ValueError(
                    f"Query '{name}' must define either 'sql' or 'sql_file'"
                )

    return queries
