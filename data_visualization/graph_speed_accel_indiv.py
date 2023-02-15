import json

FILE = "../1_130/groundtruth_scene_1_130__cajoles_processed.json"


with open(FILE) as file:
    data = json.load(file)

# graphs speed and acceleration information of car trajectories
def graph_speed_accel(ax1,ax2):
    speed = []
    accel = []
    ttl = 0
    for set in data:
        ttl+=1

        # just concatenate the lists
        for i in range(1, len(set['speed'])):
            speed.append(set['speed'][i][2])
            if i == 1: continue
            accel.append(set['accel'][i][2])
    ax1.hist(speed)
    ax1.set_ylabel("# of trajectories")
    ax1.set_xlabel("speed (mph)")
    ax1.set_title("distribution of speeds")

    ax2.hist(accel)
    ax2.set_ylabel("# of trajectories")
    ax2.set_xlabel("acceleration (f/s^2)")
    ax2.set_title("distribution of accelerations")



# prints data regarding lane change information for car trajectories
def print_lane_changes(ax):
    ttl, ttl_lc, num_changes = 0,0,0
    lanes = {'E1': 0, 'E2': 0, 'E3': 0, 'E4': 0, 'E5': 0, 'E6': 0, 'W1': 0, 'W2': 0,
                      'W3': 0, 'W4': 0, 'W5': 0, 'W6': 0}
    for set in data:
        ttl += 1
        if len(set['lane_changes']) > 1:
            ttl_lc += 1
            num_changes += len(set['lane_changes']) - 1
        for chng in set['lane_changes']:
            lanes[chng[0]] += 1

    names = list(lanes.keys())
    values = list(lanes.values())

    ax.bar(range(len(lanes)), values, tick_label=names)
    ax.set_ylabel("# of trajectories")
    ax.set_xlabel("lane of highway")
    ax.set_title("distribution of lane locations")
