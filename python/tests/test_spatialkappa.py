import SpatialKappa
import os
import unittest
from py4j.protocol import * 

class TestSpatialKappa(unittest.TestCase):
    
    def setUp(self):
        self.sk = SpatialKappa.SpatialKappa()
        self.sim = self.sk.kappa_sim("ms", True)
        self.sim.loadFile("caPump.ka")

    def test_runForTime(self):
        self.sim.runForTime(100.0, False)
        self.assertEqual(self.sim.getTime(), 100.0)

    def test_addTransition(self):
        ca_agent = self.sim.getAgent("ca")
        tran = self.sim.addTransition("TEST", ca_agent, 0.0)
        self.assertEqual(str(tran), "'TEST' : [] -> [[ca(x)]] @ 0.0")
        self.sim.setTransitionRate("TEST", 100.0)
        self.assertEqual(str(tran), "'TEST' : [] -> [[ca(x)]] @ 100.0")

    def test_addAgent(self):
        obs = self.sim.getObservation("ca")
        self.assertTrue(isinstance(obs, float))
        ## Add an integer number of Ca ions specified as a float
        self.sim.addAgent('ca', 11.0) 
        obs2 = self.sim.getObservation("ca")
        self.assertEqual(obs2, obs + 11.0)
        ## Add an integer number of Ca ions specified as an integer
        self.sim.addAgent('ca', 10) 
        obs3 = self.sim.getObservation("ca")
        self.assertEqual(obs3, obs2 + 10)

        ## Somthing like this should work, but it doesn't.
        ## self.assertRaises(TypeError, random.shuffle, (1,2,3))
        ## Hence the hack below
        error = False
        try:
            self.sim.addAgent("ca", 11.5)
        except Py4JJavaError:
            error = True
        self.assertTrue(error)

    def test_addVariable(self):
        ca_agent = self.sim.getAgent("ca")
        self.sim.addVariable(ca_agent,  "x", "?")
        TotCa1 = self.sim.getVariable("TotCa")
        TotCa2 = self.sim.getVariable("ca(x)?")
        self.assertEqual(TotCa1, TotCa2)
        print TotCa1, TotCa2
        self.sim.runForTime(10.0, False)
        TotCa1 = self.sim.getVariable("TotCa")
        TotCa2 = self.sim.getVariable("ca(x)?")
        self.assertEqual(TotCa1, TotCa2)
        print TotCa1, TotCa2

    def test_addVariableMap(self):
        ## Create an error due to nonexistent site name
        error = False
        try:
            self.sim.addVariableMap({"ca": {"nonexistent_site_name": {"l": "?"}}}, 'test')
        except Py4JJavaError:
            error = True
        self.assertTrue(error)
        
        ## Create an error due to nonexistent site attribute
        error = False
        try:
            self.sim.addVariableMap({"ca": {"x": {"nonexistent_site_attribute": "?"}}}, 'test')
        except Py4JJavaError:
            error = True
        self.assertTrue(error)

        self.sim.addVariableMap({"ca": {"x": {"l": "?"}}}, 'TotCa2')
        TotCa1 = self.sim.getVariable("TotCa")
        TotCa2 = self.sim.getVariable("TotCa2")
        self.assertEqual(TotCa1, TotCa2)
        self.sim.addVariableMap({"ca": {"x": {"l": "1"}}, "P": {"x": {"l": "1"}}}, 'P-Ca2')
        PCa1 = self.sim.getVariable("P-Ca")
        PCa2 = self.sim.getVariable("P-Ca2")
        self.assertEqual(PCa1, PCa2)
        print PCa1, PCa2

if __name__ == '__main__':
    unittest.main()
