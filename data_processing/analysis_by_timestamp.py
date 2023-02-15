import json



# extracts and organizes timestamp data into timestamp-based discrete lane categories with car
# information (x-coordinate, y-coordinate, car id)
def organize_by_car(data):
    lanes = {'E1': [0, 12], 'E2': [12, 24], 'E3': [24, 36], 'E4': [36, 48], 'E5': [48, 60],
             'E6': [60, 72], 'W1': [72, 84], 'W2': [84, 96], 'W3': [96, 108], 'W4': [108, 120],
             'W5': [120, 132], 'W6': [132, 144]}
    for set in data:
        by_car = {'E1': [], 'E2': [], 'E3': [], 'E4': [], 'E5': [], 'E6': [], 'W1': [], 'W2': [],
                    'W3': [], 'W4': [], 'W5': [], 'W6': []}
        pos = set['position']
        id = set['id']
        for i in range(len(id)):
            x, y = pos[i]
            carid = list(id[i].values())[0]
            for key, ranges in lanes.items():
                # sorting by lane
                if ranges[0] < y <= ranges[1]:
                    by_car[key].append((x, y, carid))
                    break
        set['by car'] = by_car


# organizes timestamp-based lane category data by x-coordinate of car
def organize_by_x(data):
    # where each set is a timestamp
    for set in data:
        # where key is lane number, values are list of cars on lane
        for key, values in set['by car'].items():

            # sort each lane in the time stamp by x position
            values.sort(key = lambda x:x[0])


# transforms data into dictionary of car trajectories and includes leader vehicle of each car at
# each time stamp
def get_car_leaders(data, by_car_by_timestamp):
    for set in data:
        time = set['timestamp']

        for key, values in set['by car'].items():

            # where car is each car on lane
            for idx, car in enumerate(values):

                car_id = car[2]

                if idx == len(values) - 1:
                    leader = None
                else:
                    leader = values[idx + 1][2]

                if not by_car_by_timestamp.get(car_id):
                    by_car_by_timestamp[car_id] = {'leader': []}

                cur_car_leader = by_car_by_timestamp[car_id]['leader']
                cur_car_leader.append([leader, time])
            # print(by_car_by_timestamp[car_id]['leader'])


# combines information of individual car leaders and transforms data to be (car leader, beginning
# time stamp, end time stamp)
def combine_car_leaders(by_car_by_timestamp):

    # for each car trajectory
    for car, items in by_car_by_timestamp.items():
        cur_leader = None
        start_time = None
        lst = []

        # for each leader w/in car trajectory
        for idx, leader in enumerate(items['leader']):
            # if no values
            if start_time == None:
                cur_leader = leader[0]
                start_time = leader[1]

            # leader change, add prev leader tuple
            elif leader[0] != cur_leader or idx == len(items['leader']) - 1:
                lst.append((cur_leader, start_time, leader[1]))
                cur_leader = leader[0]
                start_time = leader[1]

        items['leader'] = lst


# calculates follow distance of cars from leaders, and store as car_id: (leader, distance, time)
# finds follow distance every second to avoid taking up too much space
def calculate_follow_distance(data, by_car_by_timestamp):
    counter = 0
    for set in data:
        if counter%25 != 0:
            counter += 1
            continue
        time = set['timestamp']
        for key, values in set['by car'].items():
            # key, values in format lane, [(x pos, y pos, car id), ...]
            for idx, value in enumerate(values[:-1]):
                x = value[0]
                car = value[2]
                leader = values[idx+1][2]
                leader_x = values[idx+1][0]
                if not by_car_by_timestamp[car].get('follow distance'):
                    by_car_by_timestamp[car]['follow distance'] = []
                by_car_by_timestamp[car]['follow distance'].append((leader, leader_x-x, time))
        counter += 1

# dumps data organized by trajectory into a new json file
def create_newfile_dictionary(new_file, by_car_by_timestamp):
    new_file.write(json.dumps(by_car_by_timestamp, indent=4))


# runs the functions in analysis_by_timestamp
def main(data):
    by_car_by_timestamp = {}

    organize_by_car(data)
    organize_by_x(data)
    get_car_leaders(data, by_car_by_timestamp)
    combine_car_leaders(by_car_by_timestamp)
    calculate_follow_distance(data, by_car_by_timestamp)

    with open('../1_130/groundtruth_scene_1_130__cajoles_transformed_by_car.json', 'w') as new_file:
        create_newfile_dictionary(new_file, by_car_by_timestamp)

