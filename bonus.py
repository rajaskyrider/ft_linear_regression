import os

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd


def load_model(path: str = "./model_params.csv") -> tuple[float, float]:
	if not os.path.exists(path):
		return (0.0, 0.0)
	with open(path, "r") as f:
		f.readline()
		line = f.readline().strip()
	try:
		return tuple(map(float, line.split(",")))
	except ValueError:
		print("Invalid model parameters, using default values")
		return (0.0, 0.0)


def print_precision(km: pd.Series, price: pd.Series, theta0: float, theta1: float):
	predictions = theta0 + theta1 * km
	errors = predictions - price

	mse = (errors ** 2).mean()
	rmse = mse ** 0.5
	mae = errors.abs().mean()
	total_variation = ((price - price.mean()) ** 2).sum()
	residual_variation = (errors ** 2).sum()
	r2 = 1 - (residual_variation / total_variation)

	print(f"theta0: {theta0}")
	print(f"theta1: {theta1}")
	print(f"Mean Squared Error: {mse}")
	print(f"Root Mean Squared Error: {rmse}")
	print(f"Mean Absolute Error: {mae}")
	print(f"R-squared: {r2}")


def plot_data(km: pd.Series, price: pd.Series, theta0: float, theta1: float):
	plt.scatter(km, price, label="Dataset", color="steelblue")

	line_x = [km.min(), km.max()]
	line_y = [theta0 + theta1 * x for x in line_x]
	plt.plot(line_x, line_y, color="darkred", linewidth=2, label="Regression line")

	plt.xlabel("Mileage (km)")
	plt.ylabel("Price (EUR)")
	plt.title("Car Price vs Mileage")
	plt.gca().xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f"{int(x / 1000)}k"))
	plt.legend()
	plt.tight_layout()
	plt.show()


def main():
	df = pd.read_csv("./data.csv")
	km = df.loc[:, "km"]
	price = df.loc[:, "price"]
	theta0, theta1 = load_model()

	print_precision(km, price, theta0, theta1)
	plot_data(km, price, theta0, theta1)


if __name__ == "__main__":
	main()
