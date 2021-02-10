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

__all__ = ['QueryAction']


class QueryAction(BaseScalyrAction):
    def run(self, filter="", maxCount=100, startTime=None, endTime=None, columns=None,
            priority="low", api_url=None, token=None):
        data = {
            "queryType": "log",
            "filter": filter,
            "maxCount": maxCount,
        }

        if startTime:
            data["startTime"] = startTime

        if endTime:
            data["endTime"] = startTime

        ok, result = self._send_api_request(path="/query", data=data, api_url=api_url,
                                            token=token)
        return (ok, result)
