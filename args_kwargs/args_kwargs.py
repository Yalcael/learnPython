def invite_friends(host_name, *friends):
    invite_friends("Alice", "John", "Max", "David")


# Here's a function called invite_friends, it takes one required argument host_name and then with *friends, it collects all the extra names you provide.
# Now when we call this function like this Python bundles all the extra names into the friends tuple, so you can print them or do whatever you like.


def plan_party(host_name, **party_details):
    plan_party("Alice", music="Jazz", food="Pizza", decorations="Balloons")


# Here's a function called plan_party, it takes a required argument host_name and then with **party_details, it collects all the extra options you provide.
# When we call this function like this, Python gathers all these options into the party_details dictionary, so you can customize your party easily.


# *Args and **Kwargs
#
# The * before Args tells Python to accept any number of positional arguments.
# The arguments are collected into a tuple which you can then use within your function.
#
# Imagine you're throwing a party and you want to invite some friends, but you're not sure how many will show up.
# You create a list of names with a * in front like this : *friends
# This way, you can invite as many friends as you want and Python will handle it for you.
# --------------------
#
# The ** before Kwargs indicates that Python should accept any number of keyword, these arguments are stored in a Python dictionary.
#
# Think of it as planning a party with options. You want to set various parameters like music, food and decorations but some might change.
# You create a dictionary with two ** like this.
# This lets you specify options flexibly.
