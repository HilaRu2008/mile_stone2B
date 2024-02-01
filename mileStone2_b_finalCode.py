
def list_of_all_info_log(path_file):

    with open(path_file, "r") as file_to_read:  # read the file

        # get rid of the first lines (not part of the info)
        for title_line in range(3):
            file_to_read.readline()

        # add the lins as elements to list
        list_of_info = file_to_read.readlines()

    return list_of_info






def relevant_info_log_file(file_path):

    """ this func isolates the relevant info out of every line of data in the log_file to a list of lists

    :param path_file: the path of the file we want to read (log file)
    :type path_file: String
    :return: a list of lists containing each the relevant data we need from every action in the log
    :rtype: List
    """

    """""
    with open(path_file, "r") as file_to_read:  # read the file

        # get rid of the first lines (not part of the info)
        for title_line in range(3):
            file_to_read.readline()

        # add the lins as elements to list
        list_of_info = file_to_read.readlines()
    """
    list_of_info = list_of_all_info_log(file_path)


    list_of_relevant_info = []

    # get all the relevant info to a sub list
    for line in list_of_info:

        sub_lst_of_relevant_info = []

        image_name = line[:line.index(" ")]  # gets the name of the action
        sub_lst_of_relevant_info.append(image_name)  # add the image_name as the first element in the sub list of relevant info

        mem_usage = line.split(" ")[-1][:-2]
        # to isolate the mem_usage, i created a list with key = " ", so the last element will be the relevant info
        # the [-1] means: take the last element in the list (the mem usage)
        # the [:-1] means: take the last parts (\n) and (K) out of the last element we isolated

        # remove any comma from the mem usage
        mem_usage = mem_usage.replace(',', '')

        # add the image_name as the first element in the sub list of relevant info
        sub_lst_of_relevant_info.append(mem_usage)

        # now: sub_lst_of_relevant_info = [image_name, mem_usage]

        list_of_relevant_info.append(sub_lst_of_relevant_info)  # add every sub list to the list of ALL relevant info

    return list_of_relevant_info





def relevant_info_common_processes_file(path_file):

    """ this func reads the file common processes and excort the relevant info to a sub list inside big list

    :param path_file: the path of the file we want to open (common_processes)
    :return: a list of lists containing each the relevant data (image_name, mem_usage)
    """

    with open(path_file, "r") as file_to_read:  # read the file
        list_of_info = file_to_read.readlines()
        # print(list_of_info)

        list_of_relevant_info = []
        # go over every line of info in the file
        for line in list_of_info:
            sub_lst_of_relevant_info = []

            # separate every line of data to a list of the image_name (index 0) and mem usage(index 1). key = ' '
            image_name = line.split(" ")[0]
            mem_usage = line.split(" ")[1][:-2]  # the last elements with the '\n' and 'K' removed

            # remove any coma from the mem usage
            mem_usage = mem_usage.replace(',', '')

            # append the name and usage to a sub list of the relevant data
            sub_lst_of_relevant_info.append(image_name)
            sub_lst_of_relevant_info.append(mem_usage)
            list_of_relevant_info.append(sub_lst_of_relevant_info)


    return list_of_relevant_info


def data_comparison (log_list_of_relevant_info, common_list_of_relevant_info, list_of_log_all_info): # , list_of_log_all_info
    """ this function goes over every name of process, compares them,
     and if they are the same than it ckecks if the memory of the process from the log list is sus

    :param log_list_of_relevant_info: the list of relevant info from the log file
    :param common_list_of_relevant_info: the list of relevant info from the common processes file
    :param list_of_log_all_info: the list containing the full data of every process
    :return: a list of all the sus processes found (full info and not just the "relevant"
    """

    sus_processes = []

    # goes over every process in the list of relevant info (log) + the ist of relevant info (common), and compares the names
    for log_action_index in range(len(log_list_of_relevant_info)):
        for common_action in common_list_of_relevant_info:
            # comapre the names of each process
            if log_list_of_relevant_info[log_action_index][0] == common_action[0]:
                # check if the log process memory is sus
                if int(log_list_of_relevant_info[log_action_index][1]) > int(common_action[1]) + 50000:
                    # if the process is sus, add it to a list of sus processes
                    sus_processes.append(list_of_log_all_info[log_action_index])


                    """ if i want to print the sus processes only with the relevant info:
                    
    for log_action in log_list_of_relevant_info:
        for common_action in common_list_of_relevant_info:
            if log_action[0] == common_action[0]:
                if int(log_action[1]) > int(common_action[1]) + 50000:
                    # index_of_full_sus_log = log_list_of_relevant_info.index
                    sus_processes.append(log_action)

                    """


    return sus_processes



def main():

    log_file_path = r"C:\Users\naama\PycharmProjects\pythonProject\log_file.txt"
    common_processes_file_path = r"C:\Users\naama\PycharmProjects\pythonProject\common_processes.txt"
    text1 = r"C:\Users\naama\PycharmProjects\pythonProject\1.txt"
    text2 = r"C:\Users\naama\PycharmProjects\pythonProject\2.txt"
    text3 = r"C:\Users\naama\PycharmProjects\pythonProject\3.txt"
    lst_of_logs_to_ckeck = [log_file_path, text1, text2, text3]

    # go over in loop and check every log (without common file)
    for log_path in lst_of_logs_to_ckeck:

        print("\n\n",f" --- computer log path: {log_path} ---")


        # all info from the log file
        # print("\n============== all log file info ============ \n")
        # print(list_of_all_info_log(log_path))

        # the relevant info from the log file
        # print("\n================ log file relevant info ============== \n")
        # print(relevant_info_log_file(log_path))

        # the relevant info from common processes
        # print("\n\n============= common relevant file info ================\n")
        # print(relevant_info_common_processes_file(common_processes_file_path))


        # parameters we need for the sus processes list (func)
        log_list_info_relevant = relevant_info_log_file(log_path)  # the relevant info from log file
        common_list_info_relevant = relevant_info_common_processes_file(common_processes_file_path)  # the relevant info from common file
        list_of_all_info_in_log_file = list_of_all_info_log(log_path)  # the list of all info from the log file

        # the sus processes list
        list_of_suspisious_processes = data_comparison(log_list_info_relevant, common_list_info_relevant, list_of_all_info_in_log_file)  # a list of all sus processes


        if len(list_of_suspisious_processes) == 0:  # if sus processes not found
            print("\nthis computer is clean!")
        else:  # if sus processes found
            print("\n\n============ the sus processes ============ \n")  # prints all the suspisious processes found from the list of sus processes
            for i in list_of_suspisious_processes:
                print(i)



if __name__ == "__main__":
    main()
