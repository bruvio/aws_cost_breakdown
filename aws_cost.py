#!/usr/bin/env python
# -*- encoding: utf-8

import datetime as dt
from urllib.parse import urlencode, urlparse, urlunparse
import webbrowser


today = dt.datetime.now()

query_dict = {
    # Look at costs for the last thirty days
    "startDate": (today - dt.timedelta(days=30)).strftime("%Y-%m-%d"),
    "endDate": today.strftime("%Y-%m-%d"),
    "timeRangeOption": "Custom",

    # Break down costs by day
    "granularity": "Daily",

    # Line chart of API operation costs
    "chartStyle": "Line",
    "filter": '[{"dimension":"Operation","values":[""],"include":false,"children":null}]',
    "groupBy": "Operation",

    # Give it a nice title
    "isTemplate": "true",
    "reportName": "Daily API operation costs",
    "reportType": "CostUsage",
}

parts = [
    # scheme
    "https",

    # netloc
    "console.aws.amazon.com",

    # path
    "/cost-reports/home",

    # params
    "",

    # query
    "",

    # fragment
    "/custom?%s" % urlencode(query_dict)
]

webbrowser.open(urlunparse(parts))
