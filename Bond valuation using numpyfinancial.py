# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 11:42:13 2022

@author: Giri
"""


import numpy_financial as npf
import numpy as np

principal = 1000
annual_interest = 0.04 #riskfree rate
period = 3
coupon_payment = 0.10 * principal #(couponrate* principal)

bond_price = (npf.pv(annual_interest, period, coupon_payment, principal)) * -1
print("The price of bond is( using numpy financial) : $" + str(bond_price))