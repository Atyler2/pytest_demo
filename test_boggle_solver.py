import unittest
import sys

sys.path.append("/home/codio/workspace/") #have to tell the unittest the PATH to find boggle_solver.py and the Boggle Class

from boggle_solver import Boggle

class TestSuite_Alg_Scalability_Cases(unittest.TestCase):
    # ADD 4x4, 5x5, 6x6, 7x7...13x13, and LARGER 
    
    #COME BACK TO THIS!!
    def test_Normal_case_3x3(self):
        grid = [["A", "B", "C"],["D", "E", "F"],["G", "H", "I"]]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["abc", "abdhi", "cfi", "dea"]
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    def test_Normal_case_4x4(self):
        grid = [["A", "B", "C", 'D'],["E", "F", "G", 'H',],["I", "J", "K", 'L'],
                 ['M', 'N', 'O', 'P'] ]
        dictionary = ["abcd", "abc", "aei", "aeif", "aeifn", "aabc", "cgkn"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["abcd", "abc", 'aei', "aeif", "cgkn"]
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    def test_Normal_case_5x5(self):
        grid = [["A", "B", 'C','D','E'],
                ["F", "G", "H", 'I','J'],
                ["K", "L", "M", 'N' ,'O'],
                ['P','Q','R','S','T'] ,
                ['U','V','W','X','Y']]
        dictionary = ["abcde", "afkpu", "abchn", "lnno", "abcce", "afk", "vwxt"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["abcde", "afkpu", 'abchn', "afk", "vwxt"]
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)
    
    def test_Normal_case_6x6(self):
        grid = [['A','B','C','D','E','F'], 
                ['G','H','I','J','K','L'], 
                ['M','N','O','P','Q','R'], 
                ['S','T','U','V','W','X'], 
                ['Y','Z','!',"@","#","$"],
                ['%',"^",'&',"*",'(',')']]
        dictionary = ['abcdef', 'agmsy%', 'abciou', 'abipw', '%^*', "nnopw"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["abcdef", "agmsy%", "abciou", "abipw"]
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

class TestSuite_Simple_Edge_Cases(unittest.TestCase):
  #ADD MANY SIMPLE TEST CASES
    def test_SquareGrid_case_1x1(self):
        grid = [["A"]]
        dictionary = ["a", "b", "c"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    def test_SquareGrid_case_1x2(self):
        grid = [["A"], ['B']]
        dictionary = ["a", "b", "c"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)
    
    
    def test_SquareGrid_case_jagged(self):
        grid = [["A"], ['C', 'B']]
        dictionary = ["a", "b", "c"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    def test_EmptyGrid_case(self):
        grid = []
        dictionary = ["a", "b", "c"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)
    
    def test_SquareGrid_case_wrong_dictionary(self):
        grid = [["A", "B", "C"],["D", "E", "F"],["G", "H", "I"]]
        dictionary = ["xyz", "wjk", 'jlm', "opqr" ]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)


    def test_EmptyGrid_case_0x0(self):
        grid = [[]]
        dictionary = ["hello", "there", "general", "kenobi"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

class TestSuite_Complete_Coverage(unittest.TestCase):
  #ADD MANY COMPLEXED TEST CASES 
    def test_case_1(self):  
        self.assertEqual(True, True)

    def test_Complex_case_Snake(self):
        grid = [['A','B','C','D','E'],
                ['F','G','H','I','J'],
                ['K','L','M','N','O'],
                ['P','Q','R','S','T'] ,
                ['U','V','W','X','Y']]
        dictionary = ["kgcio", "xrnhd", "abd", 'fggh']
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["kgcio", "xrnhd"]
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)
    
    def test_Complex_case_Overlap(self):
        grid = [["A","B","C",'D'],
                ["E","F","G",'H'],
                ["I","J","K",'L'],
                ['M','N','O','P'] ]
        dictionary = ['abc', 'abcd', 'bfg', 'bfgh']
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ['abc', 'abcd', 'bfg', 'bfgh']
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)
    
class TestSuite_Qu_and_St(unittest.TestCase):
  #ADD QU AND ST TEST CASES
    def test_case_1(self): 
        self.assertEqual(True, True)

    def test_ST_QU_Test1(self):
        grid = [["A","B","C",'D'],
                ["E","F","QU",'H'],
                ["I","ST","K",'L'],
                ['M','N','O','P'] ]
        dictionary = ['stkl', 'quuko', 'mop', 'quhl']
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ['stkl','quhl']
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)
    

if __name__ == '__main__':
	unittest.main()

