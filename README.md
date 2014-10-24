test-framework
==============

test micro framework in nodejs and python

## Bottle (Python)

Module

- bottle
- gunicorn
- meinheld

## Express (Node)

Module

- express

## Falcon (Python)

Module

- falcon
- gunicorn
- meinheld
- Cython


### Run Server

**Bottle** :

	 gunicorn -b 127.0.0.1:8080 apps_bottle:app -k="meinheld.gmeinheld.MeinheldWorker" -w=5

**Express**:

	 node node_modules/server.js 8080

**Falcon**:

	 gunicorn -b 127.0.0.1:8080 apps_falcon:app -k="meinheld.gmeinheld.MeinheldWorker" -w=5

### Benchmark

	 ab -n 1000 -c 100 http://127.0.0.1:8080/json

### Result

- Bottle (Python) - Requests per second:    4235.04 [#/sec] (mean)

- Express (Node) - Requests per second:    2682.33 [#/sec] (mean)

- Falcon (Python) - Requests per second:    4976.91 [#/sec] (mean)

