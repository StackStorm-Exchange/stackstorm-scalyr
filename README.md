# Scalyr integration pack

Integrate with Scalyr - blazing fast logs management and observability, [www.scalyr.com](https://www.scalyr.com)

### Configuration
Copy the example configuration in scalyr.yaml.example to /opt/stackstorm/configs/scalyr.yaml and edit as required:

    cp scalyr.yaml.example /opt/stackstorm/configs/scalyr.yaml

Find or create your api token at [https://www.scalyr.com/keys](https://www.scalyr.com/keys)
Place an API token to the config file at `/opt/stackstorm/configs/scalyr.yaml`. It should look like this:


    url: "https://www.scalyr.com/api"
    token: "73ce4a24b5553d2e482ea8a8500e71b8ad4554f-"

Reload configuration. Remember to do it every time when config is changed.

    st2ctl reload --register-configs

### Actions

... description coming soon


### Configuring Scalyr Alarms to trigger StackStorm actions

... descriptions coming soon
