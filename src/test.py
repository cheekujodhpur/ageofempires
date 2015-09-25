import viz
import simulation

results = simulation.simulate()
viz.phase_3D(results,'population','food','wood')
viz.phase_2D(results,'food','wood')
