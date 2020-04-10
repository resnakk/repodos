
import matplotlib.pyplot as plt
import statistics as es
from peakdetect import peakdetect
#====================== UNITS ======================
m = 1
cm = 0.01
mm = 0.001
kg = 1
g = 0.001
Pa = 1
GPa = 10**9 
#======================== VALUES ===========================
h = [50*cm,45*cm,40*cm,50*cm,50*cm] 			
motor = 232*g 							#always present
added_mass = 142*g 			
top_plate_top_bolts = 146.8*g 			#always present
Top_bolts_nuts = 21.5*g 				#always present
column = 324.6*g 						#always present
E = 200*GPa 				
density = 7850*(kg/m**3)					
a = 25*mm							
b = 3*mm
cable = []
hammer = []
rome =["i", "ii", "iii", "iv", "v"]
#============================= FUNCTIONS =====================
def importe(i):
	file1 = open("download/cable_{}_mod.txt".format(i),"r")
	file2 = open("download/hammer_{}_mod.txt".format(i),"r")
	lines1 = file1.readlines()
	lines2 = file2.readlines()
	liste = [[],[]]
	for i in lines1:
		value = i.split()
		liste[0].append(float(value[0]))
		liste[1].append(float(value[1]))
	cable.append(liste)
	
	liste = [[],[]]
	for i in lines2:
		value = i.split()
		liste[0].append(float(value[0]))
		liste[1].append(float(value[1]))
	hammer.append(liste)

for i in rome:
	importe(i)

def data(liste):
	peaks = peakdetect(liste[1])
	positive = peaks[0]
	negative = peaks[1]
	pos_positions = []
	neg_positions = []
	for i in positive:
		pos_positions.append(i[0])
	for i in negative:
		neg_positions.append(i[0])
	t_pos_c = []
	t_neg_c = []
	for i in pos_positions:
		t_pos_c.append(liste[0][i])
	for i in neg_positions:
		t_neg_c.append(liste[0][i])
	difs = []
	for i in range(1,len(t_pos_c)):
		dif = t_pos_c[i] - t_pos_c[i - 1]
		difs.append(dif)
	for i in range(1,len(t_neg_c)):
		dif = t_neg_c[i] - t_neg_c[i - 1]
		difs.append(dif)
	average = es.mean(difs)
	stdev = es.stdev(difs)
	return [average, stdev] 		
#========================= PLOTS ======================

for j in range(5):
	plt.plot(cable[j][0],cable[j][1], label = "cable_{}".format(rome[j]))

plt.ylabel("Acceleration")
plt.xlabel("time")
plt.title("Cable")
plt.legend()
plt.savefig("cable")
plt.close()
for j in range(5):	
	plt.plot(hammer[j][0],hammer[j][1], label = "hammer_{}".format(rome[j]))
plt.ylabel("Acceleration")
plt.xlabel("time")
plt.title("Hammer")
plt.legend()
plt.savefig("hammer")

#======================= DATA =====================
cable_period = []
hammer_period = []
for i in range(len(cable) - 1):
	a = data(cable[i])
	cable_period.append(a)

for i in range(len(hammer) - 1):
	a = data(hammer[i])
	hammer_period.append(a)
print cable_period
print hammer_period



#======================= CASE I =====================

#======================= CASE II ====================

#======================= CASE III ===================

#======================= CASE IV ====================

#======================= CASE V =====================
