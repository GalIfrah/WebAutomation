import requests

from Infrastructure.GenericPageObject import GenericPO
from Utils.ErrorHandler import ErrorsHandler


class browserStack:

    def changeTestStatus(self, newStatus, reason):

        sessionId = GenericPO.webDriver.remoteWebDriver.session_id

        headers = {
            'Content-Type': 'application/json',
        }

        data = '{"status":"' + newStatus + '", "reason":"' + reason + '"}'

        response = requests.put('https://api.browserstack.com/automate/sessions/' + sessionId + '.json',
                                headers=headers, data=data, auth=('galifrah3', '1qj7e4pdqqHiK941sDej'))
