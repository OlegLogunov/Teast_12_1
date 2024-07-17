import HomeWork1Mod12
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        ocr = HomeWork1Mod12.Runner("Олег")
        for _ in range(10):
            ocr.walk()
        self.assertEqual(ocr.distance, 50)

    def test_run(self):
        ocr = HomeWork1Mod12.Runner("Олег")
        for _ in range(10):
            ocr.run()
        self.assertEqual(ocr.distance, 100)

    def test_challenge(self):
        Elena = HomeWork1Mod12.Runner("Елена")
        Tat = HomeWork1Mod12.Runner("Татьяна")
        for _ in range(10):
            Elena.walk()
            Tat.run()
        self.assertNotEqual(Elena.distance, Tat.distance)

if __name__ == "__main":
    unittest.main
