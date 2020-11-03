import json 
import numpy as np 

def gen_Fp_Fv(): 
	pn_p = np.array([-1, 1], int).take(np.random.randint(0, 2)) 
	pn_v = np.array([-1, 1], int).take(np.random.randint(0, 2)) 
	value_p = np.random.rand(1) 
	value_v = np.random.rand(1) 
	Fp = round(float(pn_p * value_p), 6) 
	Fv = round(float(pn_v * value_v), 6) 
	list_data = [Fp, Fv] 
	return list_data 

for i in range(8):
	a = gen_Fp_Fv() 
	print(a)