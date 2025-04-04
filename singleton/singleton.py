import urllib.parse
import urllib.request


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class URLFetcher(metaclass=SingletonType):
    def __init__(self):
        self.urls = []

    def fetch(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                # print(the_page)
                urls = self.urls
                urls.append(url)
                self.urls = urls

    def dump_url_registry(self):
        return ', '.join(self.urls)


def is_singleton(verify_class):
    # f1 = verify_class()
    # f2 = verify_class()
    # print(f1 is f2)
    print(verify_class() is verify_class())


def main() -> None:
    is_singleton(URLFetcher)

    MY_URLS = ['http://www.voidspace.org.uk', 'http://google.com', 'http://python.org',
               'https://www.python.org/error', ]

    fetcher = URLFetcher()
    for url in MY_URLS:
        try:
            fetcher.fetch(url)
        except Exception as e:
            print(f"{url}: {e}")

    print('-------')
    done_urls = fetcher.dump_url_registry()
    print(f'Done URLs: {done_urls}')


if __name__ == "__main__":
    main()
