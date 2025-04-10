import abc


class ResourceContent:
    """
    Define the abstraction's interface.
    Maintain a reference to an object which represents the Implementor.
    """

    def __init__(self, imp):
        self._imp = imp

    def show_content(self, path):
        self._imp.fetch(path)


class ResourceContentFetcher(metaclass=abc.ABCMeta):
    """
    Define the interface (Implementor) for implementation classes
    that help fetch content.
    """

    @abc.abstractmethod
    def fetch(self, path):
        pass


class URLFetcher(ResourceContentFetcher):
    """
    Implement the Implementor interface and define its concrete
    implementation.
    """

    def fetch(self, path):
        import urllib.request
        from urllib.error import URLError, HTTPError

        # path is an URL
        try:
            req = urllib.request.Request(path)
            with urllib.request.urlopen(req) as response:
                if response.code == 200:
                    the_page = response.read()
                    print(the_page)
        except (URLError, HTTPError) as e:
            print(f"Fail to fetch data from URL '{path}': {e}")


class LocalFileFetcher(ResourceContentFetcher):
    """
    Implement the Implementor interface and define its concrete
    implementation.
    """

    def fetch(self, path):
        # path is the filepath to a text file
        try:
            with open(path) as f:
                print(f.read())
        except FileNotFoundError:
            print(f"File '{path}' not found.")


def create_file_txt(filename):
    with open(filename, 'w') as f:
        f.write(
            'Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.')


def main() -> None:
    FILENAME = 'file.txt'
    create_file_txt(FILENAME)

    url_fetcher = URLFetcher()
    iface = ResourceContent(url_fetcher)
    iface.show_content('http://python.org')

    print('===================')

    url_fetcher = URLFetcher()
    iface = ResourceContent(url_fetcher)
    iface.show_content('https://python.ogr')

    print('===================')

    localfs_fetcher = LocalFileFetcher()
    iface = ResourceContent(localfs_fetcher)
    iface.show_content('file.txt')

    print('===================')

    localfs_fetcher = LocalFileFetcher()
    iface = ResourceContent(localfs_fetcher)
    iface.show_content('wrong_file.txt')


if __name__ == "__main__":
    main()
