"""
Your city's weather service has decided to investigate the weather in a new way.
    By the air temperature on a particular day we will understand the maximum temperature on that day.
    By chaotic weather for n days the service understands the number of days in which the temperature is strictly higher 
    than on the day before (if such a day exists) and on the day after the current day (if such a day exists). 
    For example, if during 5 days the maximum air temperature was [1, 2, 5, 4, 8] degrees, 
    then the randomness over this period equals 2: on the 3rd and 5th days the conditions described above were met.
Determine from the daily temperature readings the randomness of the weather during this period.

Note that if the number of readings is n=1, then the only day will be chaotic.
 
"""

from typing import List

def get_weather_randomness(temp: List[int]) -> int:
	num_days = len(temp)
	count = 0
	if  num_days == 1:
		return 1
	for i in range(num_days):
		if i == 0 and temp[i] > temp[i+1]:
			count+=1
		if i == num_days-1 and temp[i] > temp[i-1]:
			count+=1
		if i > 0 and i < num_days-1:
			if temp[i] > temp[i+1] and temp[i] > temp[i-1]:
				count+=1
	return count 

def read_input() -> List[int]:
    n = int(input())
    temp = list(map(int, input().strip().split()))
    return temp

temp = read_input()
print(get_weather_randomness(temp))
