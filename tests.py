
import os
import sys
import unittest

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'lib'))

import db
import service

class ServiceTest(unittest.TestCase):
    def setUp(self):
        db.db.init(':memory:')
        db.db.create_tables([db.User, db.File, db.FileAlias])

    def test_save_file(self):
        test_file1 = open('tests/test_image.jpg')
        user = db.User.create(email='me@site.com')

        num_alias = 5
        with db.db.atomic():
            file_ = service.save_file(user, test_file1, num_alias)

        test_file1.close()
        total_alias = file_.aliases.select().count()
        assert total_alias == num_alias, (total_alias, num_alias)

unittest.main()
