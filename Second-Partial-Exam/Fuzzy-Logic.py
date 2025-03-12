import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


class SmartHomeLighting:
    def __init__(self):
        # Define input variables
        self.time = ctrl.Antecedent(np.arange(0, 24, 1), 'time')
        self.occupancy = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'occupancy')

        # Define output variable
        self.light_intensity = ctrl.Consequent(np.arange(0, 101, 1), 'light_intensity')

        # Define membership functions for time of day
        self.time['morning'] = fuzz.trapmf(self.time.universe, [5, 7, 11, 13])  # 6 AM - 12 PM
        self.time['afternoon'] = fuzz.trapmf(self.time.universe, [11, 13, 17, 19])  # 12 PM - 6 PM
        self.time['evening'] = fuzz.trapmf(self.time.universe, [17, 19, 21, 23])  # 6 PM - 9 PM
        self.time['night'] = fuzz.trapmf(self.time.universe, [21, 23, 24, 24]) + fuzz.trapmf(self.time.universe, [0, 0, 5, 7])
  # 9 PM - 6 AM

        # Define membership functions for occupancy
        self.occupancy['unoccupied'] = fuzz.trimf(self.occupancy.universe, [0, 0, 0.5])
        self.occupancy['occupied'] = fuzz.trimf(self.occupancy.universe, [0.5, 1, 1])

        # Define membership functions for light intensity
        self.light_intensity['off'] = fuzz.trimf(self.light_intensity.universe, [0, 0, 25])
        self.light_intensity['low'] = fuzz.trimf(self.light_intensity.universe, [0, 25, 50])
        self.light_intensity['medium'] = fuzz.trimf(self.light_intensity.universe, [25, 50, 75])
        self.light_intensity['high'] = fuzz.trimf(self.light_intensity.universe, [50, 100, 100])

        # Define rules
        self.rules = [
            # Morning rules
            ctrl.Rule(self.time['morning'] & self.occupancy['occupied'], self.light_intensity['medium']),
            ctrl.Rule(self.time['morning'] & self.occupancy['unoccupied'], self.light_intensity['off']),

            # Afternoon rules
            ctrl.Rule(self.time['afternoon'] & self.occupancy['occupied'], self.light_intensity['low']),
            ctrl.Rule(self.time['afternoon'] & self.occupancy['unoccupied'], self.light_intensity['off']),

            # Evening rules
            ctrl.Rule(self.time['evening'] & self.occupancy['occupied'], self.light_intensity['high']),
            ctrl.Rule(self.time['evening'] & self.occupancy['unoccupied'], self.light_intensity['low']),

            # Night rules
            ctrl.Rule(self.time['night'] & self.occupancy['occupied'], self.light_intensity['low']),
            ctrl.Rule(self.time['night'] & self.occupancy['unoccupied'], self.light_intensity['off'])
        ]

        # Create and simulate control system
        self.lighting_ctrl = ctrl.ControlSystem(self.rules)
        self.lighting_simulator = ctrl.ControlSystemSimulation(self.lighting_ctrl)

    def get_light_level(self, time_of_day, is_occupied):
        """
        Get the light level based on time of day and occupancy

        Args:
            time_of_day: int, hour of the day (0-23)
            is_occupied: bool, whether the room is occupied

        Returns:
            float: recommended light intensity (0-100)
        """
        # Convert boolean to binary for occupancy
        occupancy_value = 1 if is_occupied else 0

        # Set inputs
        self.lighting_simulator.input['time'] = time_of_day
        self.lighting_simulator.input['occupancy'] = occupancy_value

        try:
            # Compute result
            self.lighting_simulator.compute()
            return self.lighting_simulator.output['light_intensity']
        except:
            # Handle possible errors (e.g., rules contradiction)
            print("Error in fuzzy computation. Using default values.")
            if is_occupied:
                return 50  # Default to medium if occupied
            else:
                return 0  # Default to off if unoccupied

    def visualize_membership_functions(self):
        """Visualize the membership functions"""
        # Time of day
        self.time.view()

        # Occupancy
        self.occupancy.view()

        # Light intensity
        self.light_intensity.view()

        plt.show()


# Example usage
def main():
    # Create smart home lighting system
    lighting_system = SmartHomeLighting()

    # Test cases from the problem description
    test_cases = [
        (7, True),  # 7 AM, Occupied
        (13, False),  # 1 PM, Unoccupied
        (19, True),  # 7 PM, Occupied
        (23, False)  # 11 PM, Unoccupied
    ]

    print("\nSmart Home Lighting Control System")
    print("====================================")

    # Process each test case
    for time_of_day, is_occupied in test_cases:
        # Get time period name
        if 6 <= time_of_day < 12:
            period = "Morning"
        elif 12 <= time_of_day < 18:
            period = "Afternoon"
        elif 18 <= time_of_day < 21:
            period = "Evening"
        else:
            period = "Night"

        # Get occupancy status text
        occupancy_status = "Occupied" if is_occupied else "Unoccupied"

        # Get light intensity
        intensity = lighting_system.get_light_level(time_of_day, is_occupied)

        # Get intensity category
        if intensity < 10:
            category = "Off"
        elif intensity < 35:
            category = "Low"
        elif intensity < 65:
            category = "Medium"
        else:
            category = "High"

        # Print result
        print(f"\nTime: {time_of_day}:00 ({period})")
        print(f"Room status: {occupancy_status}")
        print(f"Light intensity: {intensity:.1f}% ({category})")

    # Uncomment to visualize membership functions
    # lighting_system.visualize_membership_functions()


if __name__ == "__main__":
    main()