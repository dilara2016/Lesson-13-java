tour_locations = ["Los Angeles", "Bangkok", "Istanbul","London", "Toronto"] # The list to search 
target_city = "New York City" # the target value

#Linear search algorithm
def linear_search(search_list, target_value):
    matches = []
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:#if target value found in the list
            matches.append(idx)#add indxe in matches list

    if not matches: #if the element is not in the matches list
        ValueError("{0} is not in the list".format(target_value)) # raise the error

    else: #Otherwise return the matches list
        return matches # With indexes where element is present

tour_stops = linear_search(tour_locations, target_city) #call the function
print("{} is present in the following locations in the list: {}".format(target_city, tour_stops))