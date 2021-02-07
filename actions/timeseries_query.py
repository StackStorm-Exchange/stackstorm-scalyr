import json
import copy

import requests

from st2common.runners.base_action import Action

__all__ = ['TimeseriesQueryAction']


class TimeseriesQueryAction(Action):
    def run(self, filter, function=None, startTime=None, endTime=None, buckets=None,
            priority="low", token=None):
        data = {
            "queries": [{}]
        }

        if filter:
            data["queries"][0]["filter"] = filter

        if function:
            data["queries"][0]["function"] = function

        if startTime:
            data["queries"][0]["startTime"] = startTime

        if endTime:
            data["queries"][0]["endTime"] = startTime

        if buckets:
            data["queries"][0]["buckets"] = buckets

        if priority:
            data["queries"][0]["priority"] = priority

        if not token:
            data["token"] = self.config["token"]

        kwargs_to_log = copy.copy(data)

        if "token" in kwargs_to_log:
            kwargs_to_log["token"] = "************"

        self.logger.info("Called with {0}".format(kwargs_to_log))

        url = self.config['url'] + "/timeseriesQuery"

        headers = {"Content-Type": "application/json"}
        results = requests.request('POST', url=url, headers=headers, data=json.dumps(data))

        ok = results.ok
        self.logger.debug("Request {}, fetched {}".format("OK" if ok else "failed", results.text))
        results = results.json() if ok else results.text
        self.logger.info("Fetched {}".format(results))
        return (ok, results)
