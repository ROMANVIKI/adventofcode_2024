created a function named red_nosed_reports()

initialized a var called total_safe_reports to just record the number of safe reports

used a while loop:

    inside that look we initialized a var named report_input that holds the input func
    if that var == 'done':
        we have to break the while loop so we know that we have reached the end of the input data
    try block :
        we have to get the data in uniform order so that we can manipulate those data to verify whether it is meeting the requirements or not

            1. we used a map func to map to those int to a list inside the map we used the split() func to split and append those int to the initialized var as integer.
            
            2. here we have have called a function to verify that the list is safe or not:
                at first we initialized a var called is_increasing = None so we can track whether the sequence is inc or dec.
            
            3. Then a for loop that loops inside the list that we provided as arg in the new func.
            
            4. we get diff var val by sub the first and second items in the list and so on by current_list[i] - current_list[i+1] 
            
            5. As per the constraints we the values should not be less than 1 and greater than 3: 
            
            6. then we have to specify whther the seq is increasing or decreasing.
            
            7. if diff is less than 0:
                we set the is_increasing val to False, because its decreasing.
            
            8. for the diff which is greater than 0:
                we set is_increasing to True.
            

            9. if diff is less than 0 and the next val or any other val in that list is trying to change the var val to True it just return False

            same for the increasing seq as well.
