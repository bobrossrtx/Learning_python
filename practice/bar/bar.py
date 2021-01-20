import random
import json
import os

bar_name_title = random.choice(["teddies_bar", "the_queens_inn", "ace_bounce"])

person_drinks = random.randint(1, 15)
person_age = random.randint(15, 30)

bar_rule_1 = "Max drinks: "
bar_rule_2 = "Min Age: "

def people(rules_data):

    for bar_name_data in rules_data["bars"]:
        for bar_name_data_objects in bar_name_data[bar_name_title]:
            print(bar_rule_1, bar_name_data_objects["max_drinks"])
            print(bar_rule_2, bar_name_data_objects["min_age"])

            print("\n")

            min_age = bar_name_data_objects["min_age"]

            if person_age < bar_name_data_objects["min_age"]:
                print(f"This person is only {person_age} years old, they cant have alcohol")
            else:
                print(f"This person is over the age of {min_age}")
                if person_drinks > bar_name_data_objects["max_drinks"]:
                    print("This customer has had more than 10 drinks")
                else:
                    print(f"This customer has only had {person_drinks}" )

print("\n")
print(f"{bar_name_title}\'s Rules")
print()

if os.path.exists("bar_rules.json"):
    with open("bar_rules.json") as bar_rules:

        rules_data = json.load(bar_rules)
        
        people(rules_data)