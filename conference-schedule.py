"""
A schedule has just been released for an upcoming tech conference. The schedule provides the start and end times of each of the presentations. Once a presentation has begun, no one can enter or leave the room. It takes no time to go from one presentation to another.
Determine the maximum number of presentations that can be attended by one person.

Example n =3
scheduleStart = [1, 1, 2]
scheduleEnd = [3, 2, 4]
Using O-based indexing, an attendee could attend any presentation alone, or both presentations 1 and 2.
Presentation 0 ends too late to be able to attend presentation 2 afterwards. The maximum number of presentations one person can attend is 2.

Function Description
Complete the function maxPresentations in the editor below.
maxPresentations has the following parameters): scheduleStart[n]: the start times of presentation i scheduleEnd[n]: the end times of presentation i
Returns:
int: the maximum number of presentations that can be attended by one person
"""

import os

def maxPresentations(scheduleStart, scheduleEnd):
    presentations = [(i, start, end) for i, (start, end) in enumerate(zip(scheduleStart, scheduleEnd))]
    
    presentations.sort(key=lambda x: x[2])
    
    count = 1
    
    last_end_time = presentations[0][2]
    
    for presentation in presentations[1:]:
        print(presentation)
        if presentation[1] >= last_end_time:
            count += 1
            last_end_time = presentation[2]  
    
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scheduleStart_count = int(input().strip())

    scheduleStart = []

    for _ in range(scheduleStart_count):
        scheduleStart_item = int(input().strip())
        scheduleStart.append(scheduleStart_item)

    scheduleEnd_count = int(input().strip())

    scheduleEnd = []

    for _ in range(scheduleEnd_count):
        scheduleEnd_item = int(input().strip())
        scheduleEnd.append(scheduleEnd_item)

    result = maxPresentations(scheduleStart, scheduleEnd)

    fptr.write(str(result) + '\n')

    fptr.close()
