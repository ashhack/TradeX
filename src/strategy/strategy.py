from abc import ABC, abstractmethod


class Strategy:

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def apply(self):
        pass

    @abstractmethod
    def backtest(self):
        pass

