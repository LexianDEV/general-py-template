## Template
This is a template for a **GENERAL APPLICATION** built in Python.

It was developed by LexianDEV

## Features

- **Laravel-like Configuration System**: Manage application settings through Python files with environment variable overrides
- **Helper Functions**: Utility functions for common operations (time, config management)
- **Modular Structure**: Organized directory structure for configs, modules, data, and logs
- **PyInstaller Ready**: Pre-configured for building standalone executables

## Configuration System

This template includes a powerful configuration system inspired by Laravel. You can:

- Define configuration in Python files (`config/app.py`, `config/database.py`, etc.)
- Override settings with JSON configuration or environment variables
- Access configuration using dot notation: `helpers.get_config('app.name')`
- Modify configuration at runtime for testing

See [CONFIG.md](CONFIG.md) for detailed documentation.

## Quick Start

```python
import helpers

# Get current time
print(f"Current time: {helpers.time()}")

# Get configuration
app_name = helpers.get_config('app.name', 'My App')
debug_mode = helpers.get_config('app.debug', False)

# Use environment variables
api_key = helpers.env('API_KEY', 'default-key')
```

## Changelog Management

This project uses the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format for documenting changes. The changelog is maintained in the `CHANGELOG.md` file and **must be edited manually** when making changes to the project.

### How to Update the Changelog

#### 1. Adding New Changes (Unreleased Section)
When you make changes to the project, add them to the `[Unreleased]` section at the top of the changelog:

```markdown
## [Unreleased]

### Added
- New feature you added

### Changed
- Something you modified

### Deprecated
- Feature that will be removed in future versions

### Removed
- Feature you removed

### Fixed
- Bug you fixed

### Security
- Security improvement you made
```

#### 2. Creating a New Release
When you're ready to release a new version:

1. **Move unreleased changes** from the `[Unreleased]` section to a new version section
2. **Set the release date** in the format `[X.Y.Z] - YYYY-MM-DD`
3. **Update the links** at the bottom of the file
4. **Leave the `[Unreleased]` section empty** for future changes

Example:
```markdown
## [Unreleased]

## [1.1.0] - 2024-12-20

### Added
- New feature you added

### Fixed
- Bug you fixed

## [1.0.0] - 2024-08-22
...
```

#### 3. Automated Release Integration
The GitHub Actions workflows automatically extract the appropriate changelog section for each release:
- When you create a tag/release, the workflow finds the matching version in the changelog
- It extracts only that version's content for the release notes
- If no matching section is found, it provides a fallback message

### Best Practices

- **Always update the changelog** when making meaningful changes
- **Use present tense** for changelog entries ("Add feature" not "Added feature")
- **Be specific and clear** about what changed
- **Group related changes** under the appropriate category
- **Link to issues/PRs** when relevant using `[#123](link)` format
- **Follow semantic versioning** for version numbers

### Example Workflow

1. Make changes to your code
2. Add entries to the `[Unreleased]` section in `CHANGELOG.md`
3. Commit your changes
4. When ready to release:
   - Move unreleased items to a new version section
   - Update version links
   - Create a git tag
   - GitHub Actions will automatically create a release with the changelog content 