from __future__ import print_function
from dataclasses import field
import time
import argparse
import csv

from heat import init_fields, write_field, iterate
from heat_cyt import init_fields_cyt, write_field_cyt, iterate_cyt


def main(input_file='bottle.dat', a=0.5, dx=0.1, dy=0.1, 
         timesteps=200, image_interval=4000):

	input_files = ['bottle.dat', 'bottle_medium.dat', 'bottle_large.dat']
	timestepsS = [100, 200, 500, 1000, 2000, 3000]
	versions = ['Python','Cython']

	# field names 
	headResults = ['version', 'input_file', 'timesteps', 'time (s)'] 
	newList = []
	for version in versions:
		for input_file in input_files:
			for timesteps in timestepsS:
				if version == 'Python':      	
					#print("Using pure Python") 	
					# Initialise the temperature field
					field, field0 = init_fields(input_file)

					#print("Heat equation solver")
					#print("Diffusion constant: {}".format(a))
					#print("Input file: {}".format(input_file))
					#print("Parameters")
					#print("----------")
					#print("  nx={} ny={} dx={} dy={}".format(field.shape[0], field.shape[1],
					#							dx, dy))
					#print("  time steps={}  image interval={}".format(timesteps,
					#										image_interval))

					# Plot/save initial field
					write_field(field, 0)
					# Iterate
					t0 = time.time()
					iterate(field, field0, a, dx, dy, timesteps, image_interval)
					t1 = time.time()
					# Plot/save final field
					write_field(field, timesteps)

					newList.append([version, input_file, timesteps, "{0}".format(t1-t0)])

					#print("Simulation finished in {0} s".format(t1-t0))
	
				if version == 'Cython':    	
				# Initialise the temperature field
					field, field0 = init_fields_cyt(input_file)

					#print("Heat equation solver")
					#print("Diffusion constant: {}".format(a))
					#print("Input file: {}".format(input_file))
					#print("Parameters")
					#print("----------")
					#print("  nx={} ny={} dx={} dy={}".format(field.shape[0], field.shape[1],
					#								dx, dy))
					#print("  time steps={}  image interval={}".format(timesteps,
					#											image_interval))

					# Plot/save initial field
					write_field_cyt(field, 0)
					# Iterate
					t0 = time.time()
					iterate_cyt(field, field0, a, dx, dy, timesteps, image_interval)
					t1 = time.time()
					# Plot/save final field
					write_field_cyt(field, timesteps)
					
					newList.append([version, input_file, timesteps, "{0}".format(t1-t0)])

					#print("Simulation finished in {0} s".format(t1-t0))
	#print(newList)
	
	with open('results-A.csv', 'w', encoding='UTF8', newline='') as f:
		writer = csv.writer(f)

		# write the header
		writer.writerow(headResults)

		# write multiple rows
		writer.writerows(newList)

if __name__ == '__main__':

    # Process command line arguments
    parser = argparse.ArgumentParser(description='Heat equation')
    parser.add_argument('-dx', type=float, default=0.01,
                        help='grid spacing in x-direction')
    parser.add_argument('-dy', type=float, default=0.01,
                        help='grid spacing in y-direction')
    parser.add_argument('-a', type=float, default=0.5,
                        help='diffusion constant')
    parser.add_argument('-n', type=int, default=200,
                        help='number of time steps')
    parser.add_argument('-i', type=int, default=4000,
                        help='image interval')
    parser.add_argument('-f', type=str, default='bottle.dat', 
                        help='input file')

    args = parser.parse_args()

    main(args.f, args.a, args.dx, args.dy, args.n, args.i)

