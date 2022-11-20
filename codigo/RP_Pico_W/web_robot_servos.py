# web control of 4 motors robot 

from microdot import Microdot
import robot_servos

v='0.1'
print(f'web v{v}')

app = Microdot()

WEB_PORT = 80

html = """
        <html>
        <body>
        <table>
        <tr> <td>   </td>
             <td> <a href="/forward">Forward</a> </td>
             <td>   </td>  </tr>
        <tr> <td> <a href="/left">Left</a> </td>
             <td> <a href="/stop">STOP</a> </td>
             <td> <a href="/right">Right</a> </td>  </tr>
        <tr> <td>  </td>
             <td> <a href="/backward">Backward</a> </td>
             <td>  </td>  </tr>
         </table>
        </body>
        </html>
        """

@app.route('/')
def root(request):
    return html, {'Content-Type': 'text/html'},200

@app.route('/forward')
def forward(request):
    robot_servos.forward(75)
    return html, {'Content-Type': 'text/html'},200


@app.route('/left')
def left(request):
    robot_servos.left(75)
    return html, {'Content-Type': 'text/html'},200

@app.route('/stop')
def stop(request):
    robot_servos.stop()
    return html, {'Content-Type': 'text/html'},200

@app.route('/right')
def right(request):
    robot_servos.right(75)
    return html, {'Content-Type': 'text/html'},200


@app.route('/backward')
def backward(request):
    robot_servos.backward(75)
    return html, {'Content-Type': 'text/html'},200

from network import WLAN,STA_IF
w=WLAN(STA_IF)
if w.isconnected():
    print(f'http://{w.ifconfig()[0]}:{WEB_PORT}/')
    app.run(port=WEB_PORT)
else:
    print('no network available') 