# web control of 4 motor with mecanum wheels robot
#  
from microdot import Microdot
import mecanum_motores

v='0.6'
print(f'web v{v}')

app = Microdot()

WEB_PORT = 80

html = """
        <html>
        <body>
        <table>
        <tr> <td> left45 </td>
             <td> <a href="/forward">Forward</a> </td>
             <td> <a href="/q45right">45 right</a> </td>  </tr>
        <tr> <td> <a href="/left">Left</a> </td>
             <td> <a href="/stop">STOP</a> </td>
             <td> <a href="/right">Right</a> </td>  </tr>
        <tr> <td> 0 </td>
             <td> <a href="/backward">Backward</a> </td>
             <td> 0 </td>  </tr>
        <tr> <td> <a href="/rot_left_back">Rot left </a> </td>
             <td> <a href="/rot_center">Rot center </a> </td>
             <td> <a href="/rot_right_back">Rot right </a> </td> </tr>
        </table>
        </body>
        </html>
        """

@app.route('/')
def root(request):
    return html, {'Content-Type': 'text/html'},200

@app.route('/forward')
def forward(request):
    mecanum_motores.forward(75)
    return html, {'Content-Type': 'text/html'},200

@app.route('/q45right')
def q45_right(request):
    mecanum_motores.q45_right(75)
    return html, {'Content-Type': 'text/html'},200

@app.route('/left')
def left(request):
    mecanum_motores.lateral_left(75)
    return html, {'Content-Type': 'text/html'},200

@app.route('/stop')
def stop(request):
    mecanum_motores.stop()
    return html, {'Content-Type': 'text/html'},200

@app.route('/right')
def right(request):
    mecanum_motores.lateral_right(75)
    return html, {'Content-Type': 'text/html'},200


@app.route('/backward')
def backward(request):
    mecanum_motores.backward(75)
    return html, {'Content-Type': 'text/html'},200



@app.route('/rot_right_back')
def rot_center(request):
    mecanum_motores.rot_right_back(75)
    return html, {'Content-Type': 'text/html'},200


@app.route('/rot_center')
def rot_center(request):
    mecanum_motores.rot_center(75)
    return html, {'Content-Type': 'text/html'},200


@app.route('/rot_left_back')
def rot_left_back(request):
    mecanum_motores.rot_left_back(75)
    return html, {'Content-Type': 'text/html'},200


from network import WLAN,STA_IF
w=WLAN(STA_IF)
if w.isconnected():
    print(f'http://{w.ifconfig()[0]}:{WEB_PORT}/')
    app.run(port=WEB_PORT)
else:
    print('no network available') 