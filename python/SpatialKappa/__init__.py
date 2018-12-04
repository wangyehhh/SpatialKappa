name = "SpatialKappa"

import py4j.java_gateway as jg
import os

class SpatialKappa:
    """Runs Java gateway to SpatialKappa"""

    port = None
    gateway = None
    gateway_client = None

    count = 0
    "Count of SpatialKappa objects"
    
    def __init__(self, classpath='', redirect_stdout=None):
        """Create and return a gateway to a Java object with SpatialKappa in
        the classpath using py4j

        The distribution of SpatialKappa should contain the
        SpatialKappa jar file, so there should be no need to download
        it separately.
        
        Keyword arguments:
        classpath -- classpath to override the default values
        redirect_stdout -- Redirect stdout to this connection - see
          py4j.java_gateway.launch_gateway()

        """
        
        skjar_file = 'SpatialKappa-v2.1.2.jar'
        antlrjar_file = 'ant-antlr-3.2.jar'
        skjar_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'share', 'SpatialKappa', skjar_file)
        antlrjar_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'share', 'SpatialKappa', antlrjar_file)
        classpath = os.pathsep.join((classpath, skjar_path, antlrjar_path))
        self.id = SpatialKappa.count
        SpatialKappa.count = SpatialKappa.count + 1
        self.redirect_stdout = redirect_stdout
        self.port = jg.launch_gateway(classpath=classpath, die_on_exit=False, redirect_stdout=self.redirect_stdout)
        self.gateway_client = jg.GatewayClient(port=self.port)
        self.gateway = jg.JavaGateway(self.gateway_client, auto_convert=True)

    def kappa_sim(self, time_units, verbose, seed=None):
        """Create and return a SpatialKappa simulation. This is actually a Java object.

        Keyword arguments:
        time_units -- Time units of the simulation. Can be "s" (seconds)
          or "ms" (milliseconds)
        verbose -- If True, more output is printed to the connection
          specified by redirect_stdout of the parent SpatialKappa object
        seed -- Random seed

        The object created has the following methods:

        * loadFile(String kappaFileName) -- Load a SpatialKappa file "kappaFileName" into the simulation

        * getTime() -- Return time of SpatialKappa simulation

        * runUntilTime(float stepEndTime, boolean progress) -- Run
          simulation from current simulation time to "stepEndTime"
          (specified in "time_units" given when creating kappa_sim.
          Time progress shown if "progress" is True.

        * runForTime(float dt, boolean progress) -- Run simulation
          from current simulation time for another "dt" (specified in
          "time_units" given when creating kappa_sim. Time progress
          shown if "progress" is True.

        * getAgent(String name) -- Get an agent

        * isAgent(String name) -- Return True if "name" is an agent

        * getAgentMap(String agentName) -- Return map of agents as Python dict

        * agentList(dict agentsMap) -- General function to allow an
          AgentList to be created programmtically. This allows a
          variable to be set using the following syntax in python:

            {agent_name1: {site_name1: {"l": link_name, "s": state_name}, 
                           site_name2: {"l": link_name, "s": state_name}, ...}, 
             agent_name2: {site_name1: {"l": link_name, "s": state_name}, ...}, ...}
            
            e.g.:
              {"ca": {"x": {"l": "1"}}, "P": {"x": {"l": "1"}}}
              is equivalent to:
              Ca(x!1),P(x!1)

        * addAgent(String key, int value) -- Add "value" units of
          agent "key" in its default configuration
        
        * addAgent(String key, double value) -- Same as the addAgent
          with an int "value", but throws an error if non-int value
          given

        * setAgentInitialValue(String key, int value) -- Set initial
          "value" of agent "key" in its default configuration

        * setAgentInitialValue(String key, double value) -- Set
          initial "value" of agent "key" in its default configuration,
          type-safe for double

        * addVariable(String label, dict agentsMap) -- Create a
          variable "label" using the syntax as described in agentList()

        * addVariable(String label, float input) -- Create a
          variable "label" with value "input"

        * getVariable(String label) -- Get value of "label"

        * getVariables() -- Return variables. If "kappa_sim.verbose"
          is True, print values
        
        * getObservation(String key) -- get Observation "key"
        
        * addTransition(String label, dict leftSideAgents, dict rightSideAgents, float rate) -- 
          Create unidirectional transition labelled "label" with
          "leftSideAgents" and "rightSideAgents" specified using format
          described in agentsList() and propensity "rate"

        * setTransitionRateOrVariable(String label, float value) -- Set rate of
          Transition "label" or of Variable "label" to "value"

        * getTransition(String label) -- Get transition labeled "label"

        """
        ks = self.gateway.jvm.org.demonsoft.spatialkappa.api.SpatialKappaSim(time_units, verbose, seed)
        return ks

    def __del__(self):
        self.gateway_client.shutdown_gateway()
        SpatialKappa.count = SpatialKappa.count - 1

