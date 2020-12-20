class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
        self.user_group_dict = {}

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    else:
        child_groups = group.get_groups()
        for child_group in child_groups:
            return is_user_in_group(user, child_group)
    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

new_group = Group("best_group")


# Testcase1: user is direct child of the group
is_member = is_user_in_group(sub_child_user, sub_child)  # True
print(is_member)

# Testcase2: user is grandchild of the group
is_member = is_user_in_group(sub_child_user, parent)  # True
print(is_member)

# Testcase3: user is not child of the group
is_member3 = is_user_in_group(sub_child_user, new_group)  # False
print(is_member)
