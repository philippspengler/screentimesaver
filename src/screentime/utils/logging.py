import logging
import json

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'timestamp': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'module': record.module,
            'message': record.getMessage()
        }
        return json.dumps(log_record)

def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG) 


    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG) 


    formatter = JsonFormatter()
    console_handler.setFormatter(formatter)


    logger.addHandler(console_handler)

    return logger
