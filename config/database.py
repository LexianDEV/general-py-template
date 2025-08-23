"""
Database configuration settings.
"""

# Default database connection
default = "sqlite"

# Database connections
connections = {
    "sqlite": {
        "driver": "sqlite",
        "database": "data/database.db",
        "prefix": ""
    },
    "mysql": {
        "driver": "mysql",
        "host": "localhost",
        "port": 3306,
        "database": "app_database",
        "username": "root",
        "password": "",
        "charset": "utf8mb4",
        "prefix": ""
    },
    "postgresql": {
        "driver": "postgresql",
        "host": "localhost", 
        "port": 5432,
        "database": "app_database",
        "username": "postgres",
        "password": "",
        "charset": "utf8",
        "prefix": ""
    }
}

# Migration settings
migrations = {
    "table": "migrations",
    "path": "database/migrations"
}

# Redis configuration for caching/sessions
redis = {
    "host": "localhost",
    "port": 6379,
    "database": 0,
    "prefix": "app:"
}