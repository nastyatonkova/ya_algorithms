# **Yandex.Practicum. Sprint 13**

# Recursion and sorting
https://contest.yandex.ru/contest/24734/problems/

## A. Bracket generator.
A contest has been announced in Udotinski. You have to write the fastest implementation of a function 
that generates all correct bracket sequences of length n.
There is only one kind of parentheses: ( )

The function takes an integer n between 0 and 10 as input.

The function is to print all possible parentheses sequences of the given 
in lexicographical order.

## B. Combinations
On the keyboards of the old cell phones, each digit corresponded to several letters. Approximately like this:

2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'.

You know the order in which the phone buttons were pressed, not counting the repetitions. Type all combinations of letters that can be typed in this sequence of keystrokes.

A string consisting of digits 2-9 inclusive is fed to the input. The length of the string does not exceed 10 characters.

**Display all possible letter combinations separated by a space.**

## C. Subsequence
Vasya likes to play the game Sequence. 
You have two strings, and you need to figure out whether the first of them 
is a subsequence of the second one. When the strings are long enough, 
sometimes it's very hard to get an answer to this question just by looking at them. 
Help Vasya, write a function that solves this problem.

The first line contains string s.

The second line contains string t.

Both lines consist of small Latin letters, the length of the lines does not exceed 1000.

**Print True if s is a subsequence of t, otherwise print False.**

## G. Closet
Eulampia decided to keep only three colors in her closet: 
pink, yellow, and crimson. She wanted to sort the clothes by color. 
First should go pink, then yellow, 
and at the end, raspberry. Help Eulampia put her closet in order.

The first line contains the number of items in the closet: 
n - it does not exceed 10000. The next line contains an array, specifying the color 
for each item. Pink is 0, yellow is 1 and crimson is 2. 
**Help Eulampia arrange the items in her closet according to 
in accordance with her idea. **

## H. Big number.
In the evening the children decide to play the game "Big Number".
The numbers are given. They need to determine what is the biggest number that can be made out of them.

The first line contains n - the number of numbers. It does not exceed 100.
The second line contains n non-negative numbers, each of them not exceeding 1000. 
does not exceed 1000.

**You must print the largest number that can be made up of them.**

## J. Bubble
To choose the best algorithm to solve the problem, 
Gosha set out to study different sorting. Bubble sorting is next in line.

The algorithm is as follows (we sort in ascending order):
At each step, we go through the array in turn comparing pairs of neighboring 
elements. If an element at position i is greater than an element at position i+1, 
swap them. After the first iteration the largest element will be 
at the end of the array.

Pass through the array by performing the specified actions n - 1 times, or until, 
until at the next iteration there is no need in exchanges, 
that is, the array is already sorted.
Help Gosha write the code of the algorithm.

In the first line the number n - the length of the array - is given as input. 
n doesn't exceed 1000. The second line contains n numbers separated by spaces. 
Each of the numbers modulo does not exceed 1000.

**We need to output the numbers in sorted order, separated by spaces.**

## K. Merge Sorting
Gosha was given the task of writing a nice merge sorting. So Gaucher has to implement the merge function and merge_sort function separately.

The merge function takes two sorted arrays, merges them into one sorted array and returns it. If the required signature is of the form merge(array, left, mid, right), then the first array is given by the half-interval [left,mid] of the array, and the second one by the half-interval [mid,right) of the array.
The merge_sort function accepts some subarray to be sorted. The subarray is specified by a half-interval - its beginning and end. The function must sort the subarray passed to it, it returns nothing.
The merge_sort function splits the half-interval into two halves and recursively calls sorting separately for each one. The two sorted arrays are then merged into one using merge.

Note that it is the half-intervals [begin,end] that are passed to the function, i.e., the right end is not included. For example, if we call merge_sort(arr, 0, 4), where arr=[4,5,3,0,1,2], only the first four elements will be sorted, the modified array will look like arr=[0,3,4,5,1,2].

The array passed to the function consists of integers that do not exceed 109 modulo. The length of the sorted range does not exceed 10^5.  

## L. Two bicycles
Vasya decided to save up money for two identical bicycles - for himself and his sister. Vasya has a piggy bank into which he can add money every day (if he is financially able to do so, of course). In the process of saving he does not take money out of the piggy bank.

You have information about the growth of Vasya's savings - how much money he has in the piggy bank on each of the days.

