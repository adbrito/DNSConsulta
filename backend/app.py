from flask import Flask, jsonify, request
from flask_cors import CORS

import dns.resolver

app = Flask(__name__)

CORS(app)  # Configurar CORS para todas las rutas

# @app.route('/dns/<nombre_dominio>/<tipo_registro>', methods=['GET'])
# def obtener_registros_dns(nombre_dominio, tipo_registro):
#     try:
#         # Realiza una consulta DNS para obtener los registros del tipo especificado
#         respuestas = dns.resolver.resolve(nombre_dominio, tipo_registro)
        
#         # Itera sobre las respuestas y obtén la información deseada
#         registros = [respuesta.to_text() for respuesta in respuestas]
        
#         # Devuelve los resultados como JSON
#         return jsonify({'nombre_dominio': nombre_dominio, 'tipo_registro': tipo_registro, 'registros': registros})
#     except dns.resolver.NoAnswer:
#         return jsonify({'error': f'No se encontraron registros {tipo_registro} para el dominio especificado'}), 404


 
@app.route('/dns/<nombre_dominio>', methods=['GET'])
def obtener_registros_dns(nombre_dominio):
    tipos_registros = ['A', 'AAAA', 'TXT', 'CNAME', 'MX', 'SOA', 'NS', 'SRV']
    registros = []

    for tipo in tipos_registros:
        try:
            # Realiza la consulta para cada tipo de registro
            result = dns.resolver.resolve(nombre_dominio, tipo)
            
            # Convierto los resultados a una lista de diccionarios serializable a JSON
            for exdata in result:
                if tipo == 'MX':
                    registros.append({'type': tipo, 'exchange': exdata.exchange.to_text(), 'preference': exdata.preference})
                else:
                    registros.append({'type': tipo, 'data': exdata.to_text()})
        except dns.resolver.NoAnswer:
            registros.append({'type': tipo, 'error': 'No answer received'})
        except dns.resolver.NXDOMAIN:
            return jsonify({'error': 'Domain does not exist.'}), 404
        except Exception as e:
            registros.append({'type': tipo, 'error': str(e)})

    return jsonify({'nombre_dominio': nombre_dominio, 'registros': registros})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
