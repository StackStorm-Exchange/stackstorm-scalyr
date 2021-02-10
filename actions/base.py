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

if False:
    from typing import Optional
    from typing import Tuple

import copy
import json

import requests

from st2common.runners.base_action import Action

__all__ = ["BaseScalyrAction"]


class BaseScalyrAction(Action):
    def _send_api_request(self, path, data, api_url=None, token=None):
        # type: (str, dict, Optional[str], Optional[str]) -> Tuple[bool, dict]
        """
        Perform Scalyr API request and return the parsed response.
        """
        if api_url:
            self.logger.debug("Using api_url which was passed as parameter to the action")
        else:
            self.logger.debug("using url from the pack config")

        if token:
            self.logger.debug("Using token which was passed as parameter to the action")
        else:
            self.logger.debug("using token from the pack config")

        api_url = api_url or self.config["url"]
        token = token or self.config["token"]

        data["token"] = token

        data_to_log = copy.copy(data)

        if "token" in data_to_log:
            data_to_log["token"] = "************"

        url = api_url + path
        serialized_data = json.dumps(data)

        self.logger.debug("Using API endpoint: {}".format(api_url))
        self.logger.debug("Using API operation URL: {}".format(url))
        self.logger.debug("Using POST body data {}".format(serialized_data))

        headers = {"Content-Type": "application/json"}
        response = requests.request('POST', url=url, headers=headers, data=serialized_data)
        ok = response.ok

        self.logger.debug("Request {}, fetched {} ({})".format("OK" if ok else "failed",
                                                               response.text, response.status_code))

        try:
            result = response.json()
        except Exception:
            result = response.text

        self.logger.debug("Fetched {}".format(result))
        return (ok, result)
