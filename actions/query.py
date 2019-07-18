from st2common.runners.base_action import Action
import requests
import json

__all__ = ['QueryAction']


class QueryAction(Action):
    def run(self, **kwargs):

        self.logger.info("Called with {0}".format(kwargs))

        url = self.config['url'] + "/query"
        kwargs['queryType'] = 'log'
        if kwargs['token'] is None:
            kwargs['token'] = self.config['token']
        if not kwargs['filter']:
            kwargs['filter'] = ""

        results = requests.request('POST', url=url, data=json.dumps(kwargs))

        ok = results.ok
        self.logger.debug("Request {}, fetched {}".format("OK" if ok else "failed", results.text))
        results = results.json() if ok else results.text
        self.logger.info("Fetched {}".format(results))
        return (ok, results)
