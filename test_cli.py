import unittest
import cli

class TestCli(unittest.TestCase):

    def setUp(self):
        self.cli = cli.Cli()

    def test_help(self):
        self.assertFalse(self.cli.do_help(""))

    def test_quit(self):
        self.assertTrue(self.cli.do_q(""))