Your task is to determine the value of the bike

- the first day on which Vasya could buy one bicycle,
- and the first day on which Vasya could buy two bikes.



The first line gives the number of days n, on which Vasya's savings were observed. 1 ≤ n ≤ 10^6.
The next line contains n non-negative integers. The numbers are in non-decreasing order. Each of the numbers does not exceed 10^6.
The third line contains a positive integer s - the cost of a bicycle. This number does not exceed 10^6.


**Two numbers should be printed - the numbers of days according to the problem. If the necessary amount is not found in the piggy bank, return -1 instead of the day number.**

## M. Golden mean
Each island in the Algosa archipelago has some number of people living on it, or the island is uninhabited 
(then there are 0 people living on the island). Let the i-th island have ai population. 
Timothy wanted to find the median among all values of the population.

Definition: The median of an array of numbers a_i 
is such a number that half of the numbers in the array are not larger than it, and the other half are not smaller. 
In general, the median of an array can be found by sorting the numbers and taking the average of them. If the number of numbers is even, 
take as the median the half-sum of the neighboring average numbers, (a[n/2] + a[n/2 + 1])/2.

Timothy already has separate data for the northern part of the archipelago and for the southern part, 
and the population values in each group are sorted in descending order.

Determine the median population for all the islands of Algos.

Hint: If n is the number of islands in the northern part of the archipelago and m islands 
in the southern part, your solution should work for O(log(n+m)).

## N. Flowerbeds
Eulampy wanted to have dandelion flowerbeds under her window. 
N gardeners were hired to do the work of preparing the land for the flowerbeds.
Each of the gardeners worked on a piece of land. 
The process was not very well organized, sometimes the same plot, 
or part of a plot could be tilled by several gardeners at once. 
A tilled plot of any size became a flowerbed. 
There could be no untreated gaps in the flowerbed.
It is necessary to define the borders of the resulting beds.

The first line contains the number of gardeners - n. 
The number of gardeners doesn't exceed 1000 The next n lines with a space 
are written the coordinates of the plots in the format:
start end Both numbers are integers, non-negative, and do not exceed 1000. 
start cannot be greater than end

** We want to print on a single line the coordinates of each of the resulting flowerbeds.
The data must appear in sorted order.**

# Final tasks
https://contest.yandex.ru/contest/24735/problems/

## A. Searching in a Broken Array
Alla made a mistake with the data structure. She decided to store the array in a circular 
buffer.
The problem was that the array was sorted. And it was possible to search 
in logarithmic time. Alla copied the data from the ring buffer 
to a regular array. But it is no longer a sorted array. 
Nevertheless, it should be possible to find an element in O(logn).

### Input format.

The first line contains the number n, the length of the array.
The second line contains a positive number k - the sought element.
n and k do not exceed 1000.
Then n positive integers are written on the line, separated by spaces, 
each of which does not exceed 1000.

### Output format.

Print the index of the element you are looking for in the array if it is found. Otherwise, print -1.

## B. Efficient Quick Sorting
Timofey decided to organize a sports programming contest to find talented trainees. Problems are chosen, participants are registered, tests are written. The only thing left to do is to figure out how the winner will be determined at the end of the competition.
Each participant has a unique login. When the contest is over, two indices are bound to it: the number of solved problems Pi and the size of the penalty Fi. The penalty is for unsuccessful attempts and time spent on the task.

Timofey decided to sort the results table in the following way: if you compare two participants, the one who solved more problems will be higher. If the number of solved problems is equal, the participant with the smaller penalty goes first. If the fines are the same, the first will be the one with the first login in alphabetical order.

Timothy ordered sweatshirts for the winners and went to the store the day before to pick them up. In his absence, he instructed you to implement a quick sort algorithm for the results table. Since Timothy likes sports programming and doesn't like to waste RAM, your implementation of sorting can't consume O(n) extra memory for intermediate data (this modification of quick sorting is called "in-place").

### Input format.

The first line specifies the number of participants n, 1 ≤ n ≤ 100,000.

Each of the following n lines contains information about one of the participants.

The i-th participant is described by three parameters:

a unique login (a string of small Latin letters, length no more than 20)
number of problems solved Pi
penalty Fi

Fi and Pi are integers in the range from 0 to 10^9

### Output format

For a sorted list of contestants print in order their logins, one per line.
