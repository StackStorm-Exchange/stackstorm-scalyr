import json
import copy

import requests

from st2common.runners.base_action import Action

__all__ = ['PowerQueryAction']


class PowerQueryAction(Action):
    def run(self, query, startTime=None, endTime=None, columns=None, priority="low", token=None):
        data = {
            "query": query,
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

        url = self.config['url'] + "/powerQuery"

        headers = {"Content-Type": "application/json"}
        response = requests.request('POST', url=url, headers=headers, data=json.dumps(data))

        ok = response.ok
        self.logger.debug("Request {}, fetched {}".format("OK" if ok else "failed", response.text))

        try:
            result = response.json()
        except Exception:
            result = response.text

        self.logger.debug("Fetched {}".format(result))
        return (ok, result)
