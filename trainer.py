import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

class regression:
	def __init__(self, theta0:int, theta1:int, learning_rate:float = 0.1, threshold:float = 0.0001, iter:int = 1000, path:str ="./model_params.csv"):
		self.theta0 = theta0
		self.theta1 = theta1
		self.learning_rate = learning_rate
		self.eps = threshold
		self.iter = iter
		self.path = path
	
	def save_model(self):
		with open(self.path, "w") as f:
			f.write("theta0,theta1\n")
			f.write(f"{self.theta0},{self.theta1}\n")

	def train(self, mileage:pd.Series, price:pd.Series):
		m = mileage.size
		mean_km = mileage.mean()
		std_km = mileage.std()
		mileage_scaled  = (mileage - mean_km) / std_km
		for iteration in range(self.iter):
		#while (True):
			error = self.theta0 + (self.theta1 * mileage_scaled) - price
			#print("error : ", error.sum())
			tmp0 = self.learning_rate * error.sum() / m
			#print("tmp0 : ", tmp0)
			tmp1 = self.learning_rate * (error * mileage_scaled).sum() / m
			#print("tmp1 : ", tmp1)
			self.theta0 -= tmp0
			self.theta1 -= tmp1
			if (abs(tmp0) < self.eps and abs(tmp1) < self.eps):
				break
		self.theta1 = self.theta1 / std_km
		self.theta0 = self.theta0 - self.theta1 * mean_km
		self.save_model()


def main():
	df = pd.read_csv("./data.csv")
	#print (df.head())
	km = df.loc[:,"km"] 
	price = df.loc[:,"price"]
	#plt.scatter(km, price)
	#plt.xlabel("Mileage (km)")
	#plt.ylabel("Price (EUR)")
	#plt.title("Price vs Mileage")
	#plt.gca().xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f"{int(x / 1000)}k"))
	#plt.show()
	reg = regression(0,0)
	reg.train(km, price)


if __name__ == "__main__":
	main()