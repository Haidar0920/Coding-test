import json
import argparse
from typing import Union
from pathlib import Path
from calculate import Calculate


class Processor:

    @staticmethod
    def load(data_file):
        """
        Loads json file
        :param data_file: file path as string or pathlib Path
        :return: Python dictionary with data
        """
        with open(data_file, 'r') as f:
            try:
                return json.load(f)
            except Exception as ex:
                print('JSON file was\'t read correctly')
                print(f'Error message was the following {ex}')
                return None

    @staticmethod
    def process(data_file: Union[str, Path]) -> str:
        """
        Processing method
        :param data_file: data_file: file path as string or pathlib Path
        :return: the string message with initial and final sums
        """
        if data := Processor.load(data_file):
            return f'Initial loan sum:\t{data["loan_sum"]:.2f}\n' \
                   f'Final sum:\t\t\t{Calculate.calculate(**data):.2f}'
        else:
            return 'Calculation was unsuccessful'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="json file name to use")
    try:
        args = parser.parse_args()
        result = Processor.process(args.file)
        print(result)
    except:
        print('Required argument file not passed')