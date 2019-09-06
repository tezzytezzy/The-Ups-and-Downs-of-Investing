def count_ups_and_downs(input_file):
    is_second_line = False
    data_points = []

    with open (input_file, 'rt', encoding="ISO-8859-1") as myfile:
        for a_line in myfile:
            if is_second_line is False:
                total_count_ups_downs = a_line.split()
                total_count = total_count_ups_downs[0]
                up_count = total_count_ups_downs[1] 
                down_count = total_count_ups_downs[2]

                is_second_line = True
            else:
                data_points = a_line.split()

    return total_count, up_count, down_count, data_points

def calc_ups_and_downs(total_count, up_count, down_count, data_points):



    

if __name__ == "__main__":
    calc_ups_and_downs(count_ups_and_downs("1.in"))
    calc_ups_and_downs(count_ups_and_downs("2.in"))



