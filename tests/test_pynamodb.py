from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


# NOTES:
# hash key  == partition key
# sort key  == range key


# PROS: IS SIMPLE
# CONS: ON QUERIES, IT DOESNT RETURN PYDANTIC OBJECTS, BUT Model objects

class UserModel(Model):
    class Meta:
        table_name = "mydynamotable"

    id = UnicodeAttribute(hash_key=True)    # partition key
    email = UnicodeAttribute(null=True)



def test_pynamo():
    # UserModel.create_table(read_capacity_units=1, write_capacity_units=1)

    #  create
    user = UserModel("John")
    user.email = "djohn@company.org"
    user.save()

    # update
    user = UserModel("John")
    user.email = "newemail@company.org"
    user.save()

def test_can_query():
    for user in UserModel.query("John", None):
        print(user)