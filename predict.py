import os

def main():
	path = "./model_params.csv"
	if not os.path.exists(path):
		print ("Model Parameters unavailable. Please train the model first")
		return
	with open(path, "r") as f:
		f.readline()
		line = f.readline().strip()
		try:
			theta0, theta1 = map(float, line.split(","))
		except (ValueError):
			print("Invalid Model parameters")
			return
	while True:
		try:
			mileage = float(input("Enter the mileage (in KM): "))
			if mileage >= 0:
				break
			else:
				print("Mileage cannot be negative")
		except (ValueError):
			print("Invalid input! Please enter a number")
	price = theta0 + theta1 * mileage
	print(f"Price of the car with a mileage of {mileage}KM is {price}EUR")

if __name__ == "__main__":
	main()