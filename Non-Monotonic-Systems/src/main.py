from knowledge_base import KnowledgeBase, DefeasibleRule, DefaultRule
from inference_engine import InferenceEngine


def initialize_knowledge_base():
    """
    Initialize the knowledge base with all the rules.

    :return: An instance of KnowledgeBase.
    """
    knowledge_base = KnowledgeBase()

    knowledge_base.add_defeasible_rule(DefeasibleRule(
        conditions={"goal": "real_estate", "income_level": "high"},
        conclusion={"recommendation": "invest in rental properties"},
        conflict_resolution_strategy="override"
    ))

    knowledge_base.add_defeasible_rule(DefeasibleRule(
        conditions={"goal": "emergency_fund", "time_horizon": "short-term"},
        conclusion={"recommendation": "invest in a money market account"}
    ))

    knowledge_base.add_defeasible_rule(DefeasibleRule(
        conditions={"goal": "tax_advantaged", "income_level": "medium"},
        conclusion={"recommendation": "contribute to a Roth IRA"}
    ))

    knowledge_base.add_defeasible_rule(DefeasibleRule(
        conditions={"goal": "diversification", "risk_tolerance": "moderate"},
        conclusion={"recommendation": "invest in a mix of stocks and bonds"}
    ))

    knowledge_base.add_defeasible_rule(DefeasibleRule(
        conditions={"goal": "retirement", "age": ">50", "income_level": "high"},
        conclusion={"recommendation": "maximize 401(k) contributions"},
        conflict_resolution_strategy="override"
    ))

    knowledge_base.add_defeasible_rule(DefeasibleRule(
        conditions={"goal": "education", "age": "<18", "income_level": "low"},
        conclusion={"recommendation": "apply for scholarships and grants"}
    ))

    knowledge_base.add_defeasible_rule(DefeasibleRule(
        conditions={"goal": "retirement", "age": ">60"},
        conclusion={"recommendation": "invest in bonds"},
        conflict_resolution_strategy="override"
    ))

    knowledge_base.add_defeasible_rule(DefeasibleRule(
        conditions={"goal": "growth", "risk_tolerance": "high"},
        conclusion={"recommendation": "invest in stocks"}
    ))

    knowledge_base.add_defeasible_rule(DefeasibleRule(
        conditions={"goal": "education", "age": ">=18", "age": "<30"},
        conclusion={"recommendation": "invest in a 529 plan"}
    ))

    knowledge_base.add_defeasible_rule(DefeasibleRule(
        conditions={"goal": "savings", "risk_tolerance": "low"},
        conclusion={"recommendation": "invest in a high-yield savings account"}
    ))

    knowledge_base.add_defeasible_rule(DefeasibleRule(
        conditions={"market_conditions": "bearish"},
        conclusion={"recommendation": "invest in gold"}
    ))

    knowledge_base.add_defeasible_rule(DefeasibleRule(
        conditions={"market_conditions": "volatile", "risk_tolerance": "moderate"},
        conclusion={"recommendation": "invest in index funds"}
    ))

    knowledge_base.add_defeasible_rule(DefeasibleRule(
        conditions={"goal": "tax_planning", "income_level": "high"},
        conclusion={"recommendation": "consult a tax advisor"},
        conflict_resolution_strategy="override"
    ))

    knowledge_base.add_defeasible_rule(DefeasibleRule(
        conditions={"goal": "estate_planning", "age": ">60"},
        conclusion={"recommendation": "create a will and trust"}
    ))

    knowledge_base.add_default_rule(DefaultRule(
        premise={"goal": "tax_planning"},
        conclusion={"recommendation": "maximize tax-deferred accounts"}
    ))

    knowledge_base.add_default_rule(DefaultRule(
        premise={"goal": "estate_planning"},
        conclusion={"recommendation": "consider life insurance"}
    ))

    knowledge_base.add_default_rule(DefaultRule(
        premise={"risk_tolerance": "moderate"},
        conclusion={"recommendation": "invest in index funds"}
    ))

    knowledge_base.add_default_rule(DefaultRule(
        premise={"goal": "retirement"},
        conclusion={"recommendation": "invest in a diversified portfolio"}
    ))

    knowledge_base.add_default_rule(DefaultRule(
        premise={"goal": "growth"},
        conclusion={"recommendation": "invest in growth stocks"}
    ))

    knowledge_base.add_default_rule(DefaultRule(
        premise={"goal": "savings"},
        conclusion={"recommendation": "invest in a high-yield savings account"}
    ))

    knowledge_base.add_default_rule(DefaultRule(
        premise={"market_conditions": "bullish"},
        conclusion={"recommendation": "consider growth-oriented investments"}
    ))

    knowledge_base.add_default_rule(DefaultRule(
        premise={"risk_tolerance": "low"},
        conclusion={"recommendation": "invest in government bonds"}
    ))

    knowledge_base.add_default_rule(DefaultRule(
        premise={"income_level": "high"},
        conclusion={"recommendation": "consult a financial advisor"}
    ))

    knowledge_base.add_default_rule(DefaultRule(
        premise={"time_horizon": "long-term"},
        conclusion={"recommendation": "invest in index funds"}
    ))

    knowledge_base.add_default_rule(DefaultRule(
        premise={"goal": "retirement", "age": ">60"},
        conclusion={"recommendation": "consider annuities"}
    ))

    return knowledge_base


def get_user_input():
    """
    Prompt the user for input and return a dictionary representing the query.

    :return: A dictionary containing the user's input.
    """
    print("\nWelcome to Ian's Financial Advisory System!")
    print("Please provide the following details to get personalized recommendations.\n")

    query = dict()
    query["goal"] = input(
        "What is your financial goal? (e.g., retirement, growth, savings, education, real_estate, tax_planning, estate_planning): ").strip().lower()
    query["age"] = int(input("What is your age? (e.g., 25, 65): "))
    query["risk_tolerance"] = input("What is your risk tolerance? (e.g., low, moderate, high): ").strip().lower()
    query["income_level"] = input("What is your income level? (e.g., low, medium, high): ").strip().lower()
    query["time_horizon"] = input(
        "What is your investment time horizon? (e.g., short-term, medium-term, long-term): ").strip().lower()
    query["market_conditions"] = input(
        "What are the current market conditions? (e.g., bullish, bearish, volatile): ").strip().lower()

    return query


def display_recommendations(conclusions):
    """
    Display the recommendations to the user.

    :param conclusions: A dictionary containing the inferred conclusions.
    """
    print("\n--- Recommendations ---")
    if conclusions:
        for key, value in conclusions.items():
            print(f"{key}: {value}")
    else:
        print("No recommendations found for your input.")
    print("-----------------------\n")


def main():
    knowledge_base = initialize_knowledge_base()
    inference_engine = InferenceEngine(knowledge_base)

    while True:
        query = get_user_input()

        conclusions = inference_engine.infer(query)

        display_recommendations(conclusions)

        continue_choice = input("Do you want to get another recommendation? (yes/no): ").strip().lower()
        if continue_choice != "yes":
            print("Thank you for using Ian's Financial Advisory System. Goodbye!")
            break


if __name__ == "__main__":
    main()