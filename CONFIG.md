# Configuration System

This Python template includes a Laravel-inspired configuration system that allows you to manage application settings through Python files and environment variable overrides.

## Features

- **Multiple Config Files**: Organize your configuration into separate Python files (e.g., `app.py`)
- **JSON Configuration**: Use `config.json` file for non-sensitive settings that get bundled into the application
- **Environment Overrides**: Use environment variables to override config values
- **Dot Notation Access**: Access nested configuration using dot notation (e.g., `app.name`, `app.logging.level`)
- **Runtime Changes**: Modify configuration values at runtime for testing or dynamic behavior
- **Helper Functions**: Easy-to-use helper functions for common config operations

## Usage

### Basic Configuration Access

```python
import helpers

# Get configuration values using dot notation
app_name = helpers.get_config('app.name', 'Default App')
response_number = helpers.get_config('app.response_number', 42)
debug_mode = helpers.get_config('app.debug', False)

# Check if a configuration exists
if helpers.has_config('app.name'):
    print("App name is configured")

# Get all configuration for a file
all_app_config = helpers.get_all_config('app')
```

### JSON Configuration Overrides

JSON configuration takes precedence over config files but environment variables still override everything. The `config.json` file is bundled into the application when built and contains non-sensitive settings:

- `app.name` → `APP_NAME` in JSON
- `app.response_number` → `APP_RESPONSE_NUMBER` in JSON  
- `app.logging.level` → `APP_LOGGING_LEVEL` in JSON

Example `config.json` file:
```json
{
  "APP_NAME": "My Custom App",
  "APP_ENV": "development", 
  "APP_DEBUG": true,
  "APP_RESPONSE_NUMBER": 100,
  "APP_MESSAGE": "Hello from the environment!",
  "APP_LOGGING_LEVEL": "DEBUG"
}
```

### Environment Variable Overrides

Environment variables take highest precedence over both JSON config and config files. Use uppercase and underscores:

- `app.name` → `APP_NAME`
- `app.response_number` → `APP_RESPONSE_NUMBER`
- `app.logging.level` → `APP_LOGGING_LEVEL`

Example environment variables:
```bash
export APP_NAME="My Custom App"
export APP_DEBUG=true
export APP_RESPONSE_NUMBER=100
export APP_MESSAGE="Hello from the environment!"
```

**Note:** The bundled `config.json` file provides application defaults and is automatically extracted and cleaned up when the application runs. Environment variables can still be used to override any setting at runtime.

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

external_api = {
    "base_url": "https://api.example.com",
    "timeout": 30,
    "retry_attempts": 3
}

cache = {
    "enabled": True,
    "ttl": 3600
}
```

### Existing Config Files

- **`app.py`**: Application-wide settings (name, version, debug mode, response number, etc.)

## Advanced Usage

### Direct Config Manager Access

```python
from config_manager import ConfigManager

# Create a custom config manager
config = ConfigManager(config_dir="custom_config", json_file="custom_config.json")

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
2. **Use JSON for Non-Sensitive Defaults**: Store application defaults in `config.json` that get bundled with the application
3. **Use Environment Variables**: For sensitive data and environment-specific settings
4. **Provide Defaults**: Always provide sensible default values
5. **Document Settings**: Add comments to explain complex configuration options
6. **Validate Config**: Add validation for critical configuration values in your application startup

**Security Note**: The `config.json` file is bundled into the application and can be viewed by anyone with access to the built executable. Only store non-sensitive configuration in this file. Use environment variables for sensitive data like API keys, passwords, and secrets.

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