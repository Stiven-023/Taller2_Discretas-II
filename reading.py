from graph import Graph

class Reading(object):

    def reader(self, file):
        a_graph=Graph()
        with open(file) as a_file:
            read = a_file.readlines()
            for line in read:
                lines = [line.rstrip() for line in read if not(line.startswith("#"))]   
        print(lines[0])
        print(lines[1:])
        a_graph.set_type(lines[0])
        a_graph.parse(lines[1:])

   

filename = 'grafoFile/GD-LA-0003-001.txt'
texto = Reading()
texto.reader(filename)


  
  

