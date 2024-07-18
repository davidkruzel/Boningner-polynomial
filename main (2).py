# determine if a graph is connected
def is_connected(graph_edges, num_vertices):
  if graph_edges == []:
    return False
  connected_vertices = set()
  connected_vertices = connected_vertices.union(graph_edges[0][2])
  test = 0
  while test < 1:
    for v in connected_vertices:
      for edge in graph_edges:
        if (v in edge[2]) and (edge[2].issubset(connected_vertices) == False):
          connected_vertices = connected_vertices.union(edge[2])
          test += 1
    if test == 0:
      if (len(connected_vertices) < num_vertices):
        return False
      else:
        return True
    else:
      test = 0

# determine if a subgraph is a spanning subtree of a given graph
def is_spanning_tree(num_vertices_of_graph, subgraph_edges):
  if not is_connected(subgraph_edges, num_vertices_of_graph):
    return False
  vertices_in_subgraph = set()
  for edge in subgraph_edges:
    vertices_in_subgraph = vertices_in_subgraph.union(edge[2])
  if ( len(vertices_in_subgraph) == num_vertices_of_graph ) and ( len(subgraph_edges) == (num_vertices_of_graph - 1)):
    return(True)
  else:
    return(False)

def is_check_colorable(gauss_code):
  for knot_edge in edge_list_sign(gauss_code):
    for j in edge_list_sign(gauss_code):
      if j[1] == knot_edge[0] and j[2] == knot_edge[2]:
        return(False)
      if ( (-1) * j[1] ) == knot_edge[0] and j[2] != knot_edge[2]:
        return(False)
      if ( (-1) * j[0] ) == knot_edge[0] and j[2] == knot_edge[2]:
        return(False)
  return(True)
  
def edge_list_sign(gauss_code):
  sign = 1
  m = []
  for i in range(len(gauss_code)):
    if i < len(gauss_code) - 1:
      a = gauss_code[i]
      b = gauss_code[i + 1]
      m.append([a, b, sign])
      sign *= -1
    else:
      a = gauss_code[i]
      b = gauss_code[0]
      m.append([a, b, sign])
  return(m)

def edge_list(gauss_code):
  m = []
  for i in range(len(gauss_code)):
    if i < len(gauss_code) - 1:
      a = gauss_code[i]
      b = gauss_code[i + 1]
      m.append([a, b])
    else:
      a = gauss_code[i]
      b = gauss_code[0]
      m.append([a, b])
  return(m)

# calculate the next knot edge in our graph 
# knot_edge is something like [ [2, -3], 'R']
# direction is something like 'F'
def next(gauss_code, crossings, knot_edge, direction):
  start_crossing = knot_edge[0][0]
  end_crossing = knot_edge[0][1]
  abs_end = abs(knot_edge[0][1])
  abs_start = abs(knot_edge[0][0])
  if direction == 'F':
    if knot_edge[1] == 'R' and crossings[abs(end_crossing) - 1] == 1:
      if end_crossing < 0:
        for i in edge_list(gauss_code):
          if i[0] == abs_end:
            return [ [i, 'R'], 'F']
      if end_crossing > 0:
        for i in edge_list(gauss_code):
          if i[1] == -abs_end:
            return [ [i, 'L'], 'B']
    if knot_edge[1] == 'R' and crossings[abs(end_crossing) - 1] == -1:
      if end_crossing < 0:
        for i in edge_list(gauss_code):
          if i[1] == abs_end:
            return [ [i, 'L'], 'B']
      if end_crossing > 0:
        for i in edge_list(gauss_code):
          if i[0] == -abs_end:
            return [ [i, 'R'], 'F']
    if knot_edge[1] == 'L' and crossings[abs(end_crossing) - 1] == 1:
      if end_crossing < 0:
        for i in edge_list(gauss_code):
          if i[1] == abs_end:
            return [ [i, 'R'], 'B']
      if end_crossing > 0:
        for i in edge_list(gauss_code):
          if i[0] == -abs_end:
            return [ [i, 'L'], 'F']
    if knot_edge[1] == 'L' and crossings[abs(end_crossing) - 1] == -1:
      if end_crossing < 0:
        for i in edge_list(gauss_code):
          if i[0] == abs_end:
            return [ [i, 'L'], 'F']
      if end_crossing > 0:
        for i in edge_list(gauss_code):
          if i[1] == -abs_end:
            return [ [i, 'R'], 'B']
  if direction == 'B':
    if knot_edge[1] == 'R' and crossings[abs(start_crossing) - 1] == 1:
      if start_crossing < 0:
        for i in edge_list(gauss_code):
          if i[0] == abs_start:
            return [ [i, 'L'], 'F']
      if start_crossing > 0:
        for i in edge_list(gauss_code):
          if i[1] == -abs_start:
            return [ [i, 'R'], 'B']
    if knot_edge[1] == 'R' and crossings[abs(start_crossing) - 1] == -1:
      if start_crossing < 0:
        for i in edge_list(gauss_code):
          if i[1] == abs_start:
            return [ [i, 'R'], 'B']
      if start_crossing > 0:
        for i in edge_list(gauss_code):
          if i[0] == -abs_start:
            return [ [i, 'L'], 'F']
    if knot_edge[1] == 'L' and crossings[abs(start_crossing) - 1] == 1:
      if start_crossing < 0:
        for i in edge_list(gauss_code):
          if i[1] == abs_start:
            return [ [i, 'L'], 'B']
      if start_crossing > 0:
        for i in edge_list(gauss_code):
          if i[0] == -abs_start:
            return [ [i, 'R'], 'F']
    if knot_edge[1] == 'L' and crossings[abs(start_crossing) - 1] == -1:
      if start_crossing < 0:
        for i in edge_list(gauss_code):
          if i[0] == abs_start:
            return [ [i, 'R'], 'F']
      if start_crossing > 0:
        for i in edge_list(gauss_code):
          if i[1] == -abs_start:
            return [ [i, 'L'], 'B']
            
