# Perceptron


Name: Md Kamrul Hasan
Email: mhasan8@cs.rochester.edu
Date: 1/27/2017

=============================================================================================== 

Description: 

Implement perceptron for the adult income dataset using Python. Experiment with performance as 
a function of learning rate.

I did it as a part of homework problem in the Machine Learning class taught by Prof Daniel Gildea
(https://www.cs.rochester.edu/~gildea/) in Spring 2017.

Four Files:

	1. accuracy(dev)_vs_iteration.png : this is graph for accuracy in dev set for each 
      iteration (given: learning rate = 0.751)
	
	2. max_accuracy(dev)_vs_learning_rate.png: This graph is for maximum accuracy in dev set 
      for each alpha (learning rate)
	
	3. num_of_iteration_vs_learning_rate.png : This graph is for how many iterations is needed
      to converge for each alpha (lerning rate)
      
	4. perceptron.py : it contains the implementaion of perceptron algorithm


=============================================================================================== 

************ Algorithm ************

input: learning rate, training set, dev set, test set

while(is_not_converged):
	for each training data X_n:
		if (misclassified):
		   update weight vector
    
    acc=get_accuray(dev_set)
    is_not_converged=funcition(acc)


#I always tracked the maximum accuracy found in dev set. If I dont find any accuray better than 
maximum in consecutive 30 itration then I assumed it converged and break the loop and return 
the best weight vector. 


=============================================================================================== 

************ Instructions to run ************

python perceptron.py



=============================================================================================== 
************ Results ************

Accuracy in Test set: 0.8321711381633377 (83.22 %)


I run an exeriment as function of learning rate (alpha).  I have iterated for all alpha 
(learning rate) range between 0.001 to 2 with 0.015 increment and find the best 
alpha (learning rate) and W (weight vector) which gives maximum accuracy in dev set

After tuning the best learning rate(alpha) = 0.751 (see graph: ax_accuracy(dev)_vs_learning_rate.png) 
and it tooks around 75 iteration (see graph: num_of_iteration_vs_learning_rate.png) 

Weight vector (for best accuracy) : 
[ -3.00400000e+00  -4.50600000e+00  -3.00400000e+00   2.25300000e+00
   3.00400000e+00  -7.51000000e-01   7.51000000e-01  -2.25300000e+00
   3.75500000e+00   5.25700000e+00   3.00400000e+00  -2.22044605e-16
  -5.25700000e+00   0.00000000e+00  -4.50600000e+00   2.25300000e+00
   7.51000000e-01  -1.50200000e+00  -2.22044605e-16  -1.50200000e+00
   7.51000000e-01   3.00400000e+00  -7.51000000e-01   1.50200000e+00
  -2.25300000e+00   3.00400000e+00  -2.22044605e-16  -7.51000000e-01
   6.00800000e+00  -2.22044605e-16   1.50200000e+00   7.51000000e-01
   3.75500000e+00  -7.51000000e-01  -1.72730000e+01  -7.51000000e+00
  -7.51000000e-01   7.51000000e-01   7.51000000e-01   3.75500000e+00
   5.25700000e+00  -2.25300000e+00  -4.50600000e+00  -4.50600000e+00
  -6.66133815e-16  -4.50600000e+00   7.51000000e+00   2.25300000e+00
   7.51000000e-01  -1.50200000e+00   1.50200000e+00   6.00800000e+00
   7.51000000e-01  -6.66133815e-16  -6.66133815e-16  -2.22044605e-16
  -2.25300000e+00  -2.25300000e+00  -4.50600000e+00   4.50600000e+00
   0.00000000e+00   3.00400000e+00  -7.51000000e-01  -7.51000000e-01
  -7.51000000e-01  -3.00400000e+00  -7.51000000e-01   2.22044605e-16
   2.25300000e+00  -1.50200000e+00  -2.25300000e+00  -1.50200000e+00
  -3.00400000e+00  -2.22044605e-16  -6.00800000e+00   3.00400000e+00
  -4.50600000e+00   1.50200000e+00  -3.75500000e+00  -6.66133815e-16
  -7.51000000e-01   6.66133815e-16   1.50200000e+00   4.50600000e+00
   7.51000000e+00   2.25300000e+00  -5.25700000e+00   6.75900000e+00
  -1.50200000e+00   0.00000000e+00  -6.00800000e+00   2.25300000e+00
  -7.51000000e-01  -1.50200000e+00  -3.00400000e+00   3.75500000e+00
  -1.50200000e+00   0.00000000e+00   3.00400000e+00   3.00400000e+00
   2.25300000e+00   1.50200000e+00  -6.75900000e+00   7.51000000e-01
  -2.25300000e+00   6.00800000e+00   7.51000000e-01  -3.00400000e+00
  -6.75900000e+00   9.76300000e+00  -1.50200000e+00   1.50200000e+00
  -8.26100000e+00  -3.75500000e+00   3.00400000e+00   6.00800000e+00
   4.50600000e+00  -6.75900000e+00   6.00800000e+00   2.25300000e+00
  -2.25300000e+00  -8.26100000e+00  -1.50200000e+00   0.00000000e+00]



=============================================================================================== 

************interpretation ************

accuracy(dev)_iteration.png graph shows the acuuray in dev set over all iteartion for learning 
rate = 0.751. This graph suggest that this data is not linearly classfiable. Because there is 
zig zag  in the graph. If it is linearly classifiable then the acuuray would increas smoothly 
and converge in some point. That is why I always tracked the maximum accuracy found in dev set. 
If I dont find any accuray better than maximum in consecutive 30 itration then I assumed it 
converged and early stop there. Moreover, max_accuracy(dev)_vs_learning_rate.png graph also 
suggest changing over the elarning rate does not change the accuray significantly over the 
range [0.001,2].

************ References ************
Book: Christopher M. Bishop, Pattern Recognition and Machine Learning
Web link: http://www.eecs.yorku.ca/course_archive/2012-13/F/4404-5327/lectures/05%20Linear%20Classifiers.pdf 
