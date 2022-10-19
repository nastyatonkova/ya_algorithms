"""
Timofey decided to organize a sports programming contest to find talented interns. 
The tasks are chosen, the participants are registered, and the tests are written. 
It remains to think how the winner will be determined at the end of the competition.

Each participant has a unique login. When the contest is over, 
two indices are bound to it: the number of solved problems Pi and the size of the penalty Fi. 
The penalty is for unsuccessful attempts and time spent on the task.

Timofey decided to sort the results table in the following way: 
if you compare two participants, the one who solved more problems will be higher. 
If the number of solved problems is equal, the participant with the smaller penalty goes first. 
If the fines are the same, the first will be the one with the first login in alphabetical order.

Timothy ordered sweatshirts for the winners and went to the store the day before to pick them up. 
In his absence, he instructed you to implement a quick sort algorithm for the results table. 
Since Timothy likes sports programming and doesn't like to waste RAM, your sorting implementation can't consume O(n) 
extra memory for intermediate data (this modification of quick sorting is called "in-place")

Implementation of in-place quicksort which utilizes pivot
as the last element in the array list.
It has a pointer to keep track of the elements greater than the pivot.
At the very end of partition() function, the pointer is swapped
with the pivot to come up with a "sorted" array relative to the pivot.

With quicksort() function, we will be utilizing partition() method to obtain
the pointer at which the left values are all smaller
than the number at pointer index and vice versa for the right values.

Input data forms array in the following way:
 - minus value of solved tasks
 - value of penalty
 - login
Sorting this array from min to max solves the task.
"""


from collections import namedtuple


def quicksort(array, comparator):
    def _partition(low, high, array):
        # last element will be the pivot and the first element the pointer
        pivot, ptr = array[high], low
        for student in range(low, high):
            if comparator(array[student], pivot):
                # swapping values greater than the pivot to the front
                array[student], array[ptr] = array[ptr], array[student]
                ptr += 1
        # finally swapping the last element with the pointer indexed number
        array[ptr], array[high] = array[high], array[ptr]
        return ptr


    def _quicksort(low, high, array):
        # terminating condition for recursion
        if len(array) == 1:
            return array
        if low < high:
            mid = _partition(low, high, array)
            # recursively sorting the left values
            _quicksort(low, mid-1, array)
            # recursively sorting the right values
            _quicksort(mid+1, high, array)
        return array

    _quicksort(0, len(array)-1, array)


if __name__ == '__main__':
    def comparator(first_student, second_student):
        if first_student.score > second_student.score:
            return True
        elif first_student.score < second_student.score:
            return False
        else:
            if first_student.penalty < second_student.penalty:
                return True
            elif first_student.penalty > second_student.penalty:
                return False
            else:
                if first_student.login < second_student.login:
                    return True
                else:
                    return False


    num_students = int(input())
    students = [None] * num_students
    Student = namedtuple('Student', 'login score penalty')
    for i in range(num_students):
        login, score, penalty = input().split()
        students[i] = Student(login, int(score), int(penalty))
    quicksort(students, comparator)
    for student in students:
        print(student.login)
