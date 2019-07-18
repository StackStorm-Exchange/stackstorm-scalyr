from st2common.runners.base_action import Action

__all__ = ['QueryAction']


class QueryAction(Action):
    def run(self, **kwargs):

        self.logger.info("Called with {0}".format(kwargs))

        # Call Scalyr API here.

        results = ["line1", "line2"]

        self.logger.info("Fetched {0}".format(results))
        return (True, results)
