# SNI-project
This repository contains the code used for the 2019-2020 SNI project at univ rennes 1.
The *_base code repositories contain the code that has been given to us (with the addition of a Makefile for the C code).
Our modifications of this code can be found in the project_code folder.

# Question 1:
Add the K parameter.

To answer this question, we added a new variable called K. Then we count the number of clients served.
If the number of clients served goes over this value K, we go out of the simulation loop and give results back to the user.

# Question 2:
Just remove the *expo()* calls to have a determinisic value of exactly mean
service time.

Here, we just replaced calls to the exponential distribution function when generating a new mst value by a constant.
  
output example:
```
	$ python MD1.py 3 7 10000 3117 100000 

	--- Data: mtba = 3.0, mst = 7.0, T = 10000.0, seed = 3117

	1428 clients were served out of 100000 Maximum

	--- meanNbOfUnits = 986.770609
  
  
	$ python MM1.py 3 7 10000 3117 100000
  
	--- Data: mtba = 3.0, mst = 7.0, T = 10000.0, seed = 3117

	1435 clients were served out of 100000 Maximum

	--- meanNbOfUnits = 982.391006
```

```
for i in $(seq 0 0.1 1.1)
do
	python MM1.py 1.0 $i 10000 3117 100000 
	python MD1.py 1.0 $i 10000 3117 100000 
done
```

# Question 3:

Same thing as question 2 but in an other model.

```
$ python MDinf.py 3 7 10000 3117 100000

 --- Data: mtba = 3.0, mst = 7.0, T = 10000.0, seed = 3117

 --- meanNbOfUnits = 2.371455

$ python MMinf.py 3 7 10000 3117 100000

 --- Data: mtba = 3.0, mst = 7.0, T = 10000.0, seed = 3117

 --- meanNbOfUnits = 2.307472

```

```
for i in $(seq 0 0.2 10)
do
	python MMinf.py 1.0 $i 10000 3117 100000 
	python MDinf.py 1.0 $i 10000 3117 100000 
done
```
**The results show little's law**

# Question 4/5: 

We added a queue to store service times, and use it to measure jitter and mean delays. 
This queue is used to store the time at which customers arrive and are removed at departure.

The jitter is calculated by making the difference of two successive delays.

```
for i in $(seq 0 0.2 10)
do
	python MMinf.py 1.0 $i 10000 3117 100000 
	python MM1.py 1.0 $i 10000 3117 100000 
done
```
**We can see MMinf is stable, MM1 is not at all**
