# Financial Advisory System

This project is a **non-monotonic reasoning system** designed to provide personalized financial recommendations based on user inputs such as financial goals, age, risk tolerance, income level, time horizon, and market conditions. It uses a combination of **defeasible logic** and **default logic** to handle complex and changing financial scenarios.

---

## Table of Contents

1. [How It Works](#how-it-works)
2. [Expected Inputs](#expected-inputs)
3. [Key Terms Explained](#key-terms-explained)
   - Bearish
   - Bullish
   - Volatile
4. [Technologies Implemented](#technologies-implemented)
5. [Getting Started](#getting-started)
   - Installation
   - Running the System
6. [Example Usage](#example-usage)
7. [License](#license)

---

## How It Works

The system uses a **knowledge base** of rules to infer financial recommendations. These rules are divided into two types:

1. **Defeasible Rules**:
   - These are rules that can be overridden by more specific or higher-priority rules.
   - Example: If the user's goal is `retirement` and their age is `>60`, the system recommends `invest in bonds`.

2. **Default Rules**:
   - These are general rules that apply when no specific defeasible rule matches the user's input.
   - Example: If the user's risk tolerance is `moderate`, the system recommends `invest in index funds`.

The system evaluates the user's input against these rules and provides the most appropriate recommendation.

---

## Expected Inputs

The system prompts the user for the following inputs:

1. **Financial Goal**:
   - Examples: `retirement`, `growth`, `savings`, `education`, `real_estate`, `tax_planning`, `estate_planning`.

2. **Age**:
   - The user's age in years (e.g., `25`, `65`).

3. **Risk Tolerance**:
   - The user's comfort level with risk. Options: `low`, `moderate`, `high`.

4. **Income Level**:
   - The user's income bracket. Options: `low`, `medium`, `high`.

5. **Time Horizon**:
   - The duration for which the user plans to invest. Options: `short-term`, `medium-term`, `long-term`.

6. **Market Conditions**:
   - The current state of the financial market. Options: `bullish`, `bearish`, `volatile`.

---

## Key Terms Explained

### Bearish
- A **bearish** market is one where prices are falling or expected to fall.
- Recommendation: The system may suggest safer investments like bonds or gold.

### Bullish
- A **bullish** market is one where prices are rising or expected to rise.
- Recommendation: The system may suggest growth-oriented investments like stocks or index funds.

### Volatile
- A **volatile** market is one where prices fluctuate significantly in a short period.
- Recommendation: The system may suggest diversified investments to mitigate risk.

---

## Technologies Implemented

1. **Python**:
   - The core logic of the system is implemented in Python.

2. **Defeasible Logic**:
   - Used to handle rules that can be overridden by more specific rules.

3. **Default Logic**:
   - Used to provide general recommendations when no specific rule applies.

4. **Knowledge Base**:
   - A collection of defeasible and default rules stored in the system.

5. **Inference Engine**:
   - The component that applies the rules to user inputs and generates recommendations.

---

## Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Non-Monotonic-Systems.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Non-Monotonic-Systems
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the System

1. Run the `main.py` file:
   ```bash
   python main.py
   ```

2. Follow the prompts to input your financial details and receive recommendations.

---

## Example Usage

```
Welcome to Ian's Financial Advisory System!
Please provide the following details to get personalized recommendations.

What is your financial goal? (e.g., retirement, growth, savings, education, real_estate, tax_planning, estate_planning): retirement
What is your age? (e.g., 25, 65): 65
What is your risk tolerance? (e.g., low, moderate, high): moderate
What is your income level? (e.g., low, medium, high): high
What is your investment time horizon? (e.g., short-term, medium-term, long-term): long-term
What are the current market conditions? (e.g., bullish, bearish, volatile): bullish

--- Recommendations ---
recommendation: maximize 401(k) contributions
-----------------------

Do you want to get another recommendation? (yes/no): no
Thank you for using Ian's Financial Advisory System. Goodbye!
```

---



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
