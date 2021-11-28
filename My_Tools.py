import random
def get_headers():
    headers = [
        {"user - agent":"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en - us)AppleWebKit/534.50(KHTML, likeGecko) Version / 5.1Safari / 534.50"},
        {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1"},
        {"user-agent":"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11"},
        {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"},
        {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53"}
    ]
    return random.choice(headers)
