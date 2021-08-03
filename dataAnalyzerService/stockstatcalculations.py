import pandas as pd


# Valuation metrics
def calculate_pe(current_price, earnings):
    pe_ratio = (current_price / earnings)
    return pe_ratio


def calculate_pb(current_price, book_value):
    pb_ratio = (current_price / book_value)
    return pb_ratio


def calculate_ps(current_price, total_sales):
    ps_ratio = (current_price / total_sales)
    return ps_ratio


# Liquidity Ratios
def calculate_current_ratio(current_assets, current_liabilities):
    current_ratio = (current_assets / current_liabilities)
    return current_ratio


def calculate_quick_ratio(current_assets, current_liabilities, inventory):
    quick_ratio = ((current_assets - inventory) / current_liabilities)
    return quick_ratio


# Leverage Ratios
def calculate_debt_ratio(total_liabilities, total_assets):
    debt_ratio = (total_liabilities / total_assets)
    return debt_ratio


def calculate_debt_to_equity(total_debt, total_equity):
    debt_to_equity = (total_debt / total_equity)
    return debt_to_equity


def calculate_interest_coverage_ratio(ebit, interest_expense):
    interest_coverage_ratio = (ebit / interest_expense)
    return interest_coverage_ratio

# def calculate_fixed_charge_coverage_ratio =


# Profitability ratios

def calculate_roe(net_income, total_equity):
    return_on_equity = (net_income / total_equity)
    return return_on_equity


def calculate_roa(net_income, average_assets):
    return_on_assets = (net_income / average_assets)
    return return_on_assets





