# Configuration System

This Python template includes a Laravel-inspired configuration system that allows you to manage application settings through Python files and environment variable overrides.

## Features

- **Multiple Config Files**: Organize your configuration into separate Python files (e.g., `app.py`, `database.py`, `mail.py`)
- **Environment Overrides**: Use `.env` file or environment variables to override config values
- **Dot Notation Access**: Access nested configuration using dot notation (e.g., `database.connections.mysql.host`)
- **Runtime Changes**: Modify configuration values at runtime for testing or dynamic behavior
- **Helper Functions**: Easy-to-use helper functions for common config operations

## Usage

### Basic Configuration Access

```python
import helpers

# Get configuration values using dot notation
app_name = helpers.get_config('app.name', 'Default App')
db_host = helpers.get_config('database.connections.mysql.host', 'localhost')
debug_mode = helpers.get_config('app.debug', False)

# Check if a configuration exists
if helpers.has_config('app.name'):
    print("App name is configured")

# Get all configuration for a file
all_app_config = helpers.get_all_config('app')
```

### Environment Variable Overrides

Environment variables take precedence over config files. Use uppercase and underscores:

- `app.name` → `APP_NAME`
- `database.connections.mysql.host` → `DATABASE_CONNECTIONS_MYSQL_HOST`

Example `.env` file:
```bash
APP_NAME=My Custom App
APP_DEBUG=true
DATABASE_HOST=production-db.example.com
```

### Runtime Configuration Changes

```python
# Modify configuration at runtime (doesn't persist)
helpers.set_config('app.name', 'Runtime Modified Name')

# Reload configuration from files
helpers.reload_config()  # Reload all
helpers.reload_config('app')  # Reload specific file
```

## Configuration Files

### Creating New Config Files

1. Create a new Python file in the `config/` directory
2. Define configuration variables as module-level variables
3. Use dictionaries for nested configuration

Example `config/services.py`:
```python
# External service configurations
api_key = "your-api-key-here"

payment = {
    "stripe": {
        "public_key": "",
        "secret_key": "",
        "webhook_secret": ""
    },
    "paypal": {
        "client_id": "",
        "client_secret": "",
        "sandbox": True
    }
}

cache = {
    "driver": "redis",
    "ttl": 3600
}
```

### Existing Config Files

- **`app.py`**: Application-wide settings (name, version, debug mode, etc.)
- **`database.py`**: Database connections and settings
- **`mail.py`**: Email/mail configuration

## Advanced Usage

### Direct Config Manager Access

```python
from config_manager import ConfigManager

# Create a custom config manager
config = ConfigManager(config_dir="custom_config", env_file="custom.env")

# Use the manager directly
value = config.get('custom.setting', 'default')
config.set('custom.setting', 'new_value')
```

### Environment Helper

```python
# Get environment variable with fallback to config
value = helpers.env('API_KEY', 'default-key')
value = helpers.env('app.name')  # Falls back to config if no env var
```

## Best Practices

1. **Organize by Feature**: Create separate config files for different aspects (database, mail, cache, etc.)
2. **Use Environment Variables**: For sensitive data and environment-specific settings
3. **Provide Defaults**: Always provide sensible default values
4. **Document Settings**: Add comments to explain complex configuration options
5. **Validate Config**: Add validation for critical configuration values in your application startup

## Example: Full Configuration Workflow

```python
import helpers

# Application startup - validate critical config
if not helpers.has_config('app.name'):
    raise ValueError("App name must be configured")

# Get database connection details
db_config = helpers.get_all_config('database')
connection = db_config['connections'][db_config['default']]

# Use environment override for sensitive data
api_key = helpers.env('API_KEY')
if not api_key:
    raise ValueError("API_KEY environment variable required")

# Runtime configuration for testing
if helpers.get_config('app.env') == 'testing':
    helpers.set_config('app.debug', True)
    helpers.set_config('database.default', 'sqlite')
```

This configuration system provides the flexibility of Laravel's config system while maintaining Python's simplicity and power.