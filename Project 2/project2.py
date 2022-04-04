# create the matrix
def establishMatrix(value):
    # initialize matrix
    matrix = []
    print("Enter the values rowwise: ")

    # fill in matrix
    for i in range(value):                    # row entries
        a = []
        for j in range(value):             # column entries
            a.append(int(input()))
        matrix.append(a)

    # print matrix
    print("The Adjacency Matrix: ", matrix)

    return matrix

def adjacencyMatrix(matrix, value):
    # initalize matrix
    vector = []

    # Make Matrix
    for i in range(value):                      # go through rows
        a = []
        for j in range(value):                  # go through columns
            if matrix[i][j] == 1 or matrix[j][i] == 1:               # if (row, column) value is 1
                a.append(j)
        vector.append(a)

    for i in range(value):
        print(i, ": ", vector[i])


# find the vertices connected by vertices
def findEdges(matrix, value):
    # initalize the list of coordinate pairs
    list = []

    # look for coordinate pairs (WILL INCLUDE DUPLICATES)
    for i in range(value):                      # go through rows
        for j in range(value):                  # go through columns
            if matrix[i][j] == 1:               # if (row, column) value is 1
                matrix [j][i] = 0
                coordinate = (i, j)
                list.append(coordinate)

    # show list of coordinates
    print("List of edges: ", list)

    return list

def incidenceMatrix(value, list):
    columns = len(list)
    rows = value

    matrix = []

    for i in range(rows):
        a = []
        for j in range(columns):
            if list[j][0] == i or list[j][1] == i:
                a.append(1)
            else:
                a.append(0)
        matrix.append(a)

    print("Incidence Matrix: ", matrix)


def main():
    # initialize value for row and column
    value = int(input("Enter the number of vertices: "))

    matrix = establishMatrix(value)

    adjacencyMatrix(matrix, value)

    edgePairs = findEdges(matrix, value)

    incidenceMatrix(value, edgePairs)

main()
