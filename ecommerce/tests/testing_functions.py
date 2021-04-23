
"""
Instead of using:
	allUsers = User.objects.using("testing").all()
	self.assertEqual(len(allUsers),0)

Just to write this in one line
"""


def expect_records(case,model,records):
	allRecords = model.objects.all()
	case.assertEqual(len(allRecords),records)


def get_records(case,model):
	allRecords = model.objects.all()
	return len(allRecords)


"""
After populating users you can use this function to test the login
and logout system

"""



from django.test import Client
from tests.populate import users_list_test
def get_all_tokens():
	c = Client()
	toReturn = []
	for user_data in users_list_test:
		response = c.post('/auth/token/login/', data=user_data)
		#print(response.__dict__)
		#print(response.data["auth_token"])
		toReturn.append(response.data["auth_token"])
	return toReturn





