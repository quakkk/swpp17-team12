import re
from urllib.parse import urlparse, parse_qs

blog_urls = {
    'naver': re.compile('blog.naver.com$'),
    'daum': re.compile('blog.daum.net$'),
    'egloos': re.compile('\w+[.]egloos[.]com$'),
    'tistory': re.compile('\w+[.]tistory[.]com$')
}


def check_domain(url):
    parsed_url = urlparse(url)
    for domain, match in blog_urls.items():
        if match.match(parsed_url.netloc):
            return domain
    return None


def check_title(url):
    parsed_url = urlparse(url)
    domain = check_domain(url)
    if domain == 'naver':
        return parsed_url.path.split('/')[1]
    elif domain == 'daum':
        return parsed_url.path.split('/')[1]
    elif domain == 'egloos':
        return parsed_url.netloc.split('.')[0]
    elif domain == 'tistory':
        return parsed_url.netloc.split('.')[0]
    else:
        return None


def check_blog_url(url):
    domain = check_domain(url)
    title = check_title(url)
    if domain == 'naver':
        return "http://blog.naver.com/{}".format(title)
    elif domain == 'daum':
        return "http://blog.daum.net/{}".format(title)
    elif domain == 'egloos':
        return "http://{}.egloos.com".format(title)
    elif domain == 'tistory':
        return "http://{}.tistory.com".format(title)
    else:
        return None
