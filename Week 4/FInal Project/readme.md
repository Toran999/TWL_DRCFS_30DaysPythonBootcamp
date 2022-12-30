# Welcome to week 4 of the bootcamp.
I have created a program in c that simulates the famous Buffon Noodle method or 
Buffon needle method to approximate the value of PI, one of the most important Mathematical constant.
In this experiment, Pi shows up in seemingly unusal place.

Consider an experiment in which equally spaced parallel lines are drawn on grounds.
Now consider a needle or noodle or match or whatever object having very small width and length equal to the 
distance between the parallel lines drawn on  the ground. 

Now If you dropped the needle or match then what is the probability that the needle will cross the 
lines that you drew.

__________________________________________
___|_______________________________________
_________/_________________________________
______________\____________________________

The matches you dropped will have random orientations and they can land anywhere on the grid.
So how do we calculate its probability??? Preety intense right?
Don't panic because luckily some old folks from 18th century came up with a whole field of 
mathematics known as geometric probability and 
__________________________________________________________________________
|                                                                         |                                                   
| IT TURNS OUT THAT THE PROBABILITY OF NEEDLE LANDING ON LINE IS 2/PI !!! |
|_________________________________________________________________________|

ISN'T IT INSANE??? HOW PI SHOWS UP IN UNIMAGINABLE PLACES???

There is another remarkable theorem in mathematics called CENTRAL LIMIT THEOREM 
that says if we repeat an probabilistic experiment infinite number (many) times we 
will get the total probability equal to the probability for each event to occur.

                                OR
Simply put, if we toss a coin for n number of time and get m number of head or tail then 
m/n = 1/2 as n approaach to infinity. i.e. we will get almost equal no of head and tail on the long run.

or say, We rolled a dice for 600,000 times then we will get each number(1,2,3,4,5,6) for about 100,000
times.

that is, if we dropped our needle or matchsticks for many times, the ratio of needles that crossed  or touched the lines to the total number of needles dropped will be equal to 2/pi.

By using this to concept together we get the value of pi will be equal to 

                    PI = 2 / probability

But we have one problem left..................

Dropping needles or matches for a million times and observing how many needles crossed the lines is too tedious to do.
Last time it was 1901 when a guy named Mario Lazzarini performed it for 3408 times.

We aren't going to do that because we have a sophisticated machine and a powerful language to order it that together can
simulate this whole process of dropping needles on a grid line in only 15 lines of instructions!!!!!!!

So I just saved your 8 hours of manual tedious work under some few lines of codes.

So let's discuss how will we simulate this whole experiment in python.

1. So first of all,  dropping a needle from a height is completely random process as we don't know where will the needle land.
   So for working with this probabilistic event we already have a perfect library in python named random. So we will import random in our program.
2. We define a variable named crossed whcih counts how many needles crossed the lines.
3. User provides input on how many needles should be tossed or how many times should a needle be tossed and store it in          
    variable named total.
4. As python stores user input variables as string we change it into integer with a pre built function int().
5. we create a for loop for total number of lines that tosses the needle for total number of times.
6. inside for loop we define a variable named head which is the position of the needle head when dropped on the grid from our     
    arbitary zero till one. zero and one are position where our two lines drawn on the ground are. so we take only two gridlines from the ground for simplification of the condition and allow our needle head to be between or on these lines.
7. 