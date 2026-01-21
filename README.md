# python-data-platform

Shared Python library providing reusable data platform utilities such as
Oracle database connectivity, query execution helpers, and standardized logging.

This repository is intended to be **consumed by other Python projects**
(e.g. data scan jobs, automated reports) and is **not a standalone application**.

---

##  What this library provides

- Oracle database connection helpers
- Query execution utilities
- Centralized logging configuration
- Common utilities shared across Jenkins jobs

Current structure:
data_platform/
├── config/
│ └── loader.py
├── db/
│ ├── db_connection.py
│ └── executor.py
└── app_logging/
  └── logger.py

##  How to use this library

Add it as a Git dependency in a consuming project:

```toml
dependencies = [
    "python_data_platform @ git+https://github.com/bcgov/nr-python-data-platform.git@v1.0.0"
]