import helpers

def main():
    print("=== General Python Template ===")
    print(f"Current time: {helpers.time()}")
    print()
    
    # Get basic app configuration
    app_name = helpers.get_config('app.name', 'Unknown App')
    app_version = helpers.get_config('app.version', '0.0.0')
    app_env = helpers.get_config('app.env', 'unknown')
    app_debug = helpers.get_config('app.debug', False)
    
    print(f"App: {app_name} v{app_version}")
    print(f"Environment: {app_env} (Debug: {app_debug})")
    print()
    
    # Demonstrate the configurable response number
    response_number = helpers.get_config('app.response_number', 0)
    message = helpers.get_config('app.message', 'Hello, World!')
    
    print("=== App Response ===")
    print(f"Message: {message}")
    print(f"Response Number: {response_number}")
    print()
    
    # Show environment variable overrides
    print("=== Configuration Source ===")
    env_number = helpers.env('APP_RESPONSE_NUMBER')
    if env_number:
        print(f"Response number is overridden by environment variable: {env_number}")
    else:
        print(f"Response number is from config file: {response_number}")
    
    env_message = helpers.env('APP_MESSAGE')
    if env_message:
        print(f"Message is overridden by environment variable: {env_message}")
    else:
        print(f"Message is from config file: {message}")

if __name__ == '__main__':
    main()