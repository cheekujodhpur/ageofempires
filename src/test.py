import viz
import simulation

results = simulation.simulate()
viz.phase_2D(results,'time','population')
viz.phase_2D(results,'food','wood')
