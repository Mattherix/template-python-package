"""Main file of the package"""
from .log import init_logger

logger = init_logger('main.log')


# Your code here
def add(a, b):
    """Add two number.

    This return the Addition of these 2 numbers.
    You will never want to use this function because it's just an example.

    :Example:

    >>> add(1, 1)
    2

    :param a: First Number
    :type a: float
    :param b: Second Number
    :type b: float
    :return: The addition of the two number
    :rtype: float
    """
    logger.debug('add(%s, %s)' % (a, b))
    return a + b
