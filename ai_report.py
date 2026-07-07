name: AMRC Daily Update
on:
  schedule:
    - cron: '0 23 * * *'
  workflow_dispatch:
jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python automation/fetch_market.py
      - run: python automation/ai_report.py
      - run: python automation/social_generator.py
