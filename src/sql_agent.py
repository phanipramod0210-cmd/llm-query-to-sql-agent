import argparse, sqlite3

def simple_translate(q):
    q=q.lower()
    if 'total sales' in q:
        return 'SELECT customer, SUM(amount) as total_sales FROM sales GROUP BY customer;'
    return 'SELECT * FROM sales LIMIT 10;'

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--db', required=True)
    p.add_argument('--query', required=True)
    args=p.parse_args()
    sql = simple_translate(args.query)
    print('Generated SQL:\n', sql)
    conn = sqlite3.connect(args.db)
    cur = conn.cursor()
    for row in cur.execute(sql):
        print(row)
