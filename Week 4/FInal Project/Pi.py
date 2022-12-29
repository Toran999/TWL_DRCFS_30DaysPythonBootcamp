# This program uses buffon needle problem to estimate the value of Pi
# Pi is an irrational number and its value is difficult to apprximate.
# Buffon noodle method uses the probability to get the rough estimate value of Pi over large iterations.
# When a needle of unit height is dropped between parallelly drawn lines of same length
# Then the probablility that the needle will drop crossing any of those lines is 2/PI
# If a needle is dropped for very large n times and for m times of those n drops if the needle crossed the lines then
# the probability is given by m/n
# to simulate a drop we will use random library 

import random

init_position = random.uniform(0,1)
