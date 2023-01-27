"""Tests for admin panel"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTests(TestCase):
    """Create user and client"""
    def setUp(self):
        self.client=Client()
        self.admin_user = get_user_model().objects.create_superuser("adminuser@example.com", "abcd123?")
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="abc123?",
            name="Test user"
        )
