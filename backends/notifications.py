


@app.before_request
def before():
    print('the request object ready to be processed:', request)


@app.after_request
def after(response):
    """
    Your function must take one parameter, a `response_class` object and return
    a new response object or the same (see Flask documentation).
    """
    print('and here we have the response object instead:', response)
    return response