# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r


class IndexViewTest(TestCase):
    'Site index tests.'
    def setUp(self):
        self.resp = self.client.get(r('core:index'))

    def test_get(self):
        'GET must return 200 as status code.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Index must be rendered with index.html.'
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_context(self):
        'Signatories must be in context.'
        self.assertIn('signatories', self.resp.context)


class CommunityBadgesViewTest(TestCase):
    'Community badges page tests.'
    def setUp(self):
        self.resp = self.client.get(r('core:community-badges'))

    def test_get(self):
        'GET must return 200 as status code.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Index must be rendered with index.html.'
        self.assertTemplateUsed(self.resp, 'community-badges.html')

    def test_context(self):
        'Context must contain badges.'
        self.assertIn('badges', self.resp.context)
