# Rebrick

The *rebrick* library provides a collection of utilities to retrieve various data from
[Rebrickable.com](https://rebrickable.com/) bricks repository. It can be used either as a simple tool, which reads
requested data and converts them into easy-access custom classes or by using the API directly to allow handling the
HTTPResponse in whatever way you want.

Please see the *examples* folder or in-code documentation of classes and functions to learn more about the *rebrick*
library capabilities as well as the original documentation of the
[Rebrickable API](https://rebrickable.com/api/v3/docs/).

See also a similar tool for [BrickSet.com](https://brickset.com/) called [brickse](https://github.com/xxao/brickse).


## Tool Example

```python
import rebrick

# init Rebrick tool
rb = rebrick.Rebrick("your_API_KEY_here", "your_USER_TOKEN_here", silent=True)

# get set info
data = rb.get_set(6608)
print(data)

# if user token is not provided on init you can get it later to access user data
rb.login("your_username_here", "your_password_here")

# get user partlists
data = rb.get_users_partlists()
print(data)
```

## API Example

```python
import rebrick
import json

# init rebrick module for general reading
rebrick.init("your_API_KEY_here")

# get set info
response = rebrick.lego.get_set(6608)
print(json.loads(response.read()))

# init rebrick module including user reading
rebrick.init("your_API_KEY_here", "your_USER_TOKEN_here")

# if you don't know the user token you can use your login credentials
rebrick.init("your_API_KEY_here", "your_username_here", "your_password_here")

# get user partlists
response = rebrick.users.get_partlists()
print(json.loads(response.read()))
```

## Installation

The *rebrick* library is fully implemented in Python. No additional compiler is necessary. After downloading the source
code just run the following command from the *rebrick* folder:

```$ python setup.py install```

or simply by using pip

```$ pip install rebrick```


## Disclaimer

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
