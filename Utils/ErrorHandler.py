


class ErrorsHandler(object):


    # GENERAL ERRORS
    SUCCESS = 'success'
    TIMEOUT_ERROR = 'time out error'


    # TEXT ERRORS
    TEXT_IS_WRONG = 'text is wrong & not equals to the expected one... please check the screen shot for that test & the error msg text on the html report'


    # CONNECT ERRORS
    LOGIN_ERROR = 'there was problem with the user login'
    LOGOUT_ERROR = 'there was logout error'


    # CHOOSE LOCATION ERRORS
    LOCATION_CHOOSING_ERRORS = 'there was an error with choosing the location...please see the error msg text on the html reporting'

    # WALLET ERRORS
    ADD_PAYMENT_ERROR = 'error while adding the credit card'
    MISSING_CARDS = ' cards are missing'
    CARD_IS_NOT_DEFAULT = 'this card doesnt contain the "V" mark or the locator on config was changed, please check the screen shot for that test'
    MISSING_SUPPORTED_CARDS = 'number of card is lower then the on expected... please check to screen shot for that issue'

    # CHECKOUT ERRORS


    # ELEMENTS ERRORS
    NO_SUCH_ELEMENT = 'no such element... the element you was trying to reach is ether missing or the locator on config is wrong, please check the screen shot for that test'
    ELEMENT_NOT_VISIBLE = 'element is not visible... the element you was trying to assert is ether missing or the locator on config is wrong, please check the screen shot for that test'
    ELEMENT_EXIST = 'the element is exist'
    ELEMENT_IS_NONE = 'element is none... or that it not exist or the config locator is wrong'
    ELEMENT_NOT_ASSIGNED_YET = 'the element you trying to get access to is not assign to any value yet, probably locator on config is wrong, please check the screen shot for that test '

    # CHECKOUT ERRORS
    GENERAL_CHECKOUT_ERROR = 'there was an error during checkout, please see the error msg text on the html reporting'

