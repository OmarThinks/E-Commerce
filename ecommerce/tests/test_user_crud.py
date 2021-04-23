# python manage.py migrate --database testing
# python manage.py test
# python manage.py test users.tests


from unittest import TestCase
from django.test import Client
from users.models import User
from tests.populate import (delete_all_records, 
	populate_users , delete_users, poplating_user_using_djoser,
	get_djoser_token,
	)

from tests.testing_functions import expect_records

class TestCaseAllWorking(TestCase):
	def test_case1(self):
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("Testing User Model")
	









class User_TestCase_01_CRUD(TestCase):
	"""docstring for ClassName"""
	

	"""@classmethod
	def setUpClass(cls):
		print("setUpClass")"""
	def setUp(self):
		self.client = Client()	

	@classmethod
	def setUpClass(cls):
		delete_all_records() 
		print("")
		print("")
		print("User_TestCase_01_CRUD") 
		print("---")
		print("---")

	def tearDown(self):
		"""Executed after reach test"""
		print("_+++++++++++++++++++++++++++++++++_")


	def test_01_make_sure_no_users(self):
		expect_records(self,User,0)
		print("test_01_make_sure_no_users")


	def test_02_create_a_user(self):
		User.objects.create(username = "user1",
			email = "",password = "ant") # 1
		expect_records(self,User,1)
		print("test_02_create_a_user")
				


	def test_03_delete_a_user(self):
		expect_records(self,User,1)
		User.objects.first().delete()
		expect_records(self,User,0)
		print("test_03_delete_a_user")
		

	def test_04_populate_users(self):
		expect_records(self,User,0)
		populate_users()
		expect_records(self,User,20)
		print("test_04_populate_users")

	def test_05_populate_users(self):
		expect_records(self,User,20)
		populate_users()
		expect_records(self,User,20)
		print("test_05_repopulate_users")

	def test_06_delete_users(self):
		expect_records(self,User,20)
		delete_users()
		expect_records(self,User,0)
		print("test_06_delete_users")


	def test_07_delete_all_records(self):
		populate_users()
		expect_records(self,User,20)
		delete_all_records()
		expect_records(self,User,0)
		print("test_07_delete_all_records")


	def test_08_duplicate_username(self):
		expect_records(self,User,0)
		User.objects.create(username = "user1",
			email = "",password = "ant") # 1
		try:
			User.objects.create(
				username = "user1",
				email = "",password = "ant") # 1
			raise Exception("can not create a"+
				" user with duplicate username")
		except Exception as e:
			#print(str(e))
			self.assertEqual(str(e),
				"UNIQUE constraint failed: users_user.username")	
		expect_records(self,User,1)
		print("test_08_duplicate_username")

	def test_09_user_props(self):
		user = User.objects.first()
		self.assertEqual(user.username,"user1")
		self.assertEqual(user.email,"")
		self.assertEqual(user.password,"ant")
		#print(user.__dict__)
		"""
{
	'_state': <django.db.models.base.ModelState object 
	at 0x000001FB97C29848>, 
	'id': 1886, 
	'password': 'ant', 
	'last_login': None, 
	'is_superuser': False, 
	'username': 'user1', 
	'first_name': '', 
	'last_name': '', 
	'email': '', 
	'is_staff': False, 
	'is_active': True, 
	'date_joined': datetime.datetime(2021, 4, 14, 
	1, 3, 50, 466343, 
	tzinfo=<UTC>)
}
		"""
		print("test_09_user_props")




