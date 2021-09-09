from bs4 import BeautifulSoup
import requests


class Brightime:
    def __init__(self, start_url, model_to_find):
        self.model_to_find = model_to_find
        self.pages = []
        self.prices = {}

        content = Brightime.__load_page(start_url)
        self.__parse(content)

        pages = Brightime.__find_pages(content)
        for page_url in pages:
            content = Brightime.__load_page(page_url)
            self.__parse(content)

    def display(self):
        for model in self.prices:
            if len(self.prices[model]) > 0:
                self.prices[model].sort()
                print('Ref {model} price range from {start} to {end}'.format(model=model, start=self.prices[model][0],
                                                                             end=self.prices[model][-1]))
            else:
                print('No price found for ref', self.model_to_find)

    def __is_finding(self, watch_model):
        for m in self.model_to_find:
            if m in watch_model:
                return m

        return None

    @staticmethod
    def __find_pages(content):
        page_numbers = content.find('ul', class_="page-numbers")

        if page_numbers:
            pages = page_numbers.find_all('a')[:-1]
            return [page['href'] for page in pages]

        return []

    @staticmethod
    def __load_page(url):
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.content, 'html.parser')
        return None

    def __parse(self, content):
        watches = content.find_all('li', class_=["product-item", "catalog_mode"])
        for watch in watches:
            model = watch.find('h4').string
            price = watch.find('span', class_="amount").contents[1]

            if model is None:
                model = watch.find('h4').a.contents[-1]

            model_to_find = self.__is_finding(model)
            if model_to_find:
                if model_to_find not in self.prices:
                    self.prices[model_to_find] = []

                self.prices[model_to_find].append(price)
