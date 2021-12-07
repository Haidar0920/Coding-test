# Coding-test
I solved test task № 2
~~~
Here we're going to create a script that should calculate cumulative interest paid on a loan
for the specific period. Don't use 3rd parties libraries in your solution and use native python
functions.

Result
We expect to have an endpoint, that will receive necessary parameters as JSON object for
the calculation and return interest paid. Assumptions: payment is at the end of a period,
interest and taxes can be omitted.
~~~ 
imported only json (because i can't put json file on input without it ) and some libraries for endpoint (fastapi etc.)

I made 2 decisions by this task
1) cli - a solution through a command program, as a program - a file name
2) app - a solution option via fastapi, sending json using the POST method to http://127.0.0.1:5000/calculate/

### data.json - it's a example of input data 

### calculate.py- calculation of cumulative interest
