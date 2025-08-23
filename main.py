import helpers

def main():
    print("=== General Python Template ===")
    print(f"Current time: {helpers.time()}")
    print()
    
    # Demonstrate config functionality
    print("=== Configuration Examples ===")
    
    # Get app configuration
    app_name = helpers.get_config('app.name', 'Unknown App')
    app_version = helpers.get_config('app.version', '0.0.0')
    app_env = helpers.get_config('app.env', 'unknown')
    app_debug = helpers.get_config('app.debug', False)
    
    print(f"App Name: {app_name}")
    print(f"App Version: {app_version}")
    print(f"Environment: {app_env}")
    print(f"Debug Mode: {app_debug}")
    print()
    
    # Get database configuration
    db_default = helpers.get_config('database.default', 'none')
    db_host = helpers.get_config('database.connections.mysql.host', 'localhost')
    
    print(f"Default Database: {db_default}")
    print(f"MySQL Host: {db_host}")
    print()
    
    # Demonstrate environment variable overrides
    print("=== Environment Variable Overrides ===")
    app_url = helpers.get_config('app.url')
    print(f"App URL (from .env): {app_url}")
    
    # Show environment helper
    debug_level = helpers.env('APP_LOGGING_LEVEL', 'INFO')
    if not debug_level:  # If no env var, fall back to config
        debug_level = helpers.get_config('app.logging.level', 'INFO')
    print(f"Logging Level (from env): {debug_level}")
    print()
    
    # Demonstrate runtime config changes
    print("=== Runtime Configuration Changes ===")
    print(f"Original app name: {helpers.get_config('app.name')}")
    helpers.set_config('app.name', 'Modified App Name')
    print(f"Modified app name: {helpers.get_config('app.name')}")
    print()
    
    # Show all config for a file
    print("=== All App Configuration ===")
    app_config = helpers.get_all_config('app')
    for key, value in app_config.items():
        if not key.startswith('_'):  # Skip private attributes
            print(f"  {key}: {value}")

if __name__ == '__main__':
    main()