#!/usr/bin/env python3
"""FARO-Africa: small-business productive-energy screening. No financing advice."""
import argparse
import json
import math
from pathlib import Path

FIELDS = ('name', 'capital_cost', 'annual_fixed_cost', 'annual_maintenance',
          'annual_extra_gross_margin', 'annual_outage_loss', 'annual_replacement',
          'annual_debt_service')

def nonnegative(x, name):
    if not isinstance(x, (int, float)) or isinstance(x, bool) or not math.isfinite(x) or x < 0:
        raise ValueError(f'{name} must be finite and nonnegative')
    return float(x)

def evaluate(data):
    years = data['years']
    if not isinstance(years, int) or isinstance(years, bool) or years < 1 or years > 30:
        raise ValueError('years must be an integer from 1 to 30')
    discount = nonnegative(data['discount_rate'], 'discount_rate')
    if discount > 1:
        raise ValueError('discount_rate must be <= 1')
    scenarios = data['scenarios']
    if not isinstance(scenarios, list) or len(scenarios) < 2:
        raise ValueError('provide two or more scenarios')
    names = set()
    results = []
    for s in scenarios:
        for k in FIELDS:
            if k not in s:
                raise ValueError(f'missing field {k}')
        name = s['name']
        if not isinstance(name, str) or not name.strip() or name in names:
            raise ValueError('scenario names must be distinct and nonempty')
        names.add(name)
        v = {k: nonnegative(s[k], k) for k in FIELDS if k != 'name'}
        annual_net = (v['annual_extra_gross_margin'] - v['annual_fixed_cost']
                      - v['annual_maintenance'] - v['annual_outage_loss']
                      - v['annual_replacement'])
        npv = -v['capital_cost'] + sum(annual_net / ((1 + discount) ** t)
                                       for t in range(1, years + 1))
        after_debt = annual_net - v['annual_debt_service']
        results.append({'name': name, 'annual_operating_net': round(annual_net, 2),
                        'annual_cash_after_debt': round(after_debt, 2),
                        'project_npv': round(npv, 2),
                        'passes_project_screen': npv >= 0,
                        'passes_liquidity_screen': after_debt >= 0,
                        'screen': 'REVIEW' if npv >= 0 and after_debt >= 0 else 'REJECT_OR_REDESIGN'})
    return {'currency': data.get('currency', 'UNSPECIFIED'), 'years': years,
            'warning': 'Synthetic screening only; not investment, engineering, or credit advice',
            'scenarios': sorted(results, key=lambda r: r['project_npv'], reverse=True)}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('scenario_json', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(evaluate(json.loads(args.scenario_json.read_text(encoding='utf-8'))),
                         indent=2, ensure_ascii=False))
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as err:
        parser.error(str(err))

if __name__ == '__main__':
    main()
