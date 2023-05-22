import unittest
from recipes import Runner

test_db = 'test_data.json'

class Testing(unittest.TestCase):

    def setUp(self):
        self.runner = Runner(db=test_db)

    def test_show_recipes(self):
        self.runner.show_recipes()
    
    def test_add_recipe(self):
        self.runner.add_recipe_to_list("1")

    def test_remove_latest_recipe(self):
        self.runner.add_recipe_to_list("2")
        assert len(self.runner.groceries) == 1

    def test_show_grocery_list(self):
        self.runner.show_grocery_list()

    def test_finalize_list(self):
        self.runner.finalize_list()

    def test_rest_list(self):
        self.runner.reset_list()
    
if __name__ == '__main__':
    unittest.main()