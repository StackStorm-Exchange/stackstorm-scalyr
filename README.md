# Scalyr integration pack

Integrate with Scalyr - blazing fast logs management and observability, [www.scalyr.com](https://www.scalyr.com)

## Configuration

Copy the example configuration in scalyr.yaml.example to /opt/stackstorm/configs/scalyr.yaml and edit as required:

    cp scalyr.yaml.example /opt/stackstorm/configs/scalyr.yaml

Find or create your api token at [https://www.scalyr.com/keys](https://www.scalyr.com/keys)
Place an API token to the config file at `/opt/stackstorm/configs/scalyr.yaml`. It should look like this:

    url: "https://app.scalyr.com/api"
    # Or https://app.ap.scalyr.com/api for Scalyr EU environment
    # url: "https://app.eu.scalyr.com/api"
    token: "73ce4a24b5553d2e482ea8a8500e71b8ad4554f-"

Reload configuration. Remember to do it every time when config is changed.

    st2ctl reload --register-configs

You can also use a different API url or token for a specific action execution (aka override
default values from the config on action execution basis), by passing ``api_url`` / ``token``
parameter to the action.

## Actions

* ``scalyr.query`` - Run a Scalyr search query.
* ``scalyr.power_query`` - Run a Scalyr power query.
* ``scalyr.timeseries_query`` - Run a single Scalyr timeseries query.
* ``scalyr.timeseries_queries`` - Run multiple Scalyr timeseries queries.

## Configuring Scalyr Alarms to trigger StackStorm actions

... descriptions coming soon
