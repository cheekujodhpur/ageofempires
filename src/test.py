import viz
import simulation

results = simulation.simulate()
viz.var_vs_time_multi(results,'population')
viz.var_vs_var_multi(results,'food','wood')