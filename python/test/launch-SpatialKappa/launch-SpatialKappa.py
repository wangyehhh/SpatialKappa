import SpatialKappa
import os

sk = SpatialKappa.SpatialKappa()
sim = sk.kappa_sim("ms", True)
sim.loadFile("caPump.ka")

sim.runForDt(0.01)
print('Time: %4.3f. %5.0f molecules of P %5.0f molecules of Ca' % (sim.getTime(), sim.getObservation("P"), sim.getObservation("ca")))

sim.runToTime(0.1)
print('Time: %4.3f. %5.0f molecules of P %5.0f molecules of Ca' % (sim.getTime(), sim.getObservation("P"), sim.getObservation("ca")))

sim.runForDt(0.01)
print('Time: %4.3f. %5.0f molecules of P %5.0f molecules of Ca' % (sim.getTime(), sim.getObservation("P"), sim.getObservation("ca")))
