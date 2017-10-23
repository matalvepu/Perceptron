#This is an implementation of perceptron algorithm
#Author: Md Kamrul Hasan (mhasan8@cs.rochester.edu)
import numpy as np
import matplotlib.pyplot as plt
import random

class Perceptron:

	def __init__(self, training_data, dev_data, test_data):
		self.training_data= training_data
		self.dev_data = dev_data
		self.test_data = test_data
		self.W=np.zeros(124)

	#this function calculate accuray in data using the 
	# classifer based on alpha (leraning rate) and W (weight vector)
	@staticmethod
	def get_accuracy_of_classifier(alpha,W,data):
		X=np.array(data[0])
		Y=np.array(data[1])
		count=float(0)
		#iterate through all data instance
		for n in range(len(X)):
			X_n=X[n]
			X_n=np.mat(X_n)
			Y_n=int(Y[n])
			W=np.mat(W)
			W_tr=W.T
			val= X_n * W_tr
			val=float(val[0,0])
			if((val * Y_n) <= 0):	#if missclassified increase the count of missclassification
			    count=count+int(1)

		accuracy=float((len(X)-count)/float(len(X)))
		return accuracy

	#this is the main algorithm of perceptron
	#It find the best weight vector by testing on dev set based on given alpha (learning rate)
	def run_algorithm(self,alpha):
		accuracy_list=[]
		max_accuracy=int(-1)
		is_converged=int(0)
		num_step=int(0)
		X=np.array(self.training_data[0])
		Y=np.array(self.training_data[1])
		#iterate all the data many times until converged
		while(is_converged == 0):
			for n in range(len(X)):
				X_n=X[n]
				X_n=np.mat(X_n)
				Y_n=int(Y[n])
				W=np.mat(self.W)
				W_tr=W.T
				val= X_n * W_tr
				val=float(val[0,0])
				if((val * Y_n) <= 0):
					self.W = self.W + alpha * Y[n] * X[n]

			#get the accuracy on dev set based on new W vector
			acc=self.get_accuracy_of_classifier(alpha,self.W,self.dev_data) 
			accuracy_list.append(acc)

			#tracking the best W for which accuracy is maximum
			if(acc > max_accuracy):
				max_accuracy=acc
				num_step=int(0)
				W_max=self.W
			else:
				num_step = num_step + int(1)
			#if consecutive 30 iteration does not find any accuracy greater then
			#the last best one then I assumed that it converged in optimum
			if(num_step >= int(30) or (max_accuracy == float(1))):
				is_converged=int(1)

		return [W_max,accuracy_list,max_accuracy]

#this function convert each data instance to vector
def convert_line_to_vector(line):
	x_vect=[0]*124
	x_vect[0]=int(1)
	str_arr=line.split()
	target_val=int(str_arr[0])
	str_arr.pop(0)
	for feature in str_arr:
		feature_arr=feature.split(":")
		x_vect[int(feature_arr[0])]=int(feature_arr[1])

	return [x_vect,target_val]

# This function parse all the data and creates list of vector
def parse_data(file_name):
	X=[]
	target=[]
	with open(file_name, "r") as f_in:
	    for line in f_in:
	    	if line:
		    	arr=convert_line_to_vector(line)
		    	X.append(arr[0])
		    	target.append(arr[1])

	
	return [X,target]
	
#########main############
def main():
	training_data=parse_data("a7a.train")
	dev_data=parse_data("a7a.dev")
	test_data=parse_data("a7a.test")

	alpha_list=np.arange(0.001,0.076, 0.015)
	dev_max_accuracy_list=[]
	iteration_number_list=[]
	best_alpha=int(-1)
	best_dev_accuracy=int(-1)
	best_dev_accuracy_list=[]
	best_W=[]

	#Iterate for all alpha (learning rate) range between 0.001 to 2 with 0.015 increment
	#Find the best alpha (learning rate) and W (weight vector) which gives maximum  
	#accuracy in dev set
	for alpha in alpha_list:
		pr=Perceptron(training_data, dev_data, test_data)
		[W_max,accuracy_list,max_accuracy]=pr.run_algorithm(alpha)
		dev_max_accuracy_list.append(max_accuracy)
		iteration_number=accuracy_list.index(max_accuracy)+int(1)
		iteration_number_list.append(iteration_number)
		if(max_accuracy>best_dev_accuracy):
			best_dev_accuracy=max_accuracy
			best_dev_accuracy_list=accuracy_list
			best_alpha=alpha
			best_W=W_max

	#plot all the results
	plt.plot(alpha_list,dev_max_accuracy_list,linestyle='--', marker='o', color='b')
	plt.axis([0, 2.1, 0.78, 0.87])
	plt.ylabel('Maximum Accuracy in Dev Set')
	plt.xlabel('Learning Parameter (alpha)')
	plt.show()

	plt.plot(alpha_list,iteration_number_list,linestyle='--', marker='o', color='r')
	plt.axis([0, 2.1, 0, 130])
	plt.ylabel('Number of Iteration Needed to Converge')
	plt.xlabel('Learning Parameter (alpha)')
	plt.show()

	plt.plot(best_dev_accuracy_list,linestyle='--', marker='o', color='b')
	plt.ylabel('Accuray in Dev Set')
	x_label="Iteration Number (alpha="+str(best_alpha)+")"
	plt.xlabel(x_label)
	plt.show()

	#find the accuracy on test set based on best alpha (learning rate) and W (weight vector)
	print("Test Accuracy :",Perceptron.get_accuracy_of_classifier(alpha,best_W,test_data))
        

if __name__ == '__main__':
    main()







