# import requests
#
# def get_proxy():
#     return requests.get("http://127.0.0.1:5010/get/").json()
#
# def delete_proxy(proxy):
#     requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
#
# # your spider code
#
# def getHtml():
#     retry_count = 3
#     # proxy = get_proxy().get("proxy")
#     # proxy = '192.168.31.30'
#
#     # print(proxy)
#     while retry_count > 0:
#         print(retry_count)
#         try:
#             html = requests.get('https://www.zhihu.com/api/v4/topics/19564862/feeds/top_activity?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Canswer_type%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.paid_info%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=10&after_id=00.00000', timeout=5)
#             # 使用代理访问
#             # html = requests.get('https://www.baidu.com', proxies={"http": "https://{}".format(proxy)},timeout=5)
#
#             return html
#         except Exception:
#             retry_count -= 1
#     # 删除代理池中代理
#     delete_proxy(proxy)
#     return None
#
# if __name__ == '__main__':
#     html = getHtml()
#     print(html.text)


import socket


def get_host_ip():
    """
    get host ip address
    获取本机IP地址

    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def is_port_used(ip, port):
    """
    check whether the port is used by other program
    检测端口是否被占用

    :param ip:
    :param port:
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        return True
    except OSError:
        return False
    finally:
        s.close()


# 测试
if __name__ == '__main__':
    host_ip = get_host_ip()
    print(host_ip)
    # print(is_port_used(host_ip, 80))
#
