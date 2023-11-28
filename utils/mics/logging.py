import logging

logging.basicConfig(
    format= '%(filename)-16s [F:%(funcName)-15s()] [L:%(lineno)-3s] #%(levelname)-4s [%(asctime)s]'
            ' %(message)s',
    level=logging.INFO,
    datefmt="%H:%M:%S",
    # level=logging.DEBUG,
)
