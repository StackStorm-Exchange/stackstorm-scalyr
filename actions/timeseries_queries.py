import json
import copy

import requests

from st2common.runners.base_action import Action

__all__ = ['TimeseriesQueryAction']


class TimeseriesQueryAction(Action):
    def run(self, queries, token=None):

        data = {
            "queries": []
        }

        for query in queries:
            # Each item can contain: filter, function, startTinme, endTime, buckets, priority
            query_item = {}

            if query.get("filter", None):
                query_item["filter"] = query["filter"]

            if query.get("function", None):
                query_item["function"] = query["function"]

            if query.get("startTime", None):
                query_item["startTime"] =  query["startTime"]

            if query.get("endTime", None):
                query_item["endTime"] =  query["endTime"]

            if query.get("buckets", None):
                query_item["buckets"] =  query["buckets"]

            if query.get("priority", None):
                query_item["priority"] =  query["priority"]

            data["queries"].append(query_item)

        if not token:
            data["token"] = self.config["token"]

        kwargs_to_log = copy.copy(data)

        if "token" in kwargs_to_log:
            kwargs_to_log["token"] = "************"

        self.logger.info("Called with {0}".format(kwargs_to_log))

        url = self.config['url'] + "/timeseriesQuery"

        headers = {"Content-Type": "application/json"}
        response = requests.request('POST', url=url, headers=headers, data=json.dumps(data))

        ok = response.ok
        self.logger.debug("Request {}, fetched {}".format("OK" if ok else "failed", response.text))

        try:
            result = response.json()
        except Exception:
            result = response.text

        self.logger.info("Fetched {}".format(result))
        return (ok, result)
