#!/usr/bin/env python

import viz
import simulation

results = simulation.simulate()
viz.phase_2D(results,'time','population','food')
