import unittest
from main import main
from utilidades import preparar_valores


class TestAssemble(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_main(self):
        expected_values = preparar_valores()
        
        values = main()
        
        self.assertEqual(values, expected_values)
        
if __name__ == "__main__":
    # print(preparar_valores())
    unittest.main()