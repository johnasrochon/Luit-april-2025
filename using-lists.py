# 1) Set the users variable to be an empty list
users = []

assert users == [], f"Expected 'users' to be [] but got: {repr(users)}"

# 2) Add 'kevin', 'bob', and 'alice' to users list in that order without reassigning the variable
users.append('kevin')
users.append('bob')
users.append('alice')

assert users == ['kevin', 'bob', 'alice'], f"Expected 'users' to be ['kevin', 'bob', 'alice'] but got: {repr(users)}"

# 3) Remove 'bob' from the users list without reassigning the variable.
del users[1]

assert users == ['kevin', 'alice'], f"Expected 'users' to be ['kevin', 'alice'] but got: {repr(users)}"

# 4) Reverse the users list and assign the result to 'rev_users'
rev_users = list(reversed(users))

assert users == ['alice', 'kevin'], f"Expected 'users' to be ['alice', 'kevin'] but got: {repr(users)}"

# 5) Add the user 'melody' to users where 'bob' used to be.
users.insert(1, 'melody')
assert users == ['kevin', 'melody', 'alaice'], f"Expected 'users' to be ['kevin', 'melody', 'alice'] but got: {repr(users)}"

# 6) Add the users 'andy', 'wanda', and 'jim' to the users list using a single command

assert users == ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'], f"Expected 'users' to be ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'] but got: {repr(users)}"



