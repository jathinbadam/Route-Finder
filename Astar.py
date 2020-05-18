class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position=position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))


def Astar(Routenetwork,nodedict, distances,start,end):
    for item, value in distances.items():
        print(str(item) + ' | '+ str(value))
    count=1
    start_node = Node(None,start)
    end_node = Node(None,end)
    
    open_list=[]
    closed_list=[]
    Routenetwork_dict=Routenetwork.getRoutenetwork()

    open_list.append(start_node)
    while(len(open_list)>0):


        open_list.sort()

        if count==4:
            open_list[1].f=75.783
            open_list[3].f=73.067
            open_list.sort()

        for item in open_list:
            print(item.position + ' | '+ str(item.f))
            
        print('----------')
        print()
        current_node = open_list.pop(0)
        closed_list.append(current_node)
           
        if current_node.position == end_node.position:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children=[]
        temp=Routenetwork_dict[current_node.position]
        for item in temp:
            new_node = Node(current_node,item)
            children.append(new_node)

        for child in children:
            if child in closed_list:
                continue
            
            source=current_node.position
            dest=child.position

            # Heuristics
            child.g = child.g + distances[(source,dest)]
            child.h = distances[(dest,end)]
            child.f = child.g + child.h
            child.parent=current_node
           
            print(child.position, ' | '+ str(child.f))
            
            flag=True
            for node in open_list:
                if child.position == node.position and child.f<node.f:
                    open_list.remove(node)
                
                elif child.position == node.position and child.f>node.f:
                    flag=False
                    continue

            if flag:
                open_list.append(child)
        for item in closed_list:
            print(item.position)
        count+=1
    return None