# Changelog

## v0.1.1 - 2025-05-05

### Bug fixes

- Ensure urls render in pypi. [[dd2d677](https://github.com/NRWLDev/pytest-pogo/commit/dd2d677acb3232c5b361eca26780c691aa9a3396)]

## v0.1.0 - 2024-09-09

### Miscellaneous

- Migrate from poetry to uv for dependency and build management [[b71e868](https://github.com/NRWLDev/pytest-pogo/commit/b71e868de960948865ffeb254434c8374c167071)]
- Update changelog-gen and related configuration. [[aec994b](https://github.com/NRWLDev/pytest-pogo/commit/aec994bb4f917dabe45d6296398aabcf3b7b2959)]

## v0.0.4 - 2024-05-22

### Bug fixes

- Use pytests -v flag rather than a duplicate fixture to expose more verbose logs [a3ac9ea](https://github.com/NRWLDev/pytest-pogo/commit/a3ac9ea8026221ba8a837c4df004e85e4855a855)

## v0.0.3 - 2024-05-22

### Features and Improvements

- Quiet down logs in pogo_engine fixture, and introduce pogo_engine_verbose with apply/rollback logs. [2ba1fdf](https://github.com/NRWLDev/pytest-pogo/commit/2ba1fdffce2803c5a724cb0c10028728e690d428)

## v0.0.2 - 2024-03-11

### Features and Improvements

- Add `pogo_config` fixture. [[1178f9d](https://github.com/NRWLDev/pytest-pogo/commit/1178f9dfaadaa65b10b7aa6c4306ca777c971ce5)]

## v0.0.1 - 2024-03-10

### Features and Improvements

- Add pogo_engine fixture to auto manage migrations in test session [[6b5e62e](https://github.com/NRWLDev/pytest-pogo/commit/6b5e62eae8b92633075db481478a592774c5d6b7)]
