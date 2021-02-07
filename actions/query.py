import json
import copy

import requests

from st2common.runners.base_action import Action

__all__ = ['QueryAction']


class QueryAction(Action):
    def run(self, filter="", maxCount=100, startTime=None, endTime=None, columns=None,
            priority="low", token=None):
        data = {
            "queryType": "log",
            "filter": filter,
            "maxCount": maxCount,
        }

        if startTime:
            data["startTime"] = startTime

        if endTime:
            data["endTime"] = startTime

        if not token:
            data["token"] = self.config["token"]

        kwargs_to_log = copy.copy(data)

        if "token" in kwargs_to_log:
            kwargs_to_log["token"] = "************"

        self.logger.info("Called with {0}".format(kwargs_to_log))

        url = self.config['url'] + "/query"

        headers = {"Content-Type": "application/json"}
        results = requests.request('POST', url=url, headers=headers, data=json.dumps(data))

        ok = results.ok
        self.logger.debug("Request {}, fetched {}".format("OK" if ok else "failed", results.text))
        results = results.json() if ok else results.text
        self.logger.info("Fetched {}".format(results))
        return (ok, results)
