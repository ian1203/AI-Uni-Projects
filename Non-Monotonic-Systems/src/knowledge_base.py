class KnowledgeBase:
    def __init__(self):
        """
        Initialize the knowledge base with empty lists for defeasible and default rules.
        """
        self.defeasible_rules = []
        self.default_rules = []
        self.facts = {}

    def add_defeasible_rule(self, rule):
        """
        Add a defeasible rule to the knowledge base.

        :param rule: An instance of DefeasibleRule.
        """
        self.defeasible_rules.append(rule)

    def add_default_rule(self, rule):
        """
        Add a default rule to the knowledge base.

        :param rule: An instance of DefaultRule.
        """
        self.default_rules.append(rule)

    def add_fact(self, key, value):
        """
        Add a fact to the knowledge base.

        :param key: The key for the fact (e.g., "client_id").
        :param value: The value of the fact (e.g., 123).
        """
        self.facts[key] = value

    def get_fact(self, key):
        """
        Retrieve a fact from the knowledge base.

        :param key: The key for the fact.
        :return: The value of the fact, or None if the fact does not exist.
        """
        return self.facts.get(key)

    def match_facts(self, conditions):
        """
        Check if the given conditions match the facts in the knowledge base.

        :param conditions: A dictionary of conditions to match.
        :return: True if all conditions match, False otherwise.
        """
        for key, value in conditions.items():
            if self.get_fact(key) != value:
                return False
        return True


class DefeasibleRule:
    def __init__(self, conditions, conclusion, conflict_resolution_strategy=None):
        """
        Initialize a defeasible rule.

        :param conditions: A dictionary of conditions that must be met for the rule to apply.
        :param conclusion: A dictionary representing the conclusion if the rule applies.
        :param conflict_resolution_strategy: A string indicating how to resolve conflicts (e.g., "override").
        """
        self.conditions = conditions
        self.conclusion = conclusion
        self.conflict_resolution_strategy = conflict_resolution_strategy


class DefaultRule:
    def __init__(self, premise, conclusion):
        """
        Initialize a default rule.

        :param premise: A dictionary of conditions that must be consistent for the rule to apply.
        :param conclusion: A dictionary representing the default conclusion.
        """
        self.premise = premise
        self.conclusion = conclusion