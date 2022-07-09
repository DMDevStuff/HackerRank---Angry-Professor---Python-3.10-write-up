##    https://www.hackerrank.com/challenges/angry-professor/problem

##    A Discrete Mathematics professor has a class of students. Frustrated
##    with their lack of discipline, the professor decides to cancel class if
##    fewer than some number of students are present when class starts.
##    Arrival times go from on time (arrivalTime <= 0) to arrived late (arrivalTime > 0).

##    Given the arrival time of each student and a threshhold number of
##    attendees, determine if the class is cancelled.

##### ##### ##### #####

#   Given variable names have been changed:
#   k => required_attendees
#   a => arrival_times

#   I think it is important to note that the list of arrival_times
#   is not in order, as one might reasonably assume it is.  Though sorting
#   does not help us find a solution faster and actually slows us down.

##### ##### ##### #####

#   O(n)
#   n is the number of elements in arrival_times
#   Algo:
#       Iterate through the arrival_times and keep track
#       of the number of students who are on time.
#       If the number of students who are on time ever equals
#       required_attendees we can return 'NO'
#       If we make it all the way through the list of
#       arrival_times without meeting the required_attendees
#       threshold then we return 'YES'

def angryProfessor(required_attendees, arrival_times):
    
    students_on_time = 0
    
    for student in arrival_times:
        
        if student <= 0:
            
            students_on_time += 1
            
            if students_on_time == required_attendees:
                
                return 'NO'
            
    return 'YES'
