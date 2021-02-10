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
    def run(self, filter, function=None, startTime=None, endTime=None, buckets=None,
            priority="low", api_url, token=None):
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

        ok, result = self._send_api_request(path="/timeseriesQuery", data=data, api_url=api_url,
                                            token=token)
        return (ok, result)
