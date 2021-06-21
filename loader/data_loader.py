import json
import re

# Open the file
arcana_file = open("../data/p5r/arcana_list.json")
double_element_recipes_file = open("../data/p5r/double_element_recipes.json")
element_fusion_chart_file = open("../data/p5r/element_fusion_chart.json")
element_recipes_file = open("../data/p5r/element_recipes.json")
elements_list_file = open("../data/p5r/elements_list.json")
full_compendium_file = open("../data/p5r/full_compendium.json")
full_skills_file = open("../data/p5r/full_skills.json")
min_compendium_file = open("../data/p5r/min_compendium.json")
normal_recipes_file = open("../data/p5r/normal_recipes.json")
reverse_fusion_chart_file = open("../data/p5r/reverse_fusion_chart.json")
special_recipes_file = open("../data/p5r/special_recipes.json")

# Load the file
arcana = json.load(arcana_file)
double_element_recipes = json.load(double_element_recipes_file)
element_fusion_chart = json.load(element_fusion_chart_file)
element_recipes = json.load(element_recipes_file)
elements_list = json.load(elements_list_file)
full_compendium = json.load(full_compendium_file)
full_skills = json.load(full_skills_file)
min_compendium = json.load(min_compendium_file)
normal_recipes = json.load(normal_recipes_file)
reverse_fusion_chart = json.load(reverse_fusion_chart_file)
special_recipes = json.load(special_recipes_file)

# Close the files after load
arcana_file.close()
double_element_recipes_file.close()
element_fusion_chart_file.close()
element_recipes_file.close()
elements_list_file.close()
full_compendium_file.close()
full_skills_file.close()
min_compendium_file.close()
normal_recipes_file.close()
reverse_fusion_chart_file.close()
special_recipes_file.close()

# Fix the data double_element_recipes
for element in double_element_recipes:
    element_tuples_list = []
    for element_recipe in double_element_recipes[element]:
        element_groups = re.search("(.+) x (.+)", element_recipe)
        tuple_element = element_groups.groups(0)
        element_tuples_list.append(tuple_element)
    double_element_recipes[element] = element_tuples_list

# Fix the data element_recipes
for element in element_recipes:
    element_tuples_dict = {}
    for element_recipe in element_recipes[element]:
        element_groups = re.search("(.+) x (.+)", element_recipe)
        (name, rank) = element_groups.groups(0)
        element_tuples_dict[name] = int(rank)
    element_recipes[element] = element_tuples_dict


