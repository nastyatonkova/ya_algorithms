# **Yandex.Practicum. Sprint 11**

# Introduction to algorithms
https://contest.yandex.ru/contest/23389/problems/

## A. Function Values:
Write code for a function that calculates y = ax^2 + bx + c. Write a program that will, by the coefficients a, b, c and the number x, output the value of the function at the point x.

Input the numbers a, x, b, c through a space.
**Output one number, the value of the function at point x.**

## B. Even and odd numbers:
The player presses a button and three random numbers appear on the screen. If all three numbers turn out to be the same even number, the player wins.
Write a program that determines from the three numbers whether the player wins or not.

The first line contains three random integers a, b and c. The numbers do not exceed 10^9 modulo.

**Output "WIN" if the player has won, and "FAIL" otherwise.**

## C. Neighbors:
A matrix is given. You need to write a function that, for an element, returns all of its neighbors. An element that is one cell to the left, right, up, or down from the current one is considered a neighbor. Diagonal elements are not considered neighbors.

The first line contains n - the number of matrix rows. The second is the number of columns m. The numbers m and n do not exceed 1000. The next n lines contain a matrix. The matrix elements are integers, modulo not exceeding 1000. The last two lines contain the coordinates of the element (indexing starts with zero) whose neighbors you want to find.

**Type the numbers you want, in ascending order, separated by a space.**

## D. Chaotic Weather:
Determine from the daily temperature readings the chaoticness of the weather over a particular period.
Note that if the number of readings is n=1, then the only day is chaotic. 

The first line gives the number n -- the length of the measurement period in days, 1 ≤ n≤ 10^5. The second line gives n integers -- temperature values on each of n days. The temperature values do not exceed 273 modulo.

**Find a single number -- a randomness for a given period.**

## E. Longest word:
Take a random sentence from the text and look for the longest word in it. Its length will be the conditional complexity of the article. 
The first line contains the text length L (L ≤ 10^5).
The only line contains a text consisting of lowercase Latin letters and spaces. The word is a sequence of letters not separated by spaces. Spaces can be at the beginning and at the end of the line.

**On the first line print the longest word. On the second line print its length. If there are several matching words, print the one that comes first.**

## F. Palindrome
Determine if the phrase is a palindrome. Only letters and numbers are taken into account; capital and lowercase letters are treated the same. 
The solution must work for O(N), where N is the input string length. 
Additional memory greater than O(1) cannot be used.

The only line contains a phrase or word. Letters can be Latin letters only.
Only letters and digits are counted, capital and small letters are counted the same.

**Print True if the phrase is a palindrome and False if it is not.**

## G. Work At Home:
Write an optimal function for converting an integer from decimal to binary.

The input is an integer in the range 0 to 10000.
**Output the binary representation of that number.**

## H. Binary system:
Two numbers are written in binary notation. Print their sum, also in binary. The built-in binary addition feature of the programming language cannot be used.

The solution must work for O(N), where N is the number of bits of the maximum number in the input.

Two numbers in binary notation, each on a separate line. The length of each number does not exceed 10,000 characters.  

**Output the binary representation of this number.**

## I. The power of four:
An integer number between 1 and 10000 is input.
**Output "True" if the number is a power of four, "False" otherwise.**

## J. Factorization:
A single line contains a number n (2 ≤ n ≤ 10^9), which must be factorized.
**Output in non-decreasing order the prime factors into which n is expanded..**

## K. List form:
The input is the number of digits of the number X, the list form of the non-negative number X, and the number K. 
The numbers K and X do not exceed 10000.
You need to return the list form of the number X + K.

On the first line is the length of the list form of number X. 
On the next line is the list form itself with numbers written with a space. 
The last line contains the number K.

**Output the list form of the number X + K.**


## L. There is an extra letter: 
There are 2 lines s and t consisting only of lowercase letters. 
The string t is obtained by mixing the letters of the string s and adding 1 letter to a random position. 
We need to find the added letter.

Input lines s and t, separated by a line break.

**Find the extra letter.**

# Final tasks
https://contest.yandex.ru/contest/23390/problems/

## A. Nearest zero.

Count the distances to the empty/empty lots. You have a street map to do this. The houses in the city were numbered in the order in which they were built, so their numbers are not ordered on the map in any way. Empty lots are marked with zeros. 


### Input format
The first line gives the length of the street -- n (1 ≤ n ≤ 10^6). The next line contains n non-negative integers - the numbers of houses and signs of empty areas on the map (zeros). It is guaranteed that there is at least one zero in the sequence. The house numbers (positive numbers) are unique and do not exceed 10^9. 

### Output format. 
For each plot print the distance to the nearest zero. Output the numbers on one line, separated by spaces.

## B. Manual dexterity.

Gosha and Timothy have found an unusual speed typing simulator and want to master it. The simulator is a field of 4×4 keys in which a configuration of numbers and dots appears on each round. Either a dot or a number from 1 to 9 is written on the key. At time t, the player must simultaneously press all the keys on which the digit t is written. Gosha and Timofey can press k keys each at a moment of time. If at time t all necessary keys have been pressed, the players get 1 point.

Find the number of points that Gosha and Timofey can earn, if they press the keys together.

### Input format

The first line contains an integer k (1 ≤ k ≤ 5).

The next four lines give the type of simulator -- 4 characters in each line. Each character is either a dot or a digit from 1 to 9. Characters on the same line are consecutive and not separated by spaces.

### Output format
Print a single number - the maximum number of points Gosha and Timofey can get.
