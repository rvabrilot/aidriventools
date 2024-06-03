from sqlglot import parse_one
from sqlglot.optimizer.eliminate_subqueries import eliminate_subqueries

def eliminate_subqueries_from(sql):
    """
    This function eliminates subqueries from the input SQL query.
    It takes a SQL query as input and returns a modified SQL query with subqueries eliminated.
    """
    parsed = parse_one(sql)
    if parsed is not None:
        elisub = eliminate_subqueries(parsed).sql(pretty=True)
        return elisub
    else:
        return "Invalid SQL query"

def pretify_sql(sql):
    """
    This function takes a SQL query as input and returns a prettified version of the query.
    """
    parsed = parse_one(sql)
    if parsed is not None:
        return parsed.sql(pretty=True)
    else:
        return "Invalid SQL query"