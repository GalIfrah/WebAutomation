from enum import Enum


class LocatorsTypes(Enum):

    ID = 'id'
    XPATH = 'xpath'
    NAME = 'name'
    LINK = 'link'
    CSS_SELECTOR = "css_selector"
    CLASS_NAME = "class_name"
