name = "SpatialKappa"

import py4j.java_gateway as jg
import os

class SpatialKappa:
    """Runs gateway to SpatialKappa"""

    port = None
    gateway = None
    gateway_client = None

    def __init__(self, classpath=''):
        skjar_file = 'SpatialKappa-v2.1.1.jar'
        antlrjar_file = 'ant-antlr-3.2.jar'
        skjar_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'share', 'SpatialKappa', skjar_file)
        antlrjar_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'share', 'SpatialKappa', antlrjar_file)
        classpath = os.pathsep.join((classpath, skjar_path, antlrjar_path))
        self.port = jg.launch_gateway(classpath=classpath, die_on_exit=False)
        self.gateway_client = jg.GatewayClient(port=self.port)
        self.gateway = jg.JavaGateway(self.gateway_client, auto_convert=True)

    def kappa_sim(self, time_units, verbose):
        ks = self.gateway.jvm.org.demonsoft.spatialkappa.api.SpatialKappaSim(time_units, verbose)
        return ks

    def __del__(self):
        self.gateway_client.shutdown_gateway()
        
