# SNI-project
This repository contains the code used for the 2019-2020 SNI project at univ rennes 1.
# Question 1:
Add the K parameter.

- **Does "serve" mean termination or arrival? For now I considered termination**

# Question 2:
Just remove the *expo()* calls to have a determinisic value of exactly mean
service time.

- in the pdf, they use different seeds in the 2 cases to perform the comparison,
  should we do that? why?
  
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

Same things

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
Do the same things with MM1 and MD1, and look at the two other values

```
for i in $(seq 0 0.2 10)
do
	python MMinf.py 1.0 $i 10000 3117 100000 
	python MM1.py 1.0 $i 10000 3117 100000 
done
```
**We can see MMinf is stable, MM1 is not at all**
