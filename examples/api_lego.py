#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import json
import rebrick

# Before you can start this example be sure to fill in following variable with
# your specific value:

API_KEY = "your_key"

# set default token for the whole module
rebrick.init(API_KEY)

print("Get part categories:")
response = rebrick.lego.get_categories()
print(json.loads(response.read()))
print()

print("Get part category:")
response = rebrick.lego.get_category(11)
print(json.loads(response.read()))
print()

print("Get colors:")
response = rebrick.lego.get_colors()
print(json.loads(response.read()))
print()

print("Get color:")
response = rebrick.lego.get_color(4)
print(json.loads(response.read()))
print()

print("Get element:")
response = rebrick.lego.get_element(300121)
print(json.loads(response.read()))
print()

print("Get minifig:")
response = rebrick.lego.get_minifig('fig-005891')
print(json.loads(response.read()))
print()

print("Get minifig elements:")
response = rebrick.lego.get_minifig_elements('fig-005891')
print(json.loads(response.read()))
print()

print("Get parts:")
response = rebrick.lego.get_parts('Bilbo')
print(json.loads(response.read()))
print()

print("Get part:")
response = rebrick.lego.get_part(3001)
print(json.loads(response.read()))
print()

print("Get part color:")
response = rebrick.lego.get_part_color(3001, 4)
print(json.loads(response.read()))
print()

print("Get part colors:")
response = rebrick.lego.get_part_colors(3001)
print(json.loads(response.read()))
print()

print("Get part color sets:")
response = rebrick.lego.get_part_color_sets(3001, 4)
print(json.loads(response.read()))
print()

print("Get sets:")
response = rebrick.lego.get_sets(min_year=1082, max_year=1982, min_pieces=20, max_pieces=25)
print(json.loads(response.read()))
print()

print("Get set:")
response = rebrick.lego.get_set(6608)
print(json.loads(response.read()))
print()

print("Get set elements:")
response = rebrick.lego.get_set_elements(6608)
print(json.loads(response.read()))
print()

print("Get set alternates:")
response = rebrick.lego.get_set_alternates(79003)
print(json.loads(response.read()))
print()

print("Get themes:")
response = rebrick.lego.get_themes()
print(json.loads(response.read()))
print()

print("Get theme:")
response = rebrick.lego.get_theme(73)
print(json.loads(response.read()))
print()
