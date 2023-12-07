#!/usr/bin/python3
"""Unittest for BaseModel"""

import unittest
from models.base_model import BaseModel

class testBaseModel(unittest.TestCase):
    """Test for BaseModel Class"""

    def test_equal_string(self):
        """Check if id is a string"""
        self.assertEqual(str, type(BaseModel().id))

    def test_unique_id(self):
        """Check if the id in unique"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_instance_id(self):
        """Check if id is a intance of BaseModel"""
        self.assertTrue(hasattr(BaseModel(), "id"), True)

    def test_instance_createdat(self):
        """Check if created_at is a intance of BaseModel"""
        self.assertTrue(hasattr(BaseModel(), "created_at"), True)

    def test_instance_updatedat(self):
        """Check if updated_at is a intance of BaseModel"""
        self.assertTrue(hasattr(BaseModel(), "updated_at"), True)    
        
    def test_base_instance(self):
        """Check if instace is a Intance of BaseModel"""
        self.assertIsInstance(BaseModel(), BaseModel)
        
        