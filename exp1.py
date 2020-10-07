import random

#Taking values from user to get molarity of acetone,HCL and Iodine.
print("All solutions are made in 100 ml water")
initial_weight_acetone=float(input("Enter weight of Acetone(in grams): "))
initial_weight_hcl=float(input("Enter weight of HCl(in grams): "))
initial_weight_iodine=float(input("Enter weight of I\N{SUBSCRIPT TWO}(in grams): "))

#calculation of molarity of each component
m1_acetone=(initial_weight_acetone/58.08)/0.1
m1_hcl=(initial_weight_hcl/36.46)/0.1
m1_iodine=(initial_weight_iodine/253.8089)/0.1

#volume of each component in each trial

#trial 1

print("\nEnter volumes of each solution used in trial 1(in ml): \n")
initial_volume_acetone1=float(input("Enter volume of Acetone(in ml): "))
initial_volume_hcl1=float(input("Enter volume of HCl(in ml): "))
initial_volume_iodine1=float(input("Enter volume of I\N{SUBSCRIPT TWO}(in ml): "))
initial_volume_water1=float(input("Enter volume of H\N{SUBSCRIPT TWO}O (in ml): "))
total_trial1=initial_volume_iodine1+initial_volume_acetone1+initial_volume_hcl1+initial_volume_water1

#calculation of molarity for trial 1
m1_acetone_trial1=(m1_acetone*0.1)/total_trial1
m1_hcl_trial1=(m1_hcl*0.1)/total_trial1
m1_iodine_trial1=(m1_iodine*0.1)/total_trial1

#trial 2

print("\nEnter volumes of each solution used in trial 2(in ml): \n")
initial_volume_acetone2=float(input("Enter volume of Acetone(in ml): "))
initial_volume_hcl2=float(input("Enter volume of HCl(in ml): "))
initial_volume_iodine2=float(input("Enter volume of I\N{SUBSCRIPT TWO}(in ml): "))
initial_volume_water2=float(input("Enter volume of H\N{SUBSCRIPT TWO}O (in ml): "))
total_trial2=initial_volume_iodine2+initial_volume_acetone2+initial_volume_hcl2+initial_volume_water2

#calculation of molarity for trial 1
m1_acetone_trial2=(m1_acetone*0.1)/total_trial2
m1_hcl_trial2=(m1_hcl*0.1)/total_trial2
m1_iodine_trial2=(m1_iodine*0.1)/total_trial2

#trial 3

print("\nEnter volumes of each solution used in trial 3(in ml): \n")
initial_volume_acetone3=float(input("Enter volume of Acetone(in ml): "))
initial_volume_hcl3=float(input("Enter volume of HCl(in ml): "))
initial_volume_iodine3=float(input("Enter volume of I\N{SUBSCRIPT TWO}(in ml): "))
initial_volume_water3=float(input("Enter volume of H\N{SUBSCRIPT TWO}O (in ml): "))
total_trial3=initial_volume_iodine3+initial_volume_acetone3+initial_volume_hcl3+initial_volume_water3

#calculation of molarity for trial 1
m1_acetone_trial3=(m1_acetone*0.1)/total_trial3
m1_hcl_trial3=(m1_hcl*0.1)/total_trial3
m1_iodine_trial3=(m1_iodine*0.1)/total_trial3

#trial 4

print("\nEnter volumes of each solution used in trial 4(in ml): \n")
initial_volume_acetone4=float(input("Enter volume of Acetone(in ml): "))
initial_volume_hcl4=float(input("Enter volume of HCl(in ml): "))
initial_volume_iodine4=float(input("Enter volume of I\N{SUBSCRIPT TWO}(in ml): "))
initial_volume_water4=float(input("Enter volume of H\N{SUBSCRIPT TWO}O (in ml): "))
total_trial4=initial_volume_iodine4+initial_volume_acetone4+initial_volume_hcl4+initial_volume_water4

#calculation of molarity for trial 1
m1_acetone_trial4=(m1_acetone*0.1)/total_trial4
m1_hcl_trial4=(m1_hcl*0.1)/total_trial4
m1_iodine_trial4=(m1_iodine*0.1)/total_trial4


print("Values Entered By you are as follows: ")
print("trial\tAcetone\tHCl\tI\N{SUBSCRIPT TWO}\tH\N{SUBSCRIPT TWO}O")
print("1.\t",initial_volume_acetone1,"\t",initial_volume_hcl1,"\t",initial_volume_iodine1,"\t",initial_volume_water1)
print("2.\t",initial_volume_acetone2,"\t",initial_volume_hcl2,"\t",initial_volume_iodine2,"\t",initial_volume_water2)
print("3.\t",initial_volume_acetone3,"\t",initial_volume_hcl3,"\t",initial_volume_iodine3,"\t",initial_volume_water3)
print("4.\t",initial_volume_acetone4,"\t",initial_volume_hcl4,"\t",initial_volume_iodine4,"\t",initial_volume_water4)


#producing absorbance values for trial 1, a=ecl and c=[i]0-k't

#calculating k' 
k=random.randint(-4,5)
k=28+k
k=k/1000000
k_dash_trial1=k*m1_acetone_trial1*m1_hcl_trial1
k_dash_trial2=k*m1_acetone_trial2*m1_hcl_trial2
k_dash_trial3=k*m1_acetone_trial3*m1_hcl_trial3
k_dash_trial4=k*m1_acetone_trial4*m1_hcl_trial4
time=[]
t=0
absorbance=[]
print("Time(sec)\tabsorbance")
while(t<=1800):
	a=0.3636*(m1_iodine_trial1-k_dash_trial1*t)
	print(t,"\t",a)
	time.append(t)
	absorbance.append(a) 	
	t=t+30
	

import matplotlib.pyplot as plt
plt.plot(time,absorbance)
plt.ylabel('Absorbance')
plt.xlabel('time')
plt.show()
print(k_dash_trial1*m1_acetone_trial1*m1_hcl_trial1)
import numpy as np 
time=np.array(time)
absorbance=np.array(absorbance)
slope, intercept = np.polyfit(absorbance,time, 1)
print(slope)