# calculate the opposite knot edge in our graph
def opp(gauss_code, crossings, knot_edge):
  knot_edge2 = knot_edge[0]
  for i in edge_list(gauss_code):
    if i[0] == knot_edge[0][1] and knot_edge[1] == 'L':
      return([i, 'R']) 
    if i[0] == knot_edge[0][1] and knot_edge[1] == 'R':
      return([i, 'L'])
      
def tait_A(gauss_code, crossings):

  # make a list of all edges on our knot
  sides = []
  for i in edge_list(gauss_code):
    sides.append([i, 'R'])
    sides.append([i, 'L'])

  # create a list of vertices in our tait graph
  # each vertex is actually a list of the knot edges which comprise it
  vertices = [[]]
  vertices[0].append([ sides[0], 'F' ])

  # make a list of all knot edges in our tait graph
  included = []
  included.append(sides[0])

  # generate the first vertex of our tait graph
  resume = True
  edge = vertices[0][-1]
  while resume:
    if next(gauss_code, crossings, edge[0], edge[1]) == [ sides[0], 'F']:
      resume = False
    else:
      edge = next(gauss_code, crossings, edge[0], edge[1])
      vertices[0].append(edge)
      included.append(edge[0])

  # generate the rest of our tait graph
  resume = True
  while resume:
    resume = False
    for v in vertices:
      for s in v: 
        o = opp(gauss_code, crossings, s[0])
        if o not in included:
          resume = True
          included.append(o)
          vertices.append([])
          (vertices[-1]).append([o, 'F'])
          resume2 = True
          edge = vertices[-1][-1]
          while resume:
            if next(gauss_code, crossings, edge[0], edge[1]) == [ o, 'F']:
              resume = False
            else:
              edge = next(gauss_code, crossings, edge[0], edge[1])
              vertices[-1].append(edge)
              included.append(edge[0]) 

  # create a new list of vertices, this time getting rid of the direct F/B
  vertex = []
  for v in vertices:
    vertex.append([])
    for s in v:
      vertex[-1].append(s[0])

  # create a list of edges which represents the tait graph
  edges = []
  for c in range(1, (len(gauss_code) // 2) + 1):
    for v in vertex:
      for s in v:
        if s[0][1] == -c:
          for v2 in vertex:
            for s2 in v2:
              if s2[0][0] == -c:
                  if s[1] == 'R':
                    edges.append([c, -1, {vertex.index(v), vertex.index(v2)}])
                  else:
                    edges.append([c, 1, {vertex.index(v), vertex.index(v2)}])
                    
  return(edges)

def tait_B(gauss_code, crossings):

  # make a list of all edges on our knot
  sides = []
  for i in edge_list(gauss_code):
    sides.append([i, 'L'])
    sides.append([i, 'R'])

  # create a list of vertices in our tait graph
  # each vertex is actually a list of the knot edges which comprise it
  vertices = [[]]
  vertices[0].append([ sides[0], 'F' ])

  # make a list of all knot edges in our tait graph
  included = []
  included.append(sides[0])
  
  # generate the first vertex of our tait graph
  resume = True
  edge = vertices[0][-1]
  while resume:
    if next(gauss_code, crossings, edge[0], edge[1]) == [ sides[0], 'F']:
      resume = False
    else:
      edge = next(gauss_code, crossings, edge[0], edge[1])
      vertices[0].append(edge)
      included.append(edge[0])
  
  # generate the rest of our tait graph
  resume = True
  while resume:
    resume = False
    for v in vertices:
      for s in v: 
        o = opp(gauss_code, crossings, s[0])
        if o not in included:
          resume = True
          included.append(o)
          vertices.append([])
          (vertices[-1]).append([o, 'F'])
          resume2 = True
          edge = vertices[-1][-1]
          while resume:
            if next(gauss_code, crossings, edge[0], edge[1]) == [ o, 'F']:
              resume = False
            else:
              edge = next(gauss_code, crossings, edge[0], edge[1])
              vertices[-1].append(edge)
              included.append(edge[0]) 
  
  # create a new list of vertices, this time getting rid of the direct F/B
  vertex = []
  for v in vertices:
    vertex.append([])
    for s in v:
      vertex[-1].append(s[0])
  
  # create a list of edges which represents the tait graph
  edges = []
  for c in range(1, (len(gauss_code) // 2) + 1):
    for v in vertex:
      for s in v:
        if s[0][1] == -c:
          for v2 in vertex:
            for s2 in v2:
              if s2[0][0] == -c:
                  if s[1] == 'R':
                    edges.append([c, -1, {vertex.index(v), vertex.index(v2)}])
                  else:
                    edges.append([c, 1, {vertex.index(v), vertex.index(v2)}])
  
  return(edges)

def tau(graph_edges, num_vertices_of_graph, num_edges_of_graph, writhe):

  # Define a list which will be the end result. 
  total_sum = []

  # Parse all subgraphs of graph_edges.
  for index in range(2 ** num_edges_of_graph ):
    index_binary = str(bin(index))[2:]
    while len(index_binary) < num_edges_of_graph:
      index_binary = '0' + index_binary
    subgraph_edges = []
    for i in range(num_edges_of_graph ):
      if index_binary[i] == '1':
        subgraph_edges.append(graph_edges[i])
    if is_spanning_tree(num_vertices_of_graph, subgraph_edges):
      sign = 1
      power = 0

      # Parse the edges in the graph, determine value of each
      for initial_edge in graph_edges:

        # Define the list cut_cyc.
        # If initial_edge in subgraph_edges, then cut_cyc is the list of labels of the edges in cut(initial_edge).
        # If initial_edge not in subgraph_edges, then cut_cyc is the list of labels of the edges in cyc(initial_edge).
        cut_cyc = [initial_edge[0]]
        for different_edge in graph_edges:
          new_subgraph = []
          if initial_edge in subgraph_edges: 
            new_subgraph = [different_edge]
          else:
            new_subgraph = [initial_edge]
          for edge in subgraph_edges:
            if (edge != initial_edge) and (edge != different_edge):
              new_subgraph.append(edge)
          if is_spanning_tree(num_vertices_of_graph, new_subgraph):
            cut_cyc.append(different_edge[0])

        # Determine whether of not initial_edge is active or not. 
        # Define the power and sign of the corresponding 'A' term accordingly. 
        if initial_edge in subgraph_edges:
          power_multiple = 1
        else:
          power_multiple = -1
        if initial_edge[0] == min(cut_cyc):
          sign *= -1
          power += (power_multiple * (-3) * initial_edge[1])
        else:
          power += (power_multiple * initial_edge[1])

      # Correct the total sum. 
      test = 0
      for i in range(len(total_sum)):
        if total_sum[i][1] == power:
          test += 1
          total_sum[i][0] += sign
      if test == 0:
        total_sum.append([sign, power])

  # Correct the total sum if it is empty
  if total_sum == []:
    sum_of_signs = 0
    for edge in graph_edges:
      sum_of_signs += edge[1]
    sign = int((-1) ** sum_of_signs)
    power = 3 * sum_of_signs
    total_sum = [[sign, power]]

  # add the correct factor for the writhe
  power = int( (-3) * writhe )
  sign = int( (-1) ** power )
  for i in range(len(total_sum)):
    total_sum[i][0] *= sign
    total_sum[i][1] += power

  # Turn total_sum into a nice-looking output. 
  powers = []
  for i in range(len(total_sum)):
    powers.append(total_sum[i][1])
  powers.sort()
  solution = ''
  for i in range(len(powers)):
    power = powers[i]
    for term in total_sum:
      if term[1] == power:
        sign = term[0]
    sign = str(sign)
    num = sign
    if sign[0] == '-':
      num = sign[1:]
    power = str(power)
    if num == '1' and power != '0':
      num = ''
    if num == '0':
      pass
    elif sign[0] == '-':
      solution = solution + ' - '
    elif i != 0:
      solution = solution + ' + '
    if num == '0':
      pass
    elif power != '0':
      solution = solution + num + 'A^(' + power + ')'
    else:
      solution = solution + num

  return solution

# determine if a user-given-input is valid, and if so, return the Gauss code
def if_valid_give_code(input):
  
  # determine if the format of the code is correct
  # compile the information into separate lists
  counter = 0
  previous_num_index = None
  crossing_nums = []
  crossing_over_or_under = []
  crossing_sign = []
  for i in range(len(input)):
    if input[i].isnumeric():
      if previous_num_index == i-1:
        crossing_nums[-1] = crossing_nums[-1] + input[i]
        previous_num_index = i
      else:
        crossing_nums.append(input[i])
        previous_num_index = i
    else:
      if (input[i] == 'o') or (input[i] == 'u'):
        crossing_over_or_under.append(input[i])
        if not counter % 3 == 0:
          return False
        counter += 1
      elif (input[i] == '+') or (input[i] == '-'):
        crossing_sign.append(input[i])
        if not counter % 3 == 1:
          return False
        counter += 1
      elif input[i] == ',':
        if not counter % 3 == 2:
          return False
        counter += 1
      else:
        return False
        
  # obtain a list with the gauss code
  gauss_code = []
  crossings = []
  labels = ([0] * len(crossing_nums))
  count = 1
  for i in range(len(crossing_nums)):
    pair = []
    for j in range(len(crossing_nums)):
      if crossing_nums[i] == crossing_nums[j]:
        pair.append(j)
    if len(pair) != 2:
      return False
    c1 = min(pair)
    c2 = max(pair)
    if crossing_over_or_under[c1] == crossing_over_or_under[c2]:
      return False
    if crossing_sign[c1] != crossing_sign[c2]:
      return False
    if i == c1:
      labels[c1] = count
      count += 1
      if crossing_sign[c1] == '+':
        crossings.append(1)
      else:
        crossings.append(-1)
    if crossing_over_or_under[i] == 'o':
      gauss_code.append(labels[c1])
    else:
      gauss_code.append(-labels[c1])
  return [gauss_code, crossings]

def prompt_user():
  print('Please enter a valid knot or type "quit"')
  prompt = input(': ')
  if prompt == 'quit':
    return False
  if not if_valid_give_code(prompt):
    print('This is not a valid input')
    return True
  else:
    input_knot = if_valid_give_code(prompt)
    if not is_check_colorable(input_knot[0]):
      print('This knot is not checkerboard colorable')
      return True
    else:
      taitA = tait_A(input_knot[0], input_knot[1])
      taitB = tait_B(input_knot[0], input_knot[1])
      verticesA = set()
      for i in taitA:
        verticesA = verticesA.union(i[2])
      verticesB = set()
      for i in taitB:
        verticesB = verticesB.union(i[2])
      num_verticesA = len(verticesA)
      num_edgesA = len(taitA)
      num_verticesB = len(verticesB)
      num_edgesB= len(taitB)
      writhe = 0
      for i in input_knot[1]:
        writhe += i
      print(tau(taitA, num_verticesA, num_edgesA, writhe))
      print(tau(taitB, num_verticesB, num_edgesA, writhe))
      return True
    
# start the program
def main():
  while prompt_user():
    pass

main()

          
    




      
        
          
          
        
      



  
  
  
  


    





    


  