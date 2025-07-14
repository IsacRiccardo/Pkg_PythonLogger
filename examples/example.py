#!/usr/bin/env python3
"""
Example usage of the logger package
This demonstrates how to use the logger in different scenarios
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from logger import (
    create_logger,
    get_console_logger,
    get_file_logger,
    get_full_logger,
    LoggerConfig,
    Logger
)

def example_basic_usage():
    """Basic logger usage examples"""
    print("=== Basic Logger Usage Examples ===")
    
    # 1. Console-only logger
    console_logger = get_console_logger("MyApp", "DEBUG")
    console_logger.info("This message goes to console only")
    console_logger.debug("Debug message")
    console_logger.warning("Warning message")
    
    # 2. File-only logger
    file_logger = get_file_logger("MyApp", "app.log", "INFO")
    file_logger.info("This message goes to file only")
    file_logger.error("Error message in file")
    
    # 3. Full logger (console + file)
    full_logger = get_full_logger("MyApp", "full_app.log", "DEBUG")
    full_logger.info("This message goes to both console and file")
    full_logger.critical("Critical error!")
    
    # 4. Custom configuration
    config = LoggerConfig(
        name="CustomApp",
        level="DEBUG",
        log_file="custom.log",
        max_bytes=5*1024*1024,  # 5MB
        backup_count=3,
        format_string='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
    )
    custom_logger = Logger(config)
    custom_logger.info("Custom formatted message")
    custom_logger.exception("Exception with traceback")

def example_error_handling():
    """Example of error handling with logger"""
    print("\n=== Error Handling Examples ===")
    
    logger = get_full_logger("ErrorExample", "error_example.log")
    
    try:
        # Simulate an error
        result = 10 / 0
    except ZeroDivisionError as e:
        logger.error(f"Division by zero error: {e}")
        logger.exception("Full exception details:")
    
    try:
        # Simulate another error
        data = {"key": "value"}
        print(data["nonexistent_key"])
    except KeyError as e:
        logger.error(f"Key error: {e}")
        logger.warning("Attempted to access non-existent key")

def example_performance_logging():
    """Example of performance logging"""
    print("\n=== Performance Logging Examples ===")
    
    logger = get_console_logger("Performance", "DEBUG")
    
    import time
    
    logger.info("Starting performance test")
    start_time = time.time()
    
    # Simulate some work
    time.sleep(0.1)
    
    elapsed = time.time() - start_time
    logger.info(f"Performance test completed in {elapsed:.3f} seconds")
    
    if elapsed > 0.05:
        logger.warning(f"Performance test took longer than expected: {elapsed:.3f}s")
    else:
        logger.debug("Performance test completed within expected time")

def example_different_log_levels():
    """Example showing different log levels"""
    print("\n=== Log Level Examples ===")
    
    # Create logger with DEBUG level
    debug_logger = get_console_logger("DebugExample", "DEBUG")
    
    debug_logger.debug("This is a debug message")
    debug_logger.info("This is an info message")
    debug_logger.warning("This is a warning message")
    debug_logger.error("This is an error message")
    debug_logger.critical("This is a critical message")
    
    print("\nNow with INFO level (debug messages won't show):")
    info_logger = get_console_logger("InfoExample", "INFO")
    
    info_logger.debug("This debug message won't show")
    info_logger.info("This info message will show")
    info_logger.warning("This warning message will show")

if __name__ == "__main__":
    print("Logger Package Examples")
    print("=" * 50)
    
    example_basic_usage()
    example_error_handling()
    example_performance_logging()
    example_different_log_levels()
    
    print("\n" + "=" * 50)
    print("Examples completed. Check the generated log files for output.") 