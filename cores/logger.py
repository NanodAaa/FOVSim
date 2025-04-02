import logging
import logging.handlers
import os
import sys

class Logger:
    def __init__(self, log_dir='logs', log_file='app.log', level=logging.DEBUG, max_bytes=10*1024*1024, backup_count=5):
        """
        初始化日志模块
        :param log_dir: 日志存放目录
        :param log_file: 日志文件名
        :param level: 日志级别
        :param max_size: 单个日志文件最大大小（字节）
        :param backup_count: 备份的日志文件数量
        """
        if not os.path.exists(log_dir):
            try:
                os.mkdir(log_dir)
            except FileNotFoundError:
                sys.exit('Error when creating log directory! -- FileNotFoundError')
            except PermissionError:
                sys.exit('Error when creating log directory! -- PermissionError')
            
        self.logger = logging.getLogger('AppLogger')
        self.logger.setLevel(level)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s")
        file_handler = logging.handlers.RotatingFileHandler(
            os.path.join(log_dir, log_file), maxBytes=max_bytes, backupCount=backup_count, encoding='utf-8',
        )
        file_handler.setFormatter(formatter)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
    def debug(self, msg):
        self.logger.debug(msg)
    
    def info(self, msg):
        self.logger.info(msg)
    
    def warning(self, msg):
        self.logger.warning(msg)
    
    def error(self, msg):
        self.logger.error(msg)
    
    def critical(self, msg):
        self.logger.critical(msg)