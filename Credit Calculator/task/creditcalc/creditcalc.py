import math
import argparse


# Dm = mth differentiated payment
# P = credit principal
# i = nominal (monthly) interest int / 12 * 100
# n = number of payments (months)
# m = current period

# param
# --type      - diff or annuity
# --principal - (P)
# --periods   - (n)
# --interest  - (i)
# --payment   - (Dm) INVALID - Incorrect parameters
class PaymentCalculations:

    def __init__(self, principal, periods, interest, payment):
        if principal is None:
            principal = 0
        self.principal = float(principal)
        if periods is None:
            periods = 0
        self.periods = int(periods)
        if interest is None:
            interest = 0
        self.interest = float(interest)
        if payment is None:
            payment = 0
        self.payment = float(payment)

    def check_negatives(self):
        if self.periods < 0:
            return True
        if self.payment < 0:
            return True
        if self.interest < 0:
            return True
        if self.principal < 0:
            return True
        return False

    def get_periods(self):
        n = self.periods

    def get_principal(self):
        P = self.interest * self.periods * self.payment

    def get_differentiated(self):
        overtotal=0
        P = self.principal
        n = self.periods
        i = self.interest / (12 * 100)
        if P == 0 and n == 0 and i == 0:
            print('Incorrect parameters')
        else:
            for m in range(1, n + 1):
                a = math.ceil((P / n) + i * (P - ((P * (m - 1) / n))))
                print('Month {0}: paid out {1}'.format(m, a))
                overtotal += a
            over = math.ceil(int(overtotal - P))
            print('Overpayment = {0}'.format(over))

    def annuity_calcs(self):
        global month_s, year_s
        P = self.principal
        n = self.periods
        i = self.interest
        A = self.payment
        monthly_i = i / (100 * 12)
        if i == 0:
            print('Incorrect parameters')
        if (P == 0 or n == 0 or i == 0) and A == 0:
            print('Incorrect parameters')
        if P != 0 and n != 0 and i != 0:
            annuity = math.ceil(P * (monthly_i * math.pow(1 + monthly_i, n) / (math.pow(1 + monthly_i, n) - 1)))
            overpayment = int((annuity * n) - P)
            print("Your annuity payment = {0}!".format(annuity))
            print("Overpayment = {0}".format(overpayment))
        if A != 0 and P != 0 and i != 0:
            months = math.ceil(math.log((A / (A - monthly_i * P)), (1 + monthly_i)))
            overpayment = int((A * months) - P)
            if months / 12 > 1:
                year_s = 's'
            if months % 12 != 1:
                months_s = 's'
            if months % 12 == 0:
                print("You need {0} year{1} to repay this credit!".format(math.floor(months / 12), year_s))
            if months < 12:
                print("You need {0} month{1} to repay this credit!".format(months, month_s))
            else:
                print("You need {0} year{1} and {2} month{3} to repay this credit!".format(math.floor(months / 12), year_s, months % 12, months_s))
            print("Overpayment = {0}".format(overpayment))
        if A != 0 and n != 0 and i != 0:
            credit_principal = math.floor(A / (monthly_i * math.pow(1 + monthly_i, n) / (math.pow(1 + monthly_i, n) - 1)))
            overpayment = int((A * n) - credit_principal)
            print("Your credit principal payment = {0}!".format(credit_principal))
            print("Overpayment = {0}".format(overpayment))


ap = argparse.ArgumentParser()
ap.add_argument("-t", "--type", required=True,
                help="annuity or diff", choices=['diff', 'annuity'], type=str)
ap.add_argument("-P", "--principal", required=False,
                help="The credit principal", type=float)
ap.add_argument("-n", "--periods", required=False,
                help="The number of payment periods", type=int)
ap.add_argument("-i", "--interest", required=False,
                help="Annual interest rate", type=float)
ap.add_argument("-p", "--payment", required=False,
                help="Period payment value", type=float)
args = vars(ap.parse_args())

if len(args) < 5:
    print('Incorrect parameters')
    exit(0)
class_diff = PaymentCalculations(args['principal'], args['periods'], args['interest'], args['payment'])
if class_diff.check_negatives():
    print('Incorrect parameters')
    exit(0)
if args['type'] == 'diff':
    if args['principal'] is None or args['periods'] is None or args['interest'] is None:
        print('Incorrect parameters')
        exit(0)
    class_diff.get_differentiated()

if args['type'] == 'annuity':
    class_diff.annuity_calcs()
