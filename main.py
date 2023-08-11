from time import sleep
from os import  system
Black = "█"
White = "▒"

MaxIntMatrixY = int(input("Max Y Coordinate: "))
MaxIntMatrixX = int(input("Max X Coordinate: "))

def CreateMatrix(defVal):
	MatrixList = []
	for j in range(0, MaxIntMatrixY):
		MatrixList2 = []
		for i in range(0, MaxIntMatrixX):
			MatrixList2.append(defVal)
		MatrixList.append(MatrixList2)
	return MatrixList

def PrintMatrix(MatrixObj):
	system('cls')
	system('clear')
	for row in MatrixObj:
		for cell in row:
			if cell:
				print(f"{Black}", end="")
			else:
				print(f"{White}", end="")
		print()

def CountLiveNeighbors(matrix, y, x):
	live_neighbors = 0
	for dy in [-1, 0, 1]:
		for dx in [-1, 0, 1]:
			if dy == 0 and dx == 0:
				continue
			new_y, new_x = y + dy, x + dx
			if 0 <= new_y < MaxIntMatrixY and 0 <= new_x < MaxIntMatrixX and matrix[new_y][new_x]:
				live_neighbors += 1
	return live_neighbors

BnMatrix = CreateMatrix(0)
PrintMatrix(BnMatrix)

Flag = "R"  # 'R' -> True / 'N' -> False
while Flag == "R":
	intCoordY = int(input(f"Give Y Coordinate [Max: {MaxIntMatrixY} ]: ")) - 1
	intCoordX = int(input(f"Give X Coordinate [Max: {MaxIntMatrixX} ]: ")) - 1

	if intCoordY < 0 or intCoordY >= MaxIntMatrixY or intCoordX < 0 or intCoordX >= MaxIntMatrixX:
		print("Coordinates out of bounds. Please try again.")
		continue

	BnMatrix[intCoordY][intCoordX] = 1
	PrintMatrix(BnMatrix)

	strConfirm = input('Type S to start simulation: ')
	if (strConfirm == 'S'):
		intExecutionRuntime = int(input('Times to run the simulation: '))
		if strConfirm == "S":
			Flag = "N"

# Beginning of game logic
for _ in range(intExecutionRuntime):
	new_matrix = []

	for Y in range(MaxIntMatrixY):
		new_row = []
		for X in range(MaxIntMatrixX):
			live_neighbors = CountLiveNeighbors(BnMatrix, Y, X)
			if BnMatrix[Y][X]:
				if live_neighbors < 2 or live_neighbors > 3:
					new_row.append(0)
				else:
					new_row.append(1)
			else:
				if live_neighbors == 3:
					new_row.append(1)
				else:
					new_row.append(0)
		new_matrix.append(new_row)

	BnMatrix = new_matrix
	PrintMatrix(BnMatrix)
	sleep(0.2)
	print()