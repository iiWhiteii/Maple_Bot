import time


    

def hash_map_tracker(pos0,pos1,pos2,pos3,pos4,pos5,pos6):
    hashmap = {} 
    empty_list1 = []
    empty_list2 = []
    empty_list3 = []
    empty_list4 = []
    empty_list5 = [] 
    empty_list6 = [] 
    empty_list7 = [] 
    start_time = time.time()

    for item in pos0:  
        empty_list1.append(item)
    hashmap['charc_position'] = empty_list1
    
    for item in pos1:
        empty_list2.append(item)
    hashmap['eye_of_time_pos'] = empty_list2

    for item in pos2:
        empty_list3.append(item)
    hashmap['eye_of_time_death_pos'] = empty_list3

    for item in pos3:
        empty_list4.append(item)
    hashmap['memory_monk_pos'] = empty_list4

    for item in pos4:
        empty_list5.append(item)
    hashmap['memory_monk_death_pos'] = empty_list5 

    for item in pos5:
        empty_list6.append(item)
    hashmap['charc_minimap_pos'] = empty_list6

    for item in pos6:
        empty_list7.append(item)
    hashmap['green circle'] = empty_list7




    return hashmap
    



        #print(hashmap)