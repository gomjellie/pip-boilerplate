from unittest import TestCase

from click.testing import CliRunner

import boilerplate


class BoilerPythonTest(TestCase):
    """
        Sample Test
    """

    def __init__(self):
        super().__init__()
        self.runner = CliRunner()

    def run_print_string(self):
        result = self.runner.invoke(boilerplate.print_string, ["print", "hello"])
        print(result)
        output_string = str(result.output.encode('ascii', 'ignore').decode("utf-8"))
        print(output_string)


class BoilerCliTest(TestCase):
    def __init__(self):
        super().__init__()
        self.runner = CliRunner()

