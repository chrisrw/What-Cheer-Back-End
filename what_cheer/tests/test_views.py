from django.test import TestCase, Client
from django.urls import reverse
from what_cheer.models import Entry, Prompt
from what_cheer.views import EntryList, EntryDetail, PromptDetail
from rest_framework.test import force_authenticate, APIRequestFactory
from django.contrib.auth.models import User

# factory = APIRequestFactory()
# user = User.objects.get(username='chrisrw')


class TestViews(TestCase):
    
    def test_entry_list(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@gmail.com', password='top_secret')
        request = self.factory.get('/entries/')
        force_authenticate(request, user=self.user)
        response = EntryList.as_view()(request)
        self.assertEqual(response.status_code, 200)

    # def test_entry_detail(self):
    #     self.factory = APIRequestFactory()
    #     self.user = User.objects.create_user(
    #         username='jacob', email='jacob@gmail.com', password='top_secret')
    #     request = self.factory.get('/entries/')
    #     force_authenticate(request, user=self.user)
    #     response = EntryDetail.as_view()(request, pk='1')
    #     self.assertEqual(response.status_code, 200)







    # def test_entry_list_GET_fails_without_token(self):
    #     client = Client()

    #     response = client.get(reverse('entry_list'))

    #     self.assertEqual(response.status_code, 401)
    # def test_prompt_GET_passes(self):
        
    #     client = Client()

    #     response = client.get(reverse('prompt_detail', args=[1]))

    #     self.assertEqual(response.status_code, 200)
        