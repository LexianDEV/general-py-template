"""
General Python Template - Main Entry Point
Minimal entry point that delegates to modules.
"""

from modules import AppModule


def main():
    """Main application entry point."""
    app = AppModule()
    app.start()


if __name__ == '__main__':
    main()