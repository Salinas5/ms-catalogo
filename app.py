import flask
import random  #para datos aleatorios
import time  
import logging

app = flask.Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#(Simulación)
PRODUCTOS_FALSOS = [
    {"id": "123", "nombre": "Teclado Mecánico RGB", "precio": 150.00},
    {"id": "456", "nombre": "Mouse Gamer Pro", "precio": 80.50},
    {"id": "789", "nombre": "Monitor Curvo 27 pulgadas", "precio": 300.00},
]

def simular_latencia():
    time.sleep(random.uniform(0.1, 0.3)) # mass rapido que el orquestador

@app.route('/api/producto/<producto_id>', methods=['GET'])
def get_producto(producto_id):
    logging.info(f"Recibida solicitud para producto ID: {producto_id}")
    
    simular_latencia()
    
    producto_elegido = random.choice(PRODUCTOS_FALSOS)
    
    logging.info(f"Retornando producto aleatorio: {producto_elegido['nombre']}")
    
    return flask.jsonify(producto_elegido), 200

if __name__ == '__main__':
    # puerto 5001
    app.run(host='0.0.0.0', port=5001, debug=True)