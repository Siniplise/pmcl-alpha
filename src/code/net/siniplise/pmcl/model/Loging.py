import logging

from colorlog import ColoredFormatter

cache_path = ""

log_style = {
    "DEBUG": 'white',
    "INFO": 'green',
    "WARNING": 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

main_logger = logging.getLogger("MainLogger")

main_logger.setLevel(logging.DEBUG)

FileFmt = logging.Formatter(
    "Time:[%(asctime)s] at [%(filename)s].[%(funcName)s]:%(lineno)d Level:[%(levelname)s] --> %(message)s")

ConsoleFmt = "%(log_color)sTime:[%(log_color)s%(asctime)s] at [%(log_color)s%(filename)s].[%(log_color)s%(funcName)s]:%(log_color)s%(lineno)d [%(log_color)s%(levelname)s] --> %(log_color)s%(message)s"
DateFmt = '20%y.%b.%d - %H:%M:%S'
console_formatter = ColoredFormatter(
    fmt=ConsoleFmt,
    datefmt=DateFmt,
    reset=True,
    log_colors=log_style,
    secondary_log_colors={},
    style='%'
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(console_formatter)
console_handler.setLevel(logging.INFO)
main_logger.addHandler(console_handler)

file_handler = logging.FileHandler(filename=cache_path + "\\pmcl.log")
file_handler.setFormatter(FileFmt)
file_handler.setLevel(logging.DEBUG)
main_logger.addHandler(file_handler)

main_logger.info("Logger Loaded")
