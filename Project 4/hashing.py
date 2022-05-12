import random

# Function to determine hash value/position for Linear collision
# Linear collions genearlly leads to more collisions and values farther from their "original spot" due to clustering
def hashLinear(values, size, recordspace, collisionsLinear, collisionsquadratic):
    array = []

    # Generate array with -1's for record space
    for i in range(recordspace):
        array.append(-1)

    # Loop to delegate values to their respective location
    for i in range(size):
        currentValue = values[i]

        hash = (currentValue % recordspace) + 1

        if hash == recordspace:
            hash = 0

        if array[hash] == -1:
            array[hash] = currentValue
            print(f"Value {currentValue} hashed to {hash}")

        else:
            collisionsLinear += 1
            print(f"Value {currentValue} hashed to {hash}: COLLISION")
            collisionsLinear = linearCollision(recordspace, array, hash, currentValue, collisionsLinear)

    print(f"Number of collisions: {collisionsLinear}")

# Function to deal with collisions linearly
def linearCollision(recordspace, array, hash, currentValue, collisionsLinear):
    newHash = hash + 1

    if newHash == (recordspace - 1):
        newHash = 0

    elif newHash == hash:
        print("Recordspace is full!")

    if array[newHash] == -1:
        array[newHash] = currentValue
        print(f"Value {currentValue} hashed to {newHash}")

    else:
        collisionsLinear += 1
        print(f"Value {currentValue} hashed to {newHash}: COLLISION")
        collisionsLinear = linearCollision(recordspace, array, newHash, currentValue, collisionsLinear)

    return collisionsLinear

# Function to determine hash value/position for Quadratic Collision
# Quadratic collisions genearlly lead to less collisions becuase it spreads out the values
def hashQuadratic(values, size, recordspace, collisionsLinear, collisionsquadratic):
    array = []

    # Generate array with -1's for record space
    for i in range(recordspace):
        array.append(-1)

    print(len(array))

    # Loop to delegate values to their respective location
    for i in range(size):
        currentValue = values[i]

        hash = (currentValue % recordspace) + 1

        if hash == recordspace:
            hash = 0

        if array[hash] == -1:
            array[hash] = currentValue
            print(f"Value {currentValue} hashed to {hash}")

        else:
            print(f"Value {currentValue} hashed to {hash}: COLLISION")
            count = 1
            collisionsquadratic += 1
            collisionsquadratic = quadraticCollision(recordspace, array, hash, currentValue, collisionsquadratic, count)

    print(f"Number of collisions: {collisionsquadratic}")

# Function to deal with collisions quadraticaly
def quadraticCollision(recordspace, array, hash, currentValue, collisionsquadratic, count):
    newHash = hash + (count**2)

    if newHash == (recordspace - 1):
        newHash = 0

    elif newHash > (recordspace - 1):
        newHash = (newHash % (recordspace - 1))

    if array[newHash] == -1:
        array[newHash] = currentValue
        print(f"Value {currentValue} hashed to {newHash}")

    else:
        collisionsquadratic += 1
        print(f"Value {currentValue} hashed to {newHash}: COLLISION")
        count += 1
        hash = newHash
        collisionsquadratic = quadraticCollision(recordspace, array, hash, currentValue, collisionsquadratic, count)

    return collisionsquadratic

# Main function
def main():
    global collisionsLinear
    global collisionsquadratic

    # Define the recordspaces
    recordspacePrime = 31
    recordspace = 16

    collisionsLinear = 0
    collisionsquadratic = 0

    size = 10

    values = []

    #  Create array with random values
    for i in range(size):
        values.append(random.randint(0, 100))

    # Print array of values to be hashed
    print(f"The values are: {values}")

    # Generally has less collisions when using a prime number recordspace (also less populated with the values)
    print("\nLinear Collisions with recordspace = 31: ")
    hashLinear(values, size, recordspacePrime, collisionsLinear, collisionsquadratic)

    print("\nQuadratic Collisions with recordspace = 31: ")
    hashQuadratic(values, size, recordspacePrime, collisionsLinear, collisionsquadratic)

    # Generally has more collisions since using a non prime number and smaller recordspace close to the number of values being inserted
    print("\nLinear Collisions with recordspace = 16: ")
    hashLinear(values, size, recordspace, collisionsLinear, collisionsquadratic)

    print("\nQuadratic Collisions with recordspace = 16: ")
    hashQuadratic(values, size, recordspace, collisionsLinear, collisionsquadratic)

main()
