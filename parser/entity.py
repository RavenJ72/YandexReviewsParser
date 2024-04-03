from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Review:
    def __repr__(self):
        return repr(self.__dict__)

    def __init__(self, **kwargs):
        self.dislike = None
        self.like = None
        self.review_text = None
        self.author = None
        self.review_rating = None
        self.datetime = None
        self.selenium_id = None

        for key, value in kwargs.items():
            setattr(self, key, value)

    def parse_information(self, review_elem: WebElement):
        self.selenium_id = review_elem.id
        # ISO 8601
        self.datetime = get_dict(
            review_elem,
            './/*[@class="business-review-view__date"]//*',
        )['datePublished'][0]

        self.review_rating = get_dict(
            review_elem,
            './/*[@itemtype="http://schema.org/Rating"]//*',
        )['ratingValue'][0]

        self.author = get_dict(
            review_elem,
            './/*[@itemtype="http://schema.org/Person"]//*'
        )['name'][1]

        self.review_text = review_elem.find_element(
            By.CLASS_NAME,
            "business-review-view__body-text"
        ).text

        self.like = review_elem.find_element(
            By.CSS_SELECTOR,
            ".business-reactions-view__container:first-child"
        ).text

        self.dislike = review_elem.find_element(
            By.CSS_SELECTOR,
            ".business-reactions-view__container:nth-child(2)"
        ).text


def get_dict(parent_element: WebElement, value: str) -> dict:
    return {
        meta.get_attribute("itemprop"):
            [
                meta.get_attribute("content"),
                meta.text,
            ]
        for meta in parent_element.find_elements(By.XPATH, value)
    }


if __name__ == '__main__':
    pass
