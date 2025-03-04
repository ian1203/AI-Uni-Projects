class InferenceEngine:
    def __init__(self, knowledge_base):
        """
        Initialize the inference engine with a knowledge base.

        :param knowledge_base: An instance of the KnowledgeBase class containing rules and facts.
        """
        self.knowledge_base = knowledge_base

    def infer(self, query):
        """
        Perform non-monotonic reasoning using both defeasible and default logic.

        :param query: A dictionary representing the query.
        :return: A dictionary containing the inferred conclusions.
        """
        conclusions = {}

        defeasible_conclusions = self._apply_defeasible_rules(query)
        print("Defeasible Conclusions:", defeasible_conclusions)
        conclusions.update(defeasible_conclusions)

        default_conclusions = self._apply_default_rules(query)
        print("Default Conclusions:", default_conclusions)
        conclusions.update(default_conclusions)

        final_conclusions = self._resolve_conflicts(query, conclusions)
        print("Final Conclusions:", final_conclusions)

        return final_conclusions

    def _apply_defeasible_rules(self, query):
        """
        Apply defeasible rules to infer tentative conclusions.

        :param query: The query to process.
        :return: A dictionary of tentative conclusions.
        """
        tentative_conclusions = {}

        for rule in self.knowledge_base.defeasible_rules:
            if self._matches_conditions(rule, query):
                print(f"Applying defeasible rule: {rule.conditions} -> {rule.conclusion}")  # Debugging
                tentative_conclusions.update(rule.conclusion)

        return tentative_conclusions

    def _apply_default_rules(self, query):
        """
        Apply default rules to make assumptions in the absence of complete information.

        :param query: The query to process.
        :return: A dictionary of default conclusions.
        """
        default_conclusions = {}

        for rule in self.knowledge_base.default_rules:
            if self._is_applicable(rule, query):
                print(f"Applying default rule: {rule.premise} -> {rule.conclusion}")  # Debugging
                default_conclusions.update(rule.conclusion)

        return default_conclusions

    @staticmethod
    def _is_applicable(rule, query):
        """
        Check if a default rule is applicable.

        :param rule: A default rule from the knowledge base.
        :param query: The query to check against.
        :return: True if the rule is applicable, False otherwise.
        """

        for key, value in rule.premise.items():
            if query.get(key) != value:
                return False
        return True

    @staticmethod
    def _matches_conditions(rule, query):
        """
        Check if the rule conditions match the query.

        :param rule: A rule from the knowledge base.
        :param query: The query to check against.
        :return: True if the conditions match, False otherwise.
        """
        for key, value in rule.conditions.items():
            if key not in query:
                return False
            if isinstance(value, str) and value.startswith((">", "<", ">=", "<=")):
                try:
                    op = value[:2] if value[1] in ("=",) else value[0]
                    compare_value = float(value[len(op):])
                    query_value = float(query[key])
                    if op == ">" and not (query_value > compare_value):
                        return False
                    elif op == "<" and not (query_value < compare_value):
                        return False
                    elif op == ">=" and not (query_value >= compare_value):
                        return False
                    elif op == "<=" and not (query_value <= compare_value):
                        return False
                except (ValueError, TypeError):
                    return False
            elif query[key] != value:
                return False
        return True

    def _resolve_conflicts(self, query, conclusions):
        """
        Resolve conflicts between conclusions from defeasible and default rules.

        :param query: The query being processed.
        :param conclusions: A dictionary of conclusions.
        :return: A dictionary of final conclusions after resolving conflicts.
        """
        final_conclusions = conclusions.copy()

        most_specific_rule = None
        for rule in self.knowledge_base.defeasible_rules:
            if self._matches_conditions(rule, query):
                if most_specific_rule is None or self._is_more_specific(rule, most_specific_rule):
                    most_specific_rule = rule

        if most_specific_rule:
            print(
                f"Applying most specific rule: {most_specific_rule.conditions} -> {most_specific_rule.conclusion}")  # Debugging
            final_conclusions.update(most_specific_rule.conclusion)

        for rule in self.knowledge_base.defeasible_rules:
            if rule.conflict_resolution_strategy == "override" and self._matches_conditions(rule, query):
                if rule == most_specific_rule:
                    for key in rule.conclusion:
                        if key in final_conclusions:
                            print(
                                f"Overriding conclusion for key '{key}' with defeasible rule: {rule.conclusion}")  # Debugging
                            final_conclusions[key] = rule.conclusion[key]

        return final_conclusions

    @staticmethod
    def _is_more_specific(rule1, rule2):
        """
        Check if rule1 is more specific than rule2.

        :param rule1: A rule from the knowledge base.
        :param rule2: Another rule from the knowledge base.
        :return: True if rule1 is more specific, False otherwise.
        """
        return len(rule1.conditions) > len(rule2.conditions)