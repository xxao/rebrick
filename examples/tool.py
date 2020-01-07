#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import rebrick

# Before you can start this example be sure to fill in following variables with
# your specific values:

API_KEY = "key"
USER_TOKEN = "token"
USER_NAME = "username"
USER_PASSWORD = "password"

# init Rebrick tool
rb = rebrick.Rebrick(API_KEY, USER_TOKEN, silent=True)

# if user token is not provided on init you can get it later to access user data
rb.login(USER_NAME, USER_PASSWORD)

print("Get part categories:")
data = rb.get_categories()
print(data)
print()

print("Get part category:")
data = rb.get_category(11)
print(data)
print()

print("Get colors:")
data = rb.get_colors()
print(data)
print()

print("Get color:")
data = rb.get_color(4)
print(data)
print()

print("Get element:")
data = rb.get_element(300121)
print(data)
print()

print("Get element ids:")
data = rb.get_element_ids(3001, 4)
print(data)
print()

print("Get element image:")
data = rb.get_element_image(300121)
print(data)
print()

print("Get MOC:")
data = rb.get_moc(24522)
print(data)
print()

print("Get MOC elements:")
data = rb.get_moc_elements(24522)
print(data)
print()

print("Get parts:")
data = rb.get_parts('Bilbo')
print(data)
print()

print("Get part:")
data = rb.get_part(3001)
print(data)
print()

print("Get part colors:")
data = rb.get_part_colors(3001)
print(data)
print()

print("Get part color sets:")
data = rb.get_part_color_sets(3001, 4)
print(data)
print()

print("Get sets:")
data = rb.get_sets(min_year=1982, max_year=1982, min_pieces=20, max_pieces=25)
print(data)
print()

print("Get set:")
data = rb.get_set(6608)
print(data)
print()

print("Get set elements:")
data = rb.get_set_elements(6608)
print(data)
print()

print("Get set themes:")
data = rb.get_set_themes(6608)
print(data)
print()

print("Get set image:")
data = rb.get_set_image(6608)
print(data)
print()

print("Get set alternates:")
data = rb.get_set_alternates(79003)
print(data)
print()

print("Get themes:")
data = rb.get_themes()
print(data)
print()

print("Get theme:")
data = rb.get_theme(73)
print(data)
print()

print("Get user's elements:")
data = rb.get_users_elements(color_id=0)
print(data)
print()

print("Get user's lost elements:")
data = rb.get_users_lost_elements()
print(data)
print()

print("Get user's part lists:")
data = rb.get_users_partlists()
print(data)
print()

print("Get user's part list:")
data = rb.get_users_partlist(21261)  # provide your own list ID
print(data)
print()

print("Get user's part list elements:")
data = rb.get_users_partlist_elements(21261)  # provide your own list ID
print(data)
print()

print("Get user's sets:")
data = rb.get_users_sets()
print(data)
print()

print("Get user's set lists:")
data = rb.get_users_setlists()
print(data)
print()

print("Get user's set list:")
data = rb.get_users_setlist(84012)  # provide your own list ID
print(data)
print()

print("Get user's set list sets:")
data = rb.get_users_setlist_sets(84012)  # provide your own list ID
print(data)
print()
