import random
import matplotlib.pyplot as plt


def logistic_population_growth(P_prev, r, K, years, total_years, population_data):
    if years == 0:
        return
    # Random event: disease outbreak
    if random.random() < 0.05:  # 5% chance of disease outbreak
        P_prev *= 0.7  # Population reduces by 30%
        print("Disease outbreak! Population reduced by 30%.")

    # Seasonal variation in growth rate
    seasonal_factor = 0.8 + 0.4 * (years % 2)
    r_seasonal = r * seasonal_factor

    P_t = P_prev + r_seasonal * P_prev * (1 - P_prev / K)
    population_data.append(P_t)
    print(f"Year {total_years - years + 1}: Population = {P_t:.2f}")
    logistic_population_growth(P_t, r, K, years - 1, total_years, population_data)


initial_population = float(input("Enter the initial population: "))
growth_rate = float(input("Enter the growth rate (between 0 and 1): "))
carrying_capacity = float(input("Enter the carrying capacity: "))
num_years = int(input("Enter the number of years to simulate: "))

population_data = [initial_population]

logistic_population_growth(initial_population, growth_rate, carrying_capacity, num_years, num_years, population_data)

plt.plot(range(num_years + 1), population_data)
plt.xlabel('Years')
plt.ylabel('Population')
plt.title('Rabbit Population Growth Over Time')
plt.show()