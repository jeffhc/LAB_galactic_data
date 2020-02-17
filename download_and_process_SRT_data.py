import statistics, requests
import matplotlib.pyplot as plt

# Get Galactic longitudes
pos = list(map(lambda x: format((x*10), '.2f'), range(10)))
neg = list(map(lambda x: format((x*-10), '.2f'), range(10)))[1:]
l = pos + neg

# # Download data from SRT website
url = 'https://www.astro.uni-bonn.de/hisurvey/AllSky_profiles/download.php?ral=%s&decb=0.00&csys=0&beam=0.200'
for val in l:
	with open(val + '.txt', 'w') as f:
		request = requests.get(url % val)
		f.write(request.text)

# Parse data
final_LAB_data = {}
for val in l:
	with open(val + '.txt', 'r') as f:
		lines = f.readlines()
		LAB_index = lines.index([i for i in lines if '%%LAB' in i][0])
		LAB_data = lines[LAB_index:]
		parsed_LAB_data = [[float(i.strip()) for i in line.split(' ') if i] for line in LAB_data if '%%LAB' not in line]
		final_LAB_data[val] = parsed_LAB_data


# Find maximum velocity at each longitude

clearance_threshhold = 100
deviance_from_variance = 2.5
final_max_vels = []

for val in l:
	# Percent standard deviations starting from largest velocity index minus clearance threshhold in descending order.
	variances = []
	fluxes = [i[1] for i in final_LAB_data[val]]
	for n in range(len(fluxes)-clearance_threshhold, 0, -1):
		variances.append([
			final_LAB_data[val][n][0], 						# Velocity
			final_LAB_data[val][n][1], 						# Flux
			statistics.variance(fluxes[n:len(fluxes)]) 		# Cumulative variance at a given velocity
		])

	# Max vel is found by finding first velocity from the right whose difference from the flux
	# is greater than the deviation from variance.
	max_vel = None
	for n in range(len(variances)):
		if not max_vel:
			vel = variances[n][0]
			flux = variances[n][1]
			variance = variances[n][2]
			if abs(flux - variance) > deviance_from_variance:
				max_vel = vel

	final_max_vels.append((val, max_vel))

	plt.figure(val)
	plt.axvline(x=max_vel, linewidth=1, color='r')
	# plt.plot([i[0] for i in variances], [i[2] for i in variances], color='green')
	plt.plot([i[0] for i in final_LAB_data[val]], [i[1] for i in final_LAB_data[val]], color='b')
	plt.title('SRT - Galactic longitude: %s' % val)
	plt.xlabel('VLSR (km/s)')
	plt.ylabel('Brightness Temperature (K)')
	plt.savefig(val+'_max.png')
	print('Found max velocity for %s, saved spectrum!' % val)

# plt.show()

print(final_max_vels)
