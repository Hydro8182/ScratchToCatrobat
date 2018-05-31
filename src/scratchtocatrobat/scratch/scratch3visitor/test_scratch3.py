import unittest
from  scratchtocatrobat.scratch.scratch3visitor.looks import visitShow
globcount = 0
def createScratch3Block(opcode, arguments):
    block = {}
    block['name'] = "opcode_" + str(globcount)

    global globcount
    globcount += 1

    block['opcode'] = opcode
    block['inputs'] = {}


class TestScratch3Blocks(unittest.TestCase):
    def setUp(self):
        print "test is executed"

    def test_test(self):
        print "testset"

    def test_showSpriteBlock(self):
        testblock = createScratch3Block("show",[])
        converted_block = visitShow(testblock, {})
        print converted_block


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
