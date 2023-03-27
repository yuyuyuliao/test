from utils.url_function import url_query_encode, url_query_to_dict


def ztb_transform(origin_file_url):
    """
    下载链接带downloadztbattach的是会进行跳转的下载链接
    如：/attach/downloadztbattach
    跳转的新链接为真实下载链接
    如：/attach/ztbAttachDownloadAction.action
    输入origin_file_url 为原始下载链接 其中的params参数用于新链接的参数
    新的链接多了ztbAttachDownloadAction.action?cmd=getContent&参数

    :param origin_file_url: 原始下载链接
    :return: true_file_url
    """
    params = origin_file_url.split("/")[-1]
    base_file_url = origin_file_url.replace(params, "")
    true_file_url = f"{base_file_url}ztbAttachDownloadAction.action?cmd=getContent&{url_query_encode(url_query_to_dict(origin_file_url))}"
    return true_file_url
