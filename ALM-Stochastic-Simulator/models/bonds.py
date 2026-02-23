import numpy as np


class FixedRateBond:
    """
    Fixed-rate bond valuation and duration
    """

    def __init__(self, face_value, coupon_rate, maturity):
        self.face_value = face_value
        self.coupon_rate = coupon_rate
        self.maturity = maturity

    def price(self, rate):
        """
        Compute bond price given a constant discount rate
        """
        coupon = self.face_value * self.coupon_rate
        price = 0.0

        for t in range(1, self.maturity + 1):
            price += coupon / (1 + rate) ** t

        price += self.face_value / (1 + rate) ** self.maturity
        return price

    def duration(self, rate):
        """
        Compute Macaulay duration
        """
        coupon = self.face_value * self.coupon_rate
        price = self.price(rate)

        weighted_sum = 0.0
        for t in range(1, self.maturity + 1):
            weighted_sum += t * coupon / (1 + rate) ** t

        weighted_sum += (
            self.maturity * self.face_value / (1 + rate) ** self.maturity
        )

        return weighted_sum / price