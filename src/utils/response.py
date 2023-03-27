from http.cookiejar import strip_quotes, http2time


def get_set_cookie(response):
    """
    输入reponse 获取set_cookie

    :param response: 发起请求后的响应
    :return: 含cookies字典的列表
    """
    known_attrs = ("expires", "domain", "path", "secure", "version", "port", "max-age")
    cookie_headers = response.headers.get("Set-Cookie", "")
    if not cookie_headers:
        return ""
    result = []
    for cookie in cookie_headers.split(","):
        pairs = {}
        for index, param in enumerate(cookie.split(";")):
            param = param.strip()
            key, sep, val = param.partition("=")
            key = key.strip()
            if not key:
                if index == 0:
                    break
                else:
                    continue
            val = val.strip() if sep else None
            if index != 0:
                lc = key.lower()
                if lc in known_attrs:
                    key = lc
                if key == "version":
                    if val is not None:
                        val = strip_quotes(val)
                elif key == "expires":
                    if val is not None:
                        val = http2time(strip_quotes(val))
            pairs[key] = val
        result.append(pairs)
    return result
