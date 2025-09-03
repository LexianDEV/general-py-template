# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2024-09-03

### Removed

- Async functionality

This is because it introduced unnecessary complexity and potential issues with the application's performance.

## [1.1.0] - 2024-08-23

### Changed

- Switched from auto-generated release notes to Keep A Changelog format
- Unified build workflows for all PyInstaller-compatible platforms
- Added support for macOS builds (Intel x86_64 and Apple Silicon ARM64)
- Improved release asset naming with platform-specific identifiers

### Fixed

- Fixed requirements.txt encoding issue (UTF-16 to UTF-8)

## [1.0.0] - 2024-08-22

### Added

- Initial Python template application
- Basic time display functionality
- PyInstaller build configuration for Linux and Windows
- GitHub Actions workflows for automated builds
- Cross-platform executable generation

### Fixed

- Initial release with basic functionality

[Unreleased]: https://github.com/LexianDEV/general-py-template/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/LexianDEV/general-py-template/releases/tag/v1.0.0
