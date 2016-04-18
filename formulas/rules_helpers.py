# -*- coding:utf-8 -*-


_MONTHS_LIST = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]


def month_of_date(date_str):
    """
    >>> month_of_date('12/12/2012')
    'December'
    >>> month_of_date('02/11/2012')
    'November'
    >>> month_of_date('02/01/2012')
    'January'
    """
    return _MONTHS_LIST[int(date_str.split('/')[1]) - 1]
