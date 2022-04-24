import test_measure
import parpadeo
import ventilador_automatico
#import test_dht

while True:
    
    test_measure.showSensorData_forever()
    time.sleep(1)
    #parpadeo.parpadeo()
    ventilador_automatico.ventilador()
    