#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    
    def test_get(self):
        """test docs docs"""
        state1 = State(name="state1")
        state2 = State(name="state2")
        state3 = State(name="state3")
        models.storage.new(state1)
        models.storage.new(state2)
        models.storage.new(state3)
        models.storage.save()
        models.storage.close()
        first_state = list(models.storage.all().values())[2]
        first_state_id = first_state.id
        get = models.storage.get(State, first_state_id)
        self.assertEqual(get.id, first_state_id)
        models.storage.delete(get)
        models.storage.save()
        models.storage.close()
        get = models.storage.get(State, first_state_id)
        self.assertEqual(get, None)


class TestFileStorage2(unittest.TestCase):
    """test docs docs"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_count(self):
        """test docs docs"""
        state1 = State(name="state1")
        state2 = State(name="state2")
        state3 = State(name="state3")
        city1 = City(state_id=state1.id, name="San Francisco")
        city2 = City(state_id=state2.id, name="San Francisco2")
        city3 = City(state_id=state3.id, name="San Francisco3")
        models.storage.new(state1)
        models.storage.new(state2)
        models.storage.new(state3)
        models.storage.new(city1)
        models.storage.new(city2)
        models.storage.new(city3)
        models.storage.save()
        models.storage.close()
        total = len(models.storage.all())
        total_state = len(models.storage.all(State))
        count_total = models.storage.count()
        count_state = models.storage.count(State)
        self.assertEqual(total, count_total)
        self.assertEqual(total_state, count_state)
