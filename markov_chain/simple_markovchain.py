import numpy
from numpy import matrix


def state_probability(state, time_step, transition_matrix):
	return state*transition_matrix**time_step

time_step=input("Enter the number of time steps: ")

state_= input("Enter the file with the current state:(include quotes '') ")
transition_matrix_= input("Enter the file with the transition matrix(include quotes ''): ")

testmatrix= open(transition_matrix_)
teststate= open(state_)
transition_matrix= matrix(testmatrix.read())
state= matrix(teststate.read())

prob=state_probability(state, time_step, transition_matrix)
print prob
