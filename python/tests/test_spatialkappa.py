import SpatialKappa
import os
import unittest

class TestSpatialKappa(unittest.TestCase):
    
    def setUp(self):
        self.sk = SpatialKappa.SpatialKappa()
        self.sim = self.sk.kappa_sim("ms", True)
        self.sim.loadFile("caPump.ka")

    def test_runForTime(self):
        self.sim.runForTime(100.0, False)
        obs = self.sim.getObservation("ca")
        self.assertTrue(isinstance(obs, float))
        self.assertEqual(self.sim.getTime(), 100.0)

    def test_addTransition(self):
        ca_agent = self.sim.getAgent("ca")
        tran = self.sim.addTransition("TEST", ca_agent, 0.0)
        self.assertEqual(str(tran), "'TEST' : [] -> [[ca(x)]] @ 0.0")
        self.sim.setTransitionRate("TEST", 100.0)
        self.assertEqual(str(tran), "'TEST' : [] -> [[ca(x)]] @ 100.0")

if __name__ == '__main__':
    unittest.main()
