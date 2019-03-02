#!/usr/bin/python3
#coding = utf-8

import numpy as np
import matplotlib.pyplot as plt

def get_location():
	return np.random.random((20, 2))

def cal_dist(city):
	number = city.shape[0]
	dist = np.zeros((number, number))
	for i in range(0, number):
		for j in range(0, i + 1):
			dx = city[i][0] - city[j][0]
			dy = city[i][1] - city[j][0]
			dist[i][j] = dist[j][i] = np.sqrt(dx**2 + dy**2)
	return dist

def cal_total_dist(dist, route):
	total_dist = 0
	for i in range(0, len(route) - 1):
		total_dist += dist[route[i] - 1][route[i + 1] - 1]
	return total_dist

def gen_init_route(number, dist):
	unvisited = list(range(1, number + 1))
	init_route = []
	rest = list(range(1, number))
	rest.reverse()
	for i in rest:
		init_route.append(unvisited.pop(np.random.randint(i)))
	init_route.append(unvisited[0])
	init_route.append(init_route[0])
	init_dist = cal_total_dist(dist, init_route)
	return init_route, init_dist

def swap_city(number, dist, times_of_swap):
	route, distance = gen_init_route(number, dist)
	route_rslt = []
	dist_rslt = []
	route_rslt.append(route)
	dist_rslt.append(distance)
	for i in range(0, times_of_swap):
		city1 = np.random.randint(1, number)
		city2 = np.random.randint(1, number)
		temp = route[city1]
		route[city1] = route[city2]
		route[city2] = temp
		route_rslt.append(route)
		dist_rslt.append(cal_total_dist(dist, route))
	final_dist = min(dist_rslt)
	final_route = route_rslt[dist_rslt.index(final_dist)]
	return final_route, final_dist

def select_route(number, dist, times_of_select, times_of_swap):
	route_rslt = []
	dist_rslt = []
	for i in range(0, times_of_select):
		route, distance = swap_city(number, dist, times_of_swap)
		route_rslt.append(route)
		dist_rslt.append(distance)
	final_dist = min(dist_rslt)
	final_route = route_rslt[dist_rslt.index(final_dist)]
	return final_route, final_dist

city = get_location()
dist = cal_dist(city)
route, final_dist = select_route(city.shape[0], dist, 100, 1000)
print("The shortest route is:", route)
print("Total distance is:", final_dist)

route_in_xy = []
for i in route:
	route_in_xy.append(city[i - 1])
route_in_xy = np.asarray(route_in_xy)

x = np.hsplit(route_in_xy, 2)[0]
y = np.hsplit(route_in_xy, 2)[1]
plt.scatter(x, y)
plt.plot(x, y)
plt.show()
