

def count_ups_and_downs(input_file):
    is_second_line = False
    data_points = []

    with open (input_file, 'rt', encoding="ISO-8859-1") as myfile:
        for a_line in myfile:
            if is_second_line is False:
                total_count_ups_downs = a_line.split()
                total_idx_count = int(total_count_ups_downs[0]) - 1
                peak_count = int(total_count_ups_downs[1])
                valley_count = int(total_count_ups_downs[2])

                is_second_line = True
            else:
                data_points = a_line.split()

    calc_ups_and_downs(total_idx_count, peak_count, valley_count, data_points)

def calc_ups_and_downs(total_idx_count, peak_count, valley_count, data_points):
    peak_counter = 0
    valley_counter = 0
    stop_pos = 0

    # Peak
    stop_pos = total_idx_count - (peak_count - 1)
    for idx in range(peak_count - 1, stop_pos):
        if is_continous_up_or_down(data_points, idx, peak_count, True, False) and is_continous_up_or_down(data_points, idx, peak_count, False, False):
            peak_counter += 1

    # Valley
    stop_pos = total_idx_count - (valley_count - 1)
    for idx in range(valley_count - 1, stop_pos):
        if is_continous_up_or_down(data_points, idx, valley_count, True, True) and is_continous_up_or_down(data_points, idx, valley_count, False, True):
            valley_counter += 1

    print("peak = {0}, valley = {1}".format(peak_counter, valley_counter))


    # peak_data_point_sum = False
    # valley_data_point_sum = False
    
    # is_peak_condition_met_sofar = False
    # is_valley_condition_met_sofar = False

    # for idx in total_idx_count:
    #     if total_idx_count[idx+1] > total_idx_count[idx]:
    #         peak_data_point_sum += 1            
    #         is_peak_condition_met_sofar = True if (peak_data_point_sum >= peak_count) else False
    #     elif total_idx_count[idx+1] < total_idx_count[idx]:
    #         valley_data_point_sum +=1
    #         is_valley_condition_met_sofar = True if (valley_data_point_sum >= valley_count) else False
            

def is_continous_up_or_down(data_points, current_idx, data_point_count, idx_count_to_right = True, up = True):
    #idx_count_to_right = 1 if up else -1
    
    is_continous_up_or_down = False
    stop_idx = current_idx + data_point_count - 1 if idx_count_to_right else current_idx - data_point_count + 1

    for idx in range(current_idx, stop_idx):
        #data_point_pos + 1 +1 because the starting idx wont' get counted
        
        if idx_count_to_right and up:
            is_continous_up_or_down = True if data_points[idx + 1] > data_points[idx] else False
        elif (not idx_count_to_right) and up:
            is_continous_up_or_down = True if data_points[idx - 1] > data_points[idx] else False
        elif idx_count_to_right and (not up):
            is_continous_up_or_down = True if data_points[idx] > data_points[idx + 1] else False
        elif (not idx_count_to_right) and (not up):
            is_continous_up_or_down = True if data_points[idx - 1] > data_points[idx] else False

    return is_continous_up_or_down


if __name__ == "__main__":
    count_ups_and_downs("1.in")
    count_ups_and_downs("2.in")