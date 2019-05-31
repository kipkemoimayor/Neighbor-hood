from django.test import TestCase
from .models import Neighbour,Businesses
from django.contrib.auth.models import User
# Create your tests here.
class TestNeighbour(TestCase):
    def setUp(self):
        self.new_hood=Neighbour(name="langata",location="nairobi",occupationCount=20)
        self.new_business=Businesses(businessesName='cofee script',user=User(1),neigbor=Neighbour(1),email='@yahoo.com')
        self.new_user=User(username='collo')
    def test_initialization(self):
        self.assertTrue(self.new_hood.name,'langata')
        self.assertTrue(self.new_hood.location,'nairobi')
        self.assertTrue(self.new_hood.occupationCount,20)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_hood,Neighbour))

    def test_create_neigborhood(self):
        self.new_hood.create_neigborhood()
        hood=Neighbour.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_neigborhood(self):
        self.new_hood.delete_neigborhood()
        hood=Neighbour.objects.all()
        self.assertEqual(len(hood),0)

    def test_find_neigborhood(self):
        self.new_hood.create_neigborhood()
        self.new_hood.find_neigborhood(1)
        hood=Neighbour.objects.all()
        self.assertEqual(len(hood),1)


    def test_initialize(self):
        self.assertEqual(self.new_business.businessesName,'cofee script')
        self.assertEqual(self.new_business.user,User(1))
        self.assertEqual(self.new_business.email,'@yahoo.com')

    def test_instances(self):
        self.assertTrue(isinstance(self.new_business,Businesses))

    def test_create_business(self):
        self.new_user.save()
        self.new_hood.create_neigborhood()
        self.new_business.create_business()
        busines=Businesses.objects.all()
        self.assertTrue(len(busines)>0)

    def test_delete_business(self):
        self.new_business.delete_business()
        busines=Businesses.objects.all()
        self.assertTrue(len(busines)==0)

    def test_update_business(self):
        saved=Businesses.objects.filter(id=1)
        self.assertEqual(len(saved),0)


    def test_find_business(self):
        self.new_business.create_business()
        busines=Businesses.objects.all()
        self.assertTrue(len(busines)>1)

    # def tearDown(self):
    #     self.new_business.delete()
    #     self.new_hood.delete()
    #     self.new_user.delete()
