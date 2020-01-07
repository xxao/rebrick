#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import json
import rebrick

# Before you can start this example be sure to fill in following variables with
# your specific values:

API_KEY = "key"
USER_TOKEN = "token"
USER_NAME = "username"
USER_PASSWORD = "password"

# set default tokens for the whole module directly
rebrick.init(API_KEY, USER_TOKEN)

# OR set default tokens for the whole module by login credentials
rebrick.init(API_KEY, USER_NAME, USER_PASSWORD)

print("Get badges:")
response = rebrick.users.get_badges()
print(json.loads(response.read()))
print()


print("Get badge:")
response = rebrick.users.get_badge(1)
print(json.loads(response.read()))
print()

print("Get build:")
response = rebrick.users.get_build(6608)
print(json.loads(response.read()))
print()

print("Get elements:")
response = rebrick.users.get_elements(color_id=0)
print(json.loads(response.read()))
print()

print("Get lost elements:")
response = rebrick.users.get_lost_elements()
print(json.loads(response.read()))
print()

print("Get part lists:")
response = rebrick.users.get_partlists()
print(json.loads(response.read()))
print()

print("Get part list:")
response = rebrick.users.get_partlist(21261)  # provide your own list ID
print(json.loads(response.read()))
print()

print("Get part list elements:")
response = rebrick.users.get_partlist_elements(21261)  # provide your own list ID
print(json.loads(response.read()))
print()

print("Get part list element:")
response = rebrick.users.get_partlist_part_color(21261, 10884, 27)  # provide your own list ID
print(json.loads(response.read()))
print()

print("Get elements in lists:")
response = rebrick.users.get_partlists_elements('dish')
print(json.loads(response.read()))
print()

print("Get profile:")
response = rebrick.users.get_profile()
print(json.loads(response.read()))
print()

print("Get sets:")
response = rebrick.users.get_sets()
print(json.loads(response.read()))
print()

print("Get set lists:")
response = rebrick.users.get_setlists()
print(json.loads(response.read()))
print()

print("Get set list:")
response = rebrick.users.get_setlist(84012)  # provide your own list ID
print(json.loads(response.read()))
print()

print("Get set list sets:")
response = rebrick.users.get_setlist_sets(84012)  # provide your own list ID
print(json.loads(response.read()))
print()

print("Get user token:")
response = rebrick.users.get_token(USER_NAME, USER_PASSWORD)
print(json.loads(response.read()))
print()
