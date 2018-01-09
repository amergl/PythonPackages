from nose.tools import assert_almost_equals

from AverageCalculator import *

from numpy import *

class TestAverageCalculator:

    EPS=1e-16

    N_FILES=10

    PATH_ALL_ZEROS="test/all_zeros"

    PATH_ALL_ONE="test/all_one"

    PATH_ASCENDING="test/ascending"

    PATH_FLOATINGPOINT="test/floatingpoint"

    def testAllZeros(self):
        calculator=AverageCalculator(TestAverageCalculator.PATH_ALL_ZEROS)
        points,average=calculator.GetResult()

        solution=zeros(TestAverageCalculator.N_FILES,dtype=float);

        assert average.shape == solution.shape
        error=linalg.norm(average-solution)
        assert_almost_equals(linalg.norm(average-solution),0,delta=TestAverageCalculator.EPS)

    def testAllOne(self):
        calculator=AverageCalculator(TestAverageCalculator.PATH_ALL_ONE)
        points,average=calculator.GetResult()

        solution=ones(TestAverageCalculator.N_FILES,dtype=float);

        assert average.shape == solution.shape
        error=linalg.norm(average-solution)
        assert_almost_equals(linalg.norm(average-solution),0,delta=TestAverageCalculator.EPS)

    def testAscending(self):
        calculator=AverageCalculator(TestAverageCalculator.PATH_ASCENDING)
        points,average=calculator.GetResult()

        #starting at 0
        n=TestAverageCalculator.N_FILES-1
        #gauss formula
        solution_value=n*(n+1)/2
        solution_value/=float(TestAverageCalculator.N_FILES)
        solution=solution_value*ones(TestAverageCalculator.N_FILES)

        assert average.shape == solution.shape
        error=linalg.norm(average-solution)
        assert_almost_equals(linalg.norm(average-solution),0,delta=TestAverageCalculator.EPS)

    def testFloatingPoint(self):
        calculator=AverageCalculator(TestAverageCalculator.PATH_FLOATINGPOINT)
        points,average=calculator.GetResult()

        solution=0.1*ones(TestAverageCalculator.N_FILES)

        assert average.shape == solution.shape
        error=linalg.norm(average-solution)
        assert_almost_equals(linalg.norm(average-solution),0,delta=TestAverageCalculator.EPS)
