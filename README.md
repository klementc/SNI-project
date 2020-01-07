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
