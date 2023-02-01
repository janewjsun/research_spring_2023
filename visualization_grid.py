import matplotlib as mpl
import matplotlib.pyplot as plt
import json

import graph_analysis_by_timestamp as by_timestamp
FILE='groundtruth_scene_1_130__cajoles_transformed_by_car.json'

with open(FILE) as file:
    by_car_by_timestamp = json.load(file)

figure = plt.figure()

gs = mpl.gridspec.GridSpec(nrows=5, ncols=4, height_ratios=[1,1,3,3,3])

title = figure.add_subplot(gs[0,0:4])
title.set_axis_off()
title.text(0.47,0.5,"Plots", fontsize=20, color="#808080")


indiv_title = figure.add_subplot(gs[1,0:2])
indiv_title.text(0.3,0.5,"Individual Trajectories", fontsize=13, color="#808080")
indiv_title.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)

timestamp_title = figure.add_subplot(gs[1,2:4])
timestamp_title.text(0.3,0.5,"Timestamped Trajectories", fontsize=13, color="#808080")
timestamp_title.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)

# indiv
i1 = figure.add_subplot(gs[2,0])
i1.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
i2 = figure.add_subplot(gs[2,1])
i2.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
i3 = figure.add_subplot(gs[3,0])
i3.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
i4 = figure.add_subplot(gs[3,1])
i4.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
i5 = figure.add_subplot(gs[4,0])
i5.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
i6 = figure.add_subplot(gs[4,1])
i6.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)

#timestamp

t1 = figure.add_subplot(gs[2,2])
by_timestamp.graph_follow_distance_distribution(t1)

t2 = figure.add_subplot(gs[2,3])
by_timestamp.graph_follow_distance_change_distribution(t2)

t3 = figure.add_subplot(gs[3,2])
t3.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
t4 = figure.add_subplot(gs[3,3])
t4.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
t5 = figure.add_subplot(gs[4,2])
t5.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
t6 = figure.add_subplot(gs[4,3])
t6.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)

plt.show()
