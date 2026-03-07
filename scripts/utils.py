import logging
import sys

def setup_logging():
    """
    Configura o sistema de logs para o pipeline.
    Mostra informações no terminal e salva em um arquivo local.
    """
    logger = logging.getLogger("data_pipeline")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)

    file_handler = logging.FileHandler('logs/pipeline.log')
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(stdout_handler)
        logger.addHandler(file_handler)

    return logger