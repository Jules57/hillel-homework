class Url:
    def __init__(self, scheme='', authority='', path='', query='', fragment=''):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    # def __eq__(self, other):
    #     total_url = self.scheme + "://" + self.authority + "/" + self.path + "?" + self.query + "#" + self.fragment
    #     return total_url == other

    def __str__(self):
        total_url = self.scheme + "://" + self.authority
        if self.path != '':
            total_url = total_url + "/" + "/".join(self.path)
        if self.query != '':
            str_query = ''
            for k in self.query:
                str_query = str_query + k + '=' + self.query[k] + '&'
            str_query = str_query[:-1]
            total_url = total_url + "?" + str_query
        if self.fragment != '':
            total_url = total_url + "#" + self.fragment
        return total_url

    def __eq__(self, other):
        return str(self) == other


class HttpsUrl(Url):
    def __init__(self, scheme='https', *args, **kwargs):
        super().__init__(scheme=scheme, *args, **kwargs)


class HttpUrl(Url):
    def __init__(self, scheme='http', *args, **kwargs):
        super().__init__(scheme=scheme, *args, **kwargs)


class GoogleUrl(HttpsUrl):
    def __init__(self, authority='google.com', *args, **kwargs):
        super().__init__(authority=authority, *args, **kwargs)


class WikiUrl(HttpsUrl):
    def __init__(self, authority='wikipedia.org', *args, **kwargs):
        super().__init__(authority=authority, *args, **kwargs)


assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'

