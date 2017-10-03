from bottle import route, run, request

import sparser

@route('/expr/')
@route('/expr/<expression>')
def evaluate(expression=""):
    print(expression)
    value = sparser.check(expression)
    print(value)
    if value == None:
        value = '#NONE#'
    return {'expression':expression, 'value':value}

run(host='localhost', port=8080, reloader=True)