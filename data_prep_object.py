class Quark(object):

    # This method is automatically called whenever we create a new quark.
    # It sets the color and flavor attributes when we create an instance.
    def __init__(self, color, spin, flavor):
        self.color = color
        self.flavor = flavor
        self.spin = spin

    # Every quark has the same baryon number, so we set this outside the
    # init function.
    baryon_number = 1 / 3

    # This method models the way quarks interact with one another by
    # exchanging color.
    def interact(self, other_quark):
        self.color, other_quark.color = other_quark.color, self.color

    # The repr method controls how the object is represented by the
    # print() function and other representations of the object.
    def __repr__(self):
        return "{} {} quark".format(self.color, self.spin, self.flavor)

# Now that we have the class set up, let's call Quark() to create two
# actual instances of quark objects.
q1 = Quark("red", "+1/2", "up")
q2 = Quark("blue","-1/2", "down")

# Print each object to see what they look like.
print("q1 is a {}".format(q1))
print("q2 is a {}".format(q2))

# Test our interact() method by having q1 and q2 interact.
q1.interact(q2)

# Print them out again to see how they changed.
print("Now q1 is a {}".format(q1))
print("Now q2 is a {}".format(q2))

# Test how our object deals with the built-in type() function.
print("q1 is a {} object".format(type(q1)))
