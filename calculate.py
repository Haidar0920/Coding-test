class Calculate:

    @staticmethod
    def calculate(loan_sum: float, period: int, rate: float) -> float:
        """
        Defines calculation method
        :param loan_sum: initial loan sum
        :param period: period of loan
        :param rate: interest rate
        :return: final loan sum with interest
        """
        return loan_sum * (pow((1 + rate / 12), period))