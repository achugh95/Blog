from django.test import TestCase
from django.urls import reverse, resolve

# Create your tests here.


class TestUrls(TestCase):

    # Contact Us
    def test_contact_url(self):
        url = reverse('contact_us')                             # Value Received
        assert resolve(url).view_name == 'contact_us'           # Expected results

    # Homepage
    def test_home_url(self):
        url = reverse('list_all_posts')
        assert resolve(url).view_name == 'list_all_posts'

    # Detail view of Posts
    def test_blog_detail_url(self):
        url = reverse('detail_post', kwargs={'pk': 1})
        assert resolve(url).view_name == 'detail_post'

    # Create Post
    def test_create_blog_url(self):
        url = reverse('create_post')
        assert resolve(url).view_name == 'create_post'

    # Edit Post
    def test_edit_blog_url(self):
        url = reverse('edit_post', kwargs={'pk': 1})
        assert resolve(url).view_name == 'edit_post'
