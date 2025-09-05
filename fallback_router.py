import logging
from telegram_alerts import send_test_message  # Reuse your existing alert function

class FallbackTelegramHandler(logging.Handler):
    def emit(self, record):
        try:
            log_entry = self.format(record)
            send_test_message(f"⚠️ Fallback Log:\n{log_entry}")
        except Exception as e:
            print(f"Logger failed silently: {e}")

def setup_fallback_logger():
    logger = logging.getLogger("fallback")
    logger.setLevel(logging.WARNING)
    handler = FallbackTelegramHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
