import matplotlib as mpl
import matplotlib.pyplot as plt

import graph_speed_accel_indiv as by_car
import graph_analysis_by_timestamp as by_timestamp

fontsize = 5

figure = plt.figure()

plt.rcParams.update({'font.size': 8})
plt.subplots_adjust(left = 0.125, right = 0.9, bottom = 0.1, top = 0.9, wspace=0.2, hspace=0.5)

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
i2 = figure.add_subplot(gs[2,1])
by_car.graph_speed_accel(i1, i2)


i3 = figure.add_subplot(gs[3,0])
by_car.print_lane_changes(i3)

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
n = 5  # Keeps every 7th label
[l.set_visible(False) for (i,l) in enumerate(t1.xaxis.get_ticklabels()) if i % n != 0]

t2 = figure.add_subplot(gs[2,3])
by_timestamp.graph_follow_distance_change_distribution(t2)
[l.set_visible(False) for (i,l) in enumerate(t2.xaxis.get_ticklabels()) if i % n != 0]

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
