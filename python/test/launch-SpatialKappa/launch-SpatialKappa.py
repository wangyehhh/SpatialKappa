import SpatialKappa
import os

sk = SpatialKappa.SpatialKappa()
kappa_sim = sk.kappa_sim("ms", True)
kappa_sim.loadFile("caPump.ka")
kappa_sim.runToTime(0.01)
print kappa_sim.getObservation("P")
print kappa_sim.getObservation("ca")
