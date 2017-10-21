#import psycopg2
import psycopg2

DBNAME = "news"


def execute_query(query):
    ''' Executes a query to the news database and returns data '''
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()


# 1. What are the most popular three articles of all time?
QUERY_1 = ''' SELECT title, count(*) AS num
FROM articles 
INNER JOIN log ON log.path=CONCAT('/article/',articles.slug) 
GROUP BY articles.title 
ORDER BY num DESC; '''

# 2. Who are the most popular article authors of all time?
QUERY_2 = ''' SELECT authors.name, count(log.path) AS count
FROM articles, log, authors
WHERE articles.slug = replace(log.path,'/article/','')
AND articles.author = authors.id
GROUP BY authors.name
ORDER BY count DESC; '''

# 3. On which days did more than 1% of requests lead to errors?
QUERY_3 = ''' SELECT * FROM
(SELECT date(time), ROUND(100.0 * SUM(CASE log.status WHEN '200 OK' THEN 0 ELSE 1 END) / COUNT(log.status), 2) AS error FROM log GROUP BY date(time) ORDER BY error desc) 
AS result WHERE error > 1; '''


def print_query_1_results(query):
    ''' Formats and prints the results of query 1 returned from execute_query '''
    results = execute_query(query)
    print('\n1. The most popular Articles of all time are:\n')
    for result in results:
        print('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')


def print_query_2_results(query):
    ''' Formats and prints the results of query 2 returned from execute_query '''
    results = execute_query(query)
    print('\n2. The most popular article authors of all time are:\n')
    for result in results:
        print('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')


def print_query_3_results(query):
    ''' Formats and prints the results of query 3 returned from execute_query '''
    results = execute_query(query)
    print('\n3. Which day did more than 1% of requests lead to errors:\n')
    for result in results:
        print('The day of ' +
              str(result[0]) + ' led to more than 1% of errors with a precentage of ' + str(result[1]) + '%.')


# print out results
print_query_1_results(QUERY_1)
print_query_2_results(QUERY_2)
print_query_3_results(QUERY_3)
