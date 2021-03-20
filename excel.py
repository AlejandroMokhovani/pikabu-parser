
import pandas

fd = pandas.DataFrame({
    'Name': [
        'Manchester City', 'Real Madrid', 'Liverpool',
        'FC Bayern München', 'FC Barcelona', 'Juventus'
        ],
    'League': [
        'English Premier League (1)', 'Spain Primera Division (1)',
        'English Premier League (1)', 'German 1. Bundesliga (1)',
        'Spain Primera Division (1)', 'Italian Serie A (1)'
        ],
    'TransferBudget': [
        176000000, 188500000, 90000000,
        100000000, 180500000, 105000000]
    }
)

fd.to_excel('./excel/team.xlsx')

# df.to_excel('./teams.xlsx', sheet_name='Budgets', index=False)
