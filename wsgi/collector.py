import os
from socorro.app.generic_app import main
from socorro.collector.collector_app import CollectorApp
from socorro.webapi.servers import ModWSGIServer
import socorro.collector.collector_app

from configman import (
    ConfigFileFutureProxy,
    environment
)

if os.path.isfile('/etc/socorro/collector.ini'):
    config_path = '/etc/socorro'
else:
    config_path = ModWSGIServer.get_socorro_config_path(__file__)

# invoke the generic main function to create the configman app class and which
# will then create the wsgi app object.
main(
    CollectorApp,  # the socorro app class
    config_path=config_path,
    values_source_list=[
        ConfigFileFutureProxy,
        environment
    ]
)

application = socorro.collector.collector_app.application
