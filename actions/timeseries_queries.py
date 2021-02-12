# Copyright 2020 The StackStorm Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from base import BaseScalyrAction

__all__ = ['TimeseriesQueryAction']


class TimeseriesQueryAction(BaseScalyrAction):
    def run(self, queries, api_url=None, token=None):
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
                query_item["startTime"] = query["startTime"]

            if query.get("endTime", None):
                query_item["endTime"] = query["endTime"]

            if query.get("buckets", None):
                query_item["buckets"] = query["buckets"]

            if query.get("priority", None):
                query_item["priority"] = query["priority"]

            data["queries"].append(query_item)

        ok, result = self._send_api_request(path="/timeseriesQuery", data=data, api_url=api_url,
                                            token=token)
        return (ok, result)
