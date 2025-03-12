class LegalSystem:
    """
    Knowledge-based system using a rule-based approach with propositional logic.

    I'm using a simple rule-based system with propositional logic for this problem
    because it allows for direct representation of evidence as facts and logical
    relationships between them. The system can easily be updated with new evidence
    during an appeal process.
    """

    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        """Add a fact to the knowledge base"""
        self.facts.add(fact)

    def add_rule(self, condition, conclusion):
        """Add a rule to the knowledge base"""
        # Condition can be a single fact or a list of facts that must all be true
        self.rules.append((condition, conclusion))

    def evaluate(self):
        """Apply rules to facts until no new facts can be derived"""
        new_fact_added = True

        while new_fact_added:
            new_fact_added = False

            for condition, conclusion in self.rules:
                # If condition is a list, all facts in the list must be in self.facts
                if isinstance(condition, list):
                    if all(fact in self.facts for fact in condition):
                        if conclusion not in self.facts:
                            self.facts.add(conclusion)
                            new_fact_added = True
                # If condition is a single fact
                elif condition in self.facts:
                    if conclusion not in self.facts:
                        self.facts.add(conclusion)
                        new_fact_added = True

    def check_fact(self, fact):
        """Check if a fact is in the knowledge base"""
        return fact in self.facts

    def get_verdict(self):
        """Return the verdict based on the current facts"""
        if "guilty" in self.facts and "innocent" not in self.facts:
            return "Guilty"
        elif "innocent" in self.facts:
            return "Innocent"
        else:
            return "Insufficient evidence"

    def reset(self):
        """Reset the knowledge base for a new case"""
        self.facts = set()
        self.rules = []


# Function to handle a legal case
def process_case(case_name, initial_facts, rules, appeal_facts=None):
    print(f"\n=== {case_name} ===")

    # Initial trial
    print("Initial Trial:")
    legal_system = LegalSystem()

    # Add facts
    for fact in initial_facts:
        legal_system.add_fact(fact)

    # Add rules
    for condition, conclusion in rules:
        legal_system.add_rule(condition, conclusion)

    # Evaluate
    legal_system.evaluate()

    # Print initial verdict
    initial_verdict = legal_system.get_verdict()
    print(f"Initial verdict: {initial_verdict}")

    # If appeal facts are provided, process the appeal
    if appeal_facts:
        print("\nAppeal:")

        # Add new facts from appeal
        for fact in appeal_facts:
            legal_system.add_fact(fact)

        # Re-evaluate
        legal_system.evaluate()

        # Print updated verdict
        appeal_verdict = legal_system.get_verdict()
        print(f"Appeal verdict: {appeal_verdict}")

    return legal_system


# Case 1: The Mansion Murder
def case_mansion_murder():
    case_name = "Case 1: The Mansion Murder"

    initial_facts = [
        "near_crime_scene",
        "fingerprints_on_knife",
        "had_debt_with_victim"
    ]

    rules = [
        (["near_crime_scene", "fingerprints_on_knife", "had_debt_with_victim"], "guilty"),
        ("in_another_room", "not_near_crime_scene"),
        ("not_near_crime_scene", "alibi"),
        ("fingerprints_do_not_match", "not_fingerprints_on_knife"),
        (["alibi", "not_fingerprints_on_knife"], "innocent")
    ]

    appeal_facts = [
        "in_another_room",
        "fingerprints_do_not_match"
    ]

    return process_case(case_name, initial_facts, rules, appeal_facts)


# Case 2: The Bank Heist
def case_bank_heist():
    case_name = "Case 2: The Bank Heist"

    initial_facts = [
        "recently_fired",
        "had_access_to_blueprints",
        "witness_saw_near_bank",
        "stolen_money_found"
    ]

    rules = [
        (["recently_fired", "had_access_to_blueprints", "witness_saw_near_bank", "stolen_money_found"], "guilty"),
        ("witness_mistaken", "not_witness_saw_near_bank"),
        ("money_from_inheritance", "not_stolen_money_found"),
        (["not_witness_saw_near_bank", "not_stolen_money_found"], "innocent")
    ]

    appeal_facts = [
        "witness_mistaken",
        "money_from_inheritance"
    ]

    return process_case(case_name, initial_facts, rules, appeal_facts)


# Case 3: The Traffic Accident
def case_traffic_accident():
    case_name = "Case 3: The Traffic Accident"

    initial_facts = [
        "was_speeding",
        "ran_red_light",
        "had_alcohol_in_blood"
    ]

    rules = [
        (["was_speeding", "ran_red_light", "had_alcohol_in_blood"], "guilty"),
        ("light_was_green", "not_ran_red_light"),
        ("alcohol_within_legal_limit", "not_had_alcohol_in_blood"),
        (["not_ran_red_light", "not_had_alcohol_in_blood"], "innocent")
    ]

    appeal_facts = [
        "light_was_green",
        "alcohol_within_legal_limit"
    ]

    return process_case(case_name, initial_facts, rules, appeal_facts)


# Run all cases
if __name__ == "__main__":
    case_mansion_murder()
    case_bank_heist()
    case_traffic_accident()