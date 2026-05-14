import logging
from functools import wraps

logger = logging.getLogger(__name__)


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'function name: {func.__name__}')
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        arguments = ", ".join(args_repr + kwargs_repr)
        if len(arguments) != 0:
            logging.info(f'arguments: ({arguments})')
        value = func(*args, **kwargs)
        return value
    return wrapper
