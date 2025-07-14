# Logger Package

## Version

Current version: 1.0.0

You can access the version in code:
```python
from Pkg_PythonLogger import __version__
print(__version__)
```

A reusable Python logging package with file rotation, multiple output options, and flexible configuration.

## Features

- **Multiple Output Options**: Console, file, or both
- **File Rotation**: Automatic log file rotation with configurable size limits
- **Customizable Formatting**: Flexible log message formats
- **Multiple Log Levels**: DEBUG, INFO, WARNING, ERROR, CRITICAL
- **Exception Logging**: Special method for logging exceptions with full traceback
- **Easy Integration**: Simple import and use in any Python project

## Using as a Git Submodule

To include this logger in your project as a submodule:

```sh
git submodule add <REPO_URL> Pkg_PythonLogger
```

Replace `<REPO_URL>` with the URL of this repository. This will add the logger under the `Pkg_PythonLogger/` directory in your project.

To update the submodule later:

```sh
cd Pkg_PythonLogger
git pull origin master
cd ..
git add Pkg_PythonLogger
git commit -m "Update logger submodule"
```

## Quick Start

```python
from Pkg_PythonLogger import get_full_logger

# Create a logger that outputs to both console and file
logger = get_full_logger("MyApp", "app.log", "INFO")

# Use it
logger.info("Server started")
logger.error("An error occurred")
logger.exception("Exception with traceback")
```

## Usage Examples

### Console Only Logger
```python
from Pkg_PythonLogger import get_console_logger

logger = get_console_logger("MyApp", "DEBUG")
logger.info("This goes to console only")
```

### File Only Logger
```python
from Pkg_PythonLogger import get_file_logger

logger = get_file_logger("MyApp", "app.log", "INFO")
logger.info("This goes to file only")
```

### Full Logger (Console + File)
```python
from Pkg_PythonLogger import get_full_logger

logger = get_full_logger("MyApp", "app.log", "DEBUG")
logger.info("This goes to both console and file")
```

### Custom Configuration
```python
from Pkg_PythonLogger import LoggerConfig, Logger

config = LoggerConfig(
    name="CustomApp",
    level="DEBUG",
    log_file="custom.log",
    max_bytes=5*1024*1024,  # 5MB
    backup_count=3,
    format_string='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
)
logger = Logger(config)
```

## API Reference

### Functions

#### `get_console_logger(name, level)`
Creates a logger that only outputs to console.

#### `get_file_logger(name, log_file, level)`
Creates a logger that only outputs to file.

#### `get_full_logger(name, log_file, level)`
Creates a logger that outputs to both console and file.

#### `create_logger(name, level, log_file, console_output, file_output, max_bytes, backup_count, format_string)`
Creates a logger with custom configuration.

### Classes

#### `LoggerConfig`
Configuration class for logger settings.

**Parameters:**
- `name`: Logger name
- `level`: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `log_file`: Path to log file (optional)
- `max_bytes`: Maximum size of log file before rotation (default: 10MB)
- `backup_count`: Number of backup files to keep (default: 5)
- `format_string`: Custom format string for log messages
- `console_output`: Whether to output to console (default: True)
- `file_output`: Whether to output to file (default: True)

#### `Logger`
Main logger class with file rotation and multiple output options.

**Methods:**
- `debug(message)`: Log debug message
- `info(message)`: Log info message
- `warning(message)`: Log warning message
- `error(message)`: Log error message
- `critical(message)`: Log critical message
- `exception(message)`: Log exception with traceback

## File Structure

```
Pkg_PythonLogger/
├── __init__.py      # Package initialization
├── logger.py        # Main logger implementation
├── example.py       # Usage examples
└── README.md        # This documentation
```

## Integration

To use this logger in your project as a submodule:

1. Add this repository as a submodule (see above).
2. Import and use as shown in the examples above, e.g.:
   ```python
   from Pkg_PythonLogger import get_full_logger
   ```
3. Configure log levels and file paths as needed.

## Configuration

The logger supports various configuration options:

- **Log Levels**: DEBUG, INFO, WARNING, ERROR, CRITICAL
- **File Rotation**: Configurable file size limits and backup counts
- **Output Options**: Console, file, or both
- **Format Strings**: Custom log message formatting
- **Directory Creation**: Automatically creates log directories if they don't exist

## Examples

See `example.py` for comprehensive usage examples including:
- Basic usage patterns
- Error handling
- Performance logging
- Different log levels

## Dependencies

This package uses only the Python standard library. No external dependencies are required. 