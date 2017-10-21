"""
Searches module defines all different search algorithms
"""
import Queue
import heapq


def bfs(graph, initial_node, dest_node):
	"""
	Breadth First Search
	uses graph to do search from the initial_node to dest_node
	returns a list of actions going from the initial node to dest_node
	"""
	queue = Queue.Queue()
	trail = []
	visited = {}
	#creates queue, list and dictionary variables
	#queue to traverse the graph
	#trail to keep list copy of node path
	#visited boolean dictionary to make sure path doesnt go to same node

	for nodes in graph.get_nodes():
		visited[nodes] = False
	#sets all values in visited dictionary to false

	queue.put(initial_node)
	#adds initial_node to queue

	while not queue.empty():
		current = queue.get()
	#while loop to continue as long as queue is not empty

		if current is dest_node:
			break

		if not visited[current] == True:
			visited[current] = True
			trail.append(current)
		#if node has not been visited
		#lets trail know that node has been visited
		#append node to trail

			for node in graph.neighbors(current):
				if node not in trail:
					queue.put(node)
			#adds all neighbors to queue to have them traversed

				# if node == dest_node:
				# 	found_node = True
				# 	trail.append(node)
				# 	break
	# print trail
	result = []
	#create result list for final path

	trail.reverse()
	#reverses trail to traverse backwards

	trail2 = list(trail)
	trail2.reverse()
	#creates copy of trail to trail2
	#reverses trail2 setting it to start from beginning node

	checkNode = dest_node
	#sets checkNode to destination node

	for node_back in trail:
	#traversing the trail backwards, starting from the last node in trail

		reset = False
		#sets resent to False so iterate through all loops

		if node_back == checkNode:
		#checks if node is checkNode

			for node_forward in trail2:
			#loop going forward to check edges

				if reset:
					break
				#if reset is true, breaks out of loop

				temp = node_forward
				#sets temp to foward_node to check in next loop
				#for some reason, unable to call node_foward in following for loop

				for node in graph.neighbors(node_forward):
				#for loop for each neighbor of node_forward/temp

					if node == node_back:
					#if neighbor of node_forward equals node_back

						checkNode = temp
						#if checkNode equals temp/node_forward

						result.append(graph.get_edge(temp, node_back))
						#append edge to result

						reset = True
						break
						#sets reset to true to back up to 1st for loop


	result.reverse()
	#reverse the result

	return(result)
	#returns result

def dfs(graph, initial_node, dest_node):
	"""
	Depth First Search
	uses graph to do search from the initial_node to dest_node
	returns a list of actions going from the initial node to dest_node
	"""
	nodeStack = Stack()
	trail = []
	visited = {}
	#creates stack, list and dictionary variables
	#stack to traverse the stack
	#trail to keep list copy of node path
	#visited boolean dictionary to make sure path doesnt go to same node

	for nodes in graph.get_nodes():
		visited[nodes] = False
	#sets all values in visited dictionary to false

	nodeStack.push(initial_node)
	#pushes the root node to the stack

	visited[initial_node] = True
	#sets root node to visited

	while not nodeStack.is_empty():
	#while loop to continue  as long as nodeStack is not empty

		current = nodeStack.peek()
		#sets current to current node

		if current == dest_node:
			trail.append(current)
			break
		#checks to see if current node is the destination node
		#then appends the current node to the trail
		#breaks while loop if destination is reached

		if current not in trail:
			trail.append(current)
		#adds node to trail, only if the node is not already in trail

		if graph.neighbors(current) != []:
		#makes sure the current node has neighbors (or children)

			for node in graph.neighbors(current):
			#iterates through each element in the key
				if not visited[node] == True:
				#checks to see if node has been visited

					nodeStack.push(node)
					visited[node] = True
					break
					#if node has not been visited, pushes upcoming node to stack
					#sets upcoming node to visited
					#breaks for loop to go back into while loop
		else:
			nodeStack.pop()
			trail = trail[:-1]
		#since node has no children, we must traverse back
		#pops current stack and erases last value in list
		#goes back into while loop


	result = []
	#empty list to input edge results

	for i, nexti in zip(trail,trail[1::]):
	#loop created to get current item and next item

		result.append(graph.get_edge(i, nexti))
		#call upon get_edge method in graph to get edge and weight
		#input values are current edge to next edge

	return result
	#returns results to be checked

def dijkstra_search(graph, initial_node, dest_node):
	"""
	Dijkstra Search
	uses graph to do search from the initial_node to dest_node
	returns a list of actions going from the initial node to dest_node
	"""

	heap = []
	heapq.heappush(heap, (0, initial_node))
	trail = []

	came_from = {}
	cost_so_far = {}

	came_from[initial_node] = None
	cost_so_far[initial_node] = 0

	while not heap == []:
		current = heapq.heappop(heap)

		if current[-1] == dest_node:
			break

		for node in graph.neighbors(current[-1]):
			new_cost = cost_so_far[current[-1]] + graph.get_weight(current[-1], node)

			if node not in cost_so_far or new_cost < cost_so_far[node]:
				cost_so_far[node] = new_cost
				priority = new_cost
				heapq.heappush(heap, (priority, node))
				came_from[node] = current[-1]

	result = []
	current = dest_node
	trail.append(current)
	while came_from[current] is not initial_node:
		trail.append(came_from[current])
		current = came_from[current]

	trail.append(initial_node)
	trail.reverse()

	for i, nexti in zip(trail,trail[1::]):
	#loop created to get current item and next item
		result.append(graph.get_edge(i, nexti))
		#call upon get_edge method in graph to get edge and weight
		#input values are current edge to next edge

	return(result)


def a_star_search(graph, initial_node, dest_node):
	"""
	A* Search
	uses graph to do search from the initial_node to dest_node
	returns a list of actions going from the initial node to dest_node
	"""
	heap = []
	heapq.heappush(heap, (0, initial_node))
	trail = []

	came_from = {}
	cost_so_far = {}

	came_from[initial_node] = None
	cost_so_far[initial_node] = 0

	while not heap == []:
		current = heapq.heappop(heap)

		if current[-1] == dest_node:
			break

		for node in graph.neighbors(current[-1]):
			new_cost = cost_so_far[current[-1]] + graph.get_weight(current[-1], node)

			if node not in cost_so_far or new_cost < cost_so_far[node]:
				cost_so_far[node] = new_cost
				priority = new_cost
				heapq.heappush(heap, (priority, node))
				came_from[node] = current[-1]

	result = []
	current = dest_node
	trail.append(current)
	while came_from[current] is not initial_node:
		trail.append(came_from[current])
		current = came_from[current]

	trail.append(initial_node)
	trail.reverse()

	for i, nexti in zip(trail, trail[1::]):
		# loop created to get current item and next item
		result.append(graph.get_edge(i, nexti))
	# call upon get_edge method in graph to get edge and weight
	# input values are current edge to next edge

	return (result)


class Stack:
	def __init__(self):
		self.items = []

	# I have changed method name isEmpty to is_empty
	# because in your code you have used is_empty
	def is_empty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)
