#!/usr/bin/env python

import viz
import simulation

results = simulation.simulate()
viz.multi_phase_2D(results,'time','population','population2')
