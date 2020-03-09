from django.test import SimpleTestCase
from django.urls import reverse, resolve
from what_cheer.views import EntryList, EntryDetail, PromptDetail

# pip install virtualenvwrapper

class TestUrls(SimpleTestCase):

    def test_entries_url_resolves(self):
        url = reverse('entry_list')
        self.assertEquals(resolve(url).func.view_class, EntryList)
    def test_entry_detail_url_resolves(self):
        url = reverse('entry_detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, EntryDetail)
    def test_prompt_detail_url_resolves(self):
        url = reverse('prompt_detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, PromptDetail)