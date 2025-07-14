import logging
import logging.handlers
import os
import sys
from typing import Optional


class LoggerConfig:
    """Configuration class for logger settings"""
    
    def __init__(self, 
                 name: str = "app",
                 level: str = "INFO",
                 log_file: Optional[str] = None,
                 max_bytes: int = 10 * 1024 * 1024,  # 10MB
                 backup_count: int = 5,
                 format_string: Optional[str] = None,
                 console_output: bool = True,
                 file_output: bool = True):
        
        self.name = name
        self.level = getattr(logging, level.upper(), logging.INFO)
        self.log_file = log_file
        self.max_bytes = max_bytes
        self.backup_count = backup_count
        self.console_output = console_output
        self.file_output = file_output
        
        # Default format string
        if format_string is None:
            self.format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        else:
            self.format_string = format_string


class Logger:
    """Reusable logger class with file rotation and multiple output options"""
    
    def __init__(self, config: LoggerConfig):
        self.config = config
        self.logger = self._setup_logger()
    
    def _setup_logger(self) -> logging.Logger:
        """Setup and configure the logger"""
        logger = logging.getLogger(self.config.name)
        logger.setLevel(self.config.level)
        
        # Clear any existing handlers
        logger.handlers.clear()
        
        # Create formatter
        formatter = logging.Formatter(self.config.format_string)
        
        # Console handler
        if self.config.console_output:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(self.config.level)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
        
        # File handler with rotation
        if self.config.file_output and self.config.log_file:
            # Ensure log directory exists
            log_dir = os.path.dirname(self.config.log_file)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir)
            
            file_handler = logging.handlers.RotatingFileHandler(
                self.config.log_file,
                maxBytes=self.config.max_bytes,
                backupCount=self.config.backup_count
            )
            file_handler.setLevel(self.config.level)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        return logger
    
    def debug(self, message: str, **kwargs):
        """Log debug message"""
        self.logger.debug(message, **kwargs)
    
    def info(self, message: str, **kwargs):
        """Log info message"""
        self.logger.info(message, **kwargs)
    
    def warning(self, message: str, **kwargs):
        """Log warning message"""
        self.logger.warning(message, **kwargs)
    
    def error(self, message: str, **kwargs):
        """Log error message"""
        self.logger.error(message, **kwargs)
    
    def critical(self, message: str, **kwargs):
        """Log critical message"""
        self.logger.critical(message, **kwargs)
    
    def exception(self, message: str, **kwargs):
        """Log exception with traceback"""
        self.logger.exception(message, **kwargs)


def create_logger(name: str = "app",
                 level: str = "INFO",
                 log_file: Optional[str] = None,
                 console_output: bool = True,
                 file_output: bool = True,
                 max_bytes: int = 10 * 1024 * 1024,
                 backup_count: int = 5,
                 format_string: Optional[str] = None) -> Logger:
    """
    Convenience function to create a logger with common configurations
    
    Args:
        name: Logger name
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Path to log file (optional)
        console_output: Whether to output to console
        file_output: Whether to output to file
        max_bytes: Maximum size of log file before rotation
        backup_count: Number of backup files to keep
        format_string: Custom format string for log messages
    
    Returns:
        Logger instance
    """
    config = LoggerConfig(
        name=name,
        level=level,
        log_file=log_file,
        max_bytes=max_bytes,
        backup_count=backup_count,
        format_string=format_string,
        console_output=console_output,
        file_output=file_output
    )
    return Logger(config)


# Pre-configured logger instances for common use cases
def get_console_logger(name: str = "app", level: str = "INFO") -> Logger:
    """Get a logger that only outputs to console"""
    return create_logger(name=name, level=level, console_output=True, file_output=False)


def get_file_logger(name: str = "app", 
                   log_file: str = "app.log", 
                   level: str = "INFO") -> Logger:
    """Get a logger that only outputs to file"""
    return create_logger(name=name, level=level, log_file=log_file, 
                        console_output=False, file_output=True)


def get_full_logger(name: str = "app", 
                   log_file: str = "app.log", 
                   level: str = "INFO") -> Logger:
    """Get a logger that outputs to both console and file"""
    return create_logger(name=name, level=level, log_file=log_file, 
                        console_output=True, file_output=True) 