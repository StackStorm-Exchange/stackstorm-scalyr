# Change Log

## v1.1.0

- Fix ``scalyr.query`` action so it works correctly. Also fix parameter name from
  ``fromTime`` / ``toTime`` to ``startTime`` / ``endTime`` and add new ``priority``
  and ``columns`` parameter.
- Add new ``scalyr.power_query`` action.
- Add new ``scalyr.timeseries_query`` action.
- Add new ``scalyr.timeseries_queries`` action.
- Add new action aliases.
- In addition to ``token`` also allow base API endpoint url to be overriden on action
  execution basis using ``api_url`` action parameter.

## 1.0.0

- Drop Python 2.7 support

## v0.0.1

- Initial release.
