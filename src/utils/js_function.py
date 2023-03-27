import re


def clear_function(js_function_str: str) -> str:
    """

    :param js_function_str: javascript:view('', '');
    :return:
    """
    return re.sub(r";|javascript:", "", js_function_str)
