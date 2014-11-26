test-framework
==============

test micro framework in nodejs and python

## Bottle (Python)

Module

- bottle
- gunicorn



## Express (Node)

Module

- express

## Falcon (Python)

Module

- falcon
- gunicorn
- Cython

## Wheezy.web (Python)

Module

- wheezy
- gunicorn
- Cython

### Run Server

**Bottle** :

	 gunicorn -b 127.0.0.1:8080 apps_bottle:app -w=5
	 
**Wheezy**	 

        gunicorn -b 127.0.0.1:8080 apps_wheezy:app -w=5
        
**Express**:

	 node node_modules/server.js 8080

**Falcon**:

	 gunicorn -b 127.0.0.1:8080 apps_falcon:app -w=5

### Benchmark
        
** JSON Respone**        

	 ab -n 1000 -c 100 http://127.0.0.1:8080/json

	 

### Result

- Bottle (Python) - Requests per second:    4235.04 [#/sec] (mean)

- Express (Node) - Requests per second:    2682.33 [#/sec] (mean)

- Falcon (Python) - Requests per second:    4976.91 [#/sec] (mean)

