import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table
from parser.entity import Review
from sqlalchemy import create_engine
from sqlalchemy import inspect


def increaseReviews(driver, reviews):
    driver.execute_script("arguments[0].scrollIntoView(true);", reviews[-1])
    time.sleep(1.2)
    reviews_container = driver.find_element(By.CLASS_NAME, "business-reviews-card-view__reviews-container")
    reviews = reviews_container.find_elements(By.CLASS_NAME, "business-review-view")
    return reviews


def get_organization_reviews(org_id: int = 1124715036):
    engine = create_engine("postgresql://postgres:admin@localhost:5433/yandexMaps")
    metadata = MetaData()

    if inspect(engine).has_table("reviews"):
        Table("reviews", metadata).drop(bind=engine)

    Review.__table__.create(bind=engine, checkfirst=True)

    session = sessionmaker(bind=engine)()

    organization_url = f"https://yandex.ru/maps/org/yandeks/{org_id}/reviews/"
    driver = webdriver.Chrome()
    driver.get(organization_url)

    time.sleep(2)  # Some time to load the page

    # Block that loads all reviews
    reviews_container = driver.find_element(By.CLASS_NAME, "business-reviews-card-view__reviews-container")
    reviews = reviews_container.find_elements(By.CLASS_NAME, "business-review-view")
    reviews_counter = len(reviews)
    if reviews_counter > 49:
        while True:
            reviews = increaseReviews(driver, reviews)
            if len(reviews) - reviews_counter < 30:
                break
            reviews_counter = len(reviews)

    # TODO Remove double parsing
    reviews_selenium_elems = set()
    for review_elem in driver.find_elements(by=By.XPATH, value='//*[@class="business-review-view__info"]'):
        reviews_selenium_elems.add(review_elem)

    # Converting to objects
    data = []
    for review_elem in reviews_selenium_elems:
        new_review = Review()
        new_review.parse_information(review_elem=review_elem)
        data.append(new_review.__dict__)
        session.add(new_review)
        session.commit()

    print(str(len(reviews_selenium_elems)) + " entities successfully added!")

    driver.quit()
    engine.dispose()


if __name__ == '__main__':
    pass
