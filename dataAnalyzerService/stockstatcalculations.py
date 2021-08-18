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


def calculate_cfa_quick_ratio(cash, marketable_securities, recievables, current_liabilities):
    cfa_quick_ratio = ((cash + marketable_securities + recievables) / current_liabilities)
    return cfa_quick_ratio


# Leverage Ratios
def calculate_debt_ratio(total_liabilities, total_assets):
    debt_ratio = (total_liabilities / total_assets)
    return debt_ratio


def calculate_debt_to_equity(total_debt, total_equity):
    debt_to_equity = (total_debt / total_equity)
    return debt_to_equity

def calculate_cash_ratio(cash, marketable_securities, current_liabilities):
    cash_ratio = ((cash + marketable_securities) / current_liabilities)
    return cash_ratio


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


# EPS Calculations

def calculate_basic_eps(ttm_netIncome, ttm_preferredDivs, weighted_avg_num_comm_shrs_outstanding):
    basic_eps = ((ttm_netIncome - ttm_preferredDivs) / weighted_avg_num_comm_shrs_outstanding)
    return basic_eps


def calculate_cfa_diluted_eps(net_income, preferred_divs, convertible_pref_dividends, convertible_debt_interest,
                              corporate_tax_rate, weighted_avg_shares, shares_from_convers_of_conv_pref_shares,
                              shares_from_conversion_of_debt, shares_issuable_from_stock_options):
    cfa_diluted_eps = (((net_income - preferred_divs) + convertible_pref_dividends + (
                convertible_debt_interest * (1 - corporate_tax_rate))) / (
                                   weighted_avg_shares + shares_from_convers_of_conv_pref_shares + shares_from_conversion_of_debt + shares_issuable_from_stock_options))
    return cfa_diluted_eps



# Activity Ratios
def calculate_inventory_turnover(cogs, average_inventory):
    inventory_turnover = (cogs/average_inventory)
    return inventory_turnover


def calculate_days_of_inv_on_hand(average_inventory, cogs):
    days_of_inv_on_hand = ((average_inventory / cogs)*365)
    return days_of_inv_on_hand


def calculate_recievables_turnover(revenue, average_recievables):
    recievables_turnover = (revenue / average_recievables)
    return recievables_turnover


def calculate_days_of_sales_outstanding(avg_recievables, revenue):
    days_of_sales_outstanding = ((avg_recievables / revenue) *365)
    return days_of_sales_outstanding


#Coverage Ratios

def calculate_debt_coverage_ratio(operating_cash_flow, total_debt ):
    debt_coverage_ratio = (operating_cash_flow / total_debt)
    return debt_coverage_ratio


def calculate_interest_coverage_ratio(operating_cash_flow, interest_paid, taxes_paid):
    interest_coverage_ratio = ((operating_cash_flow + interest_paid + taxes_paid) / interest_paid)
    return interest_coverage_ratio
