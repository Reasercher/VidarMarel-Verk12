from bottle import run, route , request, static_file

#Hér birtum við statískar skrár myndir og css...
def send_css(filename):
    # static/css directory
    return static_file(filename, root='static/css')

# PNG skrár
@route('/static/img/<filename:re:.*\.jpg>')
def send_image(filename):
    # static/img directory
    return static_file(filename, root='static/img', mimetype='image/jpg')
@route('/')
def index():
    return '''
            <!DOCTYPE html>
            <html>
            <head>
                <link rel="stylesheet" href='/static/still.css' />
            </head>
            <body>
            <h1>sida um steve jobs<h1>
            <a href='/jobs?lanes=1'>Steve jobs</a><br>
            <a href='/jobs?lanes=2'>Biography</a><br>
            <a href='/jobs?lanes=3'>Pictures</a>
            </body>
            </html>
            '''

@route('/jobs')
def jobs():
    id = request.query.lanes
    if id == "1":
        return "<p>Hérna er talað um steve jobs. <img src='/static/sj.jpg'></p>"
    if id == "2":
        return "<p>Hér er talað um biography.</p> <img src='/static/bio.jpg'>"
    if id == "3":
        return "<a>Hér eru sýnd mynd   <img src='/static/butterfly.jpg'></a>"


run(host='localhost', port=8080 , debug=True , Reloader=True)
