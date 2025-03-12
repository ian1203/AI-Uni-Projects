# Artificial Intelligence Exam Exercises

This directory contains implementations of various AI algorithms and techniques as part of the second partial exam of the Artificial Intelligence course. The directory includes gradient descent optimization, a knowledge-based legal reasoning system, emotion detection using Bayesian techniques, and a fuzzy logic system for smart home lighting control.

## Table of Contents
- [Exercise 1: Gradient Descent Optimization](#exercise-1-gradient-descent-optimization)
- [Exercise 2: Knowledge-Based Legal Reasoning System](#exercise-2-knowledge-based-legal-reasoning-system)
- [Exercise 3: Emotion Detection using Bayesian Techniques](#exercise-3-emotion-detection-using-bayesian-techniques)
- [Exercise 4: Fuzzy Logic for Smart Home Lighting Control](#exercise-4-fuzzy-logic-for-smart-home-lighting-control)
- [Installation Requirements](#installation-requirements)
- [Project Structure](#project-structure)
- [Possible Errors in every exercise](#Errors-Discussion)

## Exercise 1: Gradient Descent Optimization

### Description
This exercise implements the gradient descent algorithm to find the minimum of the function f(x) = x² + 4x + 5.

### Implementation
The `gradient_descent.py` file contains:
- Function `f(x)` that computes the value of x² + 4x + 5
- Function `df(x)` that computes the derivative: 2x + 4
- Function `gradient_descent(x0, alpha, iterations)` that implements the algorithm:
  - Takes an initial value x₀, learning rate α, and number of iterations
  - Updates x in each iteration using the formula: x = x - α * df(x)
  - Tracks all x values and corresponding function values
  - Prints the progress of each iteration

The implementation uses:
- Initial value x₀ = 1
- Learning rate α = 0.1
- 20 iterations

### Expected Output
When running `gradient_descent.py`, you'll see:
1. Console output showing the progress of each iteration:
   ```
   Iteration 1: x = 0.800000, f(x) = 8.240000
   Iteration 2: x = 0.640000, f(x) = 7.409600
   ...
   Iteration 20: x = -1.985599, f(x) = 1.000029
   ```

2. A visualization saved as `gradient_descent.png` showing:
   - The function f(x) = x² + 4x + 5 as a blue line
   - Red dots marking each step of the gradient descent
   - Red dashed line connecting the steps

3. Final results showing:
   - The computed minimum after 20 iterations (x ≈ -1.986, f(x) ≈ 1.00003)
   - The analytical minimum (x = -2, f(x) = 1)

The algorithm converges very close to the true minimum of the function (x = -2), demonstrating the effectiveness of gradient descent for finding function minima.

### Usage
```
python Gradient-Descent.py
```

## Exercise 2: Knowledge-Based Legal Reasoning System

### Description
A knowledge-based system that uses propositional logic and rule-based reasoning to determine whether defendants are guilty or innocent in three different legal cases. The system also handles appeals with new evidence.

### Implementation
The `legal_cases.py` file implements:

- `LegalSystem` class that uses propositional logic to represent a rule-based system:
  - `add_fact(fact)`: Adds a fact to the knowledge base
  - `add_rule(condition, conclusion)`: Adds a rule to the knowledge base
  - `evaluate()`: Applies rules to facts until no new facts can be derived
  - `get_verdict()`: Returns "Guilty", "Innocent", or "Insufficient evidence" based on current facts
  - `reset()`: Clears the knowledge base for a new case

- `process_case(case_name, initial_facts, rules, appeal_facts)`: Function to run a case through the system:
  - Sets up initial facts and rules for a trial
  - Evaluates and returns an initial verdict
  - Adds new appeal facts if provided
  - Re-evaluates and returns an updated verdict

- Three specific case implementations:
  1. `case_mansion_murder()`: The Mansion Murder case
  2. `case_bank_heist()`: The Bank Heist case
  3. `case_traffic_accident()`: The Traffic Accident case

Each case defines:
- Initial facts (evidence against the defendant)
- Rules for determining guilt or innocence
- New facts presented during appeal

### Expected Output
When running `Legal-Cases.py`, you'll see:

```
=== Case 1: The Mansion Murder ===
Initial Trial:
Initial verdict: Guilty

Appeal:
Appeal verdict: Innocent

=== Case 2: The Bank Heist ===
Initial Trial:
Initial verdict: Guilty

Appeal:
Appeal verdict: Innocent

=== Case 3: The Traffic Accident ===
Initial Trial:
Initial verdict: Guilty

Appeal:
Appeal verdict: Innocent
```

For each case:
1. The system first concludes "Guilty" based on the initial evidence
2. After new evidence is presented in the appeal, the system updates to "Innocent"

The program demonstrates how logical reasoning can be applied to legal cases and how new evidence can change the conclusion.

### Usage
```
python Legal-Cases.py
```

## Exercise 3: Emotion Detection using Bayesian Techniques

### Description
A text emotion classification system using Bayes' Theorem to detect emotions (happy, sad, angry) in text messages. The system analyzes input text and calculates the probability of each emotion based on the words used.

### Implementation
The `Emotion-Detection.py` file implements:

- `EmotionDetector` class that uses Bayesian probability to classify emotions:
  - Initialized with prior probabilities `P(E)` for each emotion (happy: 0.4, sad: 0.3, angry: 0.3)
  - Contains conditional probabilities `P(W|E)` for common emotion-related words
  - Includes a smoothing value to handle unknown words

- Key methods:
  - `preprocess_text(text)`: Cleans and tokenizes input text
  - `calculate_probability(message)`: Calculates posterior probabilities `P(E|W)` for each emotion
  - `detect_emotion(message)`: Returns the most probable emotion and all probabilities

- Interactive `main()` function that:
  - Takes user input text messages
  - Displays the detected emotion and probability distribution
  - Continues until the user types 'quit'

The implementation uses Bayes' Theorem: `P(E|W) = P(W|E) * P(E) / P(W)` where:
- `P(E|W)` is the probability of emotion E given words W
- `P(W|E)` is the probability of words W given emotion E
- `P(E)` is the prior probability of emotion E
- `P(W)` is the probability of words W

### Expected Output
When running `emotion_detection.py`, you'll see an interactive prompt:

```
Enter a message (or 'quit' to exit): I feel so happy today!

Detected emotion: HAPPY

Probabilities:
  happy: 0.9512 (95.12%)
  sad: 0.0241 (2.41%)
  angry: 0.0247 (2.47%)

Enter a message (or 'quit' to exit): This is making me frustrated and angry

Detected emotion: ANGRY

Probabilities:
  happy: 0.0125 (1.25%)
  sad: 0.0684 (6.84%)
  angry: 0.9191 (91.91%)
```

The system:
1. Correctly identifies the dominant emotion in text messages
2. Provides probability percentages for all emotions
3. Handles unknown words through smoothing

### Usage
```
python Emotion-Detection.py
```

# Exercise 4: Fuzzy Logic for Smart Home Lighting Control

## Description
This exercise implements a fuzzy logic system to control smart home lighting based on the time of day and room occupancy. The system determines the appropriate lighting intensity using fuzzy rules that account for morning, afternoon, evening, and night conditions, as well as occupancy levels.

## Implementation
The `fuzzy_lighting.py` file contains:

### Fuzzy variables:
- **time (input):** Categorized into morning, afternoon, evening, and night.  
- **occupancy (input):** Ranges from 0 (unoccupied) to 1 (fully occupied).  
- **light_intensity (output):** Determines the brightness level from 0% to 100%.  

### Membership functions:
Define the degree to which an input belongs to a fuzzy set.

### Fuzzy rules:
- Higher lighting intensity when the room is occupied during the evening.  
- Lower intensity during the afternoon if the room is unoccupied.  
- Lights turn off at night when there’s no occupancy.  

### Control system:
Uses fuzzy inference to determine the appropriate lighting level.

## Expected Output
The system dynamically adjusts lighting intensity based on the given inputs. Example outputs include:

- **Morning, occupied** → Medium lighting  
- **Afternoon, unoccupied** → Low lighting  
- **Evening, occupied** → High lighting  
- **Night, unoccupied** → Lights off  

## Usage
```sh
python Fuzzy-Logic.py
```
## Installation Requirements
All required packages are listed in the `requirements.txt` file. Install them using:

```
pip install -r requirements.txt
```

## Project Structure
```
├── Gradient-Descent.py
├── Legal-Cases.py
├── Emotion-Detection.py
├── Fuzzy-Logic.py
├── requirements.txt
├── README.md
```

## Errors Discussion

# Potential Errors in Gradient Descent Optimization
One potential issue in the gradient descent implementation is the choice of the learning rate (α). If the learning rate is too high, the algorithm may overshoot the minimum, leading to divergence rather than convergence. If it's too low, the algorithm may take too long to converge or get stuck in a local minimum. Additionally, failing to implement a stopping condition based on the difference between consecutive function values could lead to unnecessary iterations.

**Possible Fix:** Implement a stopping condition based on the gradient's magnitude to terminate early when the updates are negligible.

# Potential Errors in Knowledge-Based Legal Reasoning System
A potential issue with the rule-based reasoning system is handling contradictory facts or missing evidence. If a case lacks sufficient facts, the system might incorrectly default to an incorrect verdict rather than returning “Insufficient Evidence.” Furthermore, if contradictory facts are present, the system might enter an infinite loop while trying to resolve them.

**Possible Fix:** Implement a mechanism to detect contradictions and return an “Undetermined” or “Insufficient Evidence” verdict instead of forcing a binary decision.

# Potential Errors in Emotion Detection using Bayesian Techniques
A possible error in the emotion detection system arises when encountering unknown words not present in the training data. If a message contains words with no associated probabilities, the Bayesian classifier might return incorrect probabilities or even fail to classify the emotion correctly. Another issue is the skewed prior probability—if the dataset has significantly more "happy" words than "sad" or "angry," the model may be biased toward predicting "happy" more often.

**Possible Fix:** Apply Laplace smoothing to handle unseen words and ensure the classifier generalizes better to new inputs. Additionally, balance the training data across emotions to avoid biased predictions.

# Potential Errors in Fuzzy Logic for Smart Home Lighting Control
A potential issue in the fuzzy logic system is overlapping or poorly defined membership functions. If the membership functions are not properly tuned, the system may assign inconsistent or incorrect intensity values for certain conditions. Additionally, the fuzzy inference system might not react properly to rapid changes in occupancy or time, leading to a lag in lighting adjustments.

**Possible Fix:** Fine-tune the membership functions through data-driven calibration and implement a smoothing mechanism to prevent erratic lighting changes due to sudden variations in input values.