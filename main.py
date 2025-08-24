"""
General Python Template - Main Entry Point
Minimal async-coordinated entry point that delegates to modules.
"""

import asyncio
from modules import AppModule


async def main():
    """Main application entry point with async foundation."""
    app = AppModule()
    await app.start()


if __name__ == '__main__':
    asyncio.run(main())