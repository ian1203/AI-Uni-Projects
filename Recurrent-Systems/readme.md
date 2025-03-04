# Rabbit Population Growth Simulation

This script simulates the growth of a rabbit population in a closed ecosystem using the **logistic growth model**. The simulation takes into account the carrying capacity of the ecosystem, which limits the population growth as resources become scarce.

---

## Table of Contents
1. [Overview](#overview)
2. [Logistic Growth Model](#logistic-growth-model)
3. [How to Use](#how-to-use)
4. [Input Parameters](#input-parameters)
5. [Output](#output)
6. [Example](#example)
7. [Dependencies](#dependencies)
8. [License](#license)

---

## Overview
The program uses a recursive approach to model the growth of a rabbit population over a specified number of years. The population growth is influenced by:
- **Growth rate (r)**: The rate at which the population grows.
- **Carrying capacity (K)**: The maximum population size the ecosystem can support.

The simulation also includes random events (e.g., disease outbreaks) and seasonal variations to make the model more realistic.

---

## Logistic Growth Model
The population growth is modeled using the following recursive formula:

P_t = P_(t-1) + r × P_(t-1) × (1 - P_(t-1) / K)


Where:
- \(P_t\): Population in year \(t\).
- \(P_{t-1}\): Population in the previous year.
- \(r\): Growth rate (between 0 and 1).
- \(K\): Carrying capacity.

---

## How to Use
1. Clone the repository or download the Python script.
2. Ensure you have Python installed (preferably Python 3.8 or higher).
3. Install the required dependencies (see [Dependencies](#dependencies)).
4. Run the script using the command:
   ```bash
   python rabbit_population.py
   ```
5. Follow the prompts to input the required parameters.

---

## Input Parameters
The program requires the following inputs:
- **Initial Population**: The starting number of rabbits.
- **Growth Rate (r)**: A value between 0 and 1 that determines how quickly the population grows.
- **Carrying Capacity (K)**: The maximum number of rabbits the ecosystem can support.
- **Number of Years**: The number of years to simulate.

---

## Output
The program outputs the population for each year, taking into account:
- **Seasonal Variations**: The growth rate fluctuates slightly each year to simulate seasonal changes.
- **Random Events**: There is a 5% chance of a disease outbreak, which reduces the population by 30%.

At the end of the simulation, a graph is displayed showing the population growth over time.

---

## Example
### Input:
```
Enter the initial population: 100
Enter the growth rate (between 0 and 1): 0.1
Enter the carrying capacity: 1000
Enter the number of years to simulate: 10
```

### Output:
```
Year 1: Population = 110.00
Year 2: Population = 121.00
Year 3: Population = 133.10
Year 4: Population = 146.41
Year 5: Population = 161.05
Year 6: Population = 177.16
Year 7: Population = 194.87
Year 8: Population = 214.36
Year 9: Population = 235.80
Year 10: Population = 259.38
```

A graph will also be displayed showing the population growth over the 10 years.

---

## Dependencies
The program requires the following Python libraries:
- `matplotlib`: For plotting the population growth graph.
- `random`: For simulating random events like disease outbreaks.

You can install the dependencies using:
```bash
pip install matplotlib
```

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.