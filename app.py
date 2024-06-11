from flask import Flask, jsonify, request
import dns.resolver

app = Flask(__name__)

 
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
    try:
        # Realiza una consulta DNS para obtener todos los registros disponibles para el dominio
        respuestas = dns.resolver.resolve(nombre_dominio)
        
        # Itera sobre las respuestas y obtén la información deseada
        registros = {
            'A': [],
            'AAAA': [],
            'TXT': [],
            'CNAME': [],
            'MX': [],
            'SOA': [],
            'NS': [],
            'SRV': []
        }
        for respuesta in respuestas:
            tipo_registro = dns.rdatatype.to_text(respuesta.rdtype)
            registros[tipo_registro].append(respuesta.to_text())
        
        # Devuelve los resultados
        return jsonify({'nombre_dominio': nombre_dominio,  'registros': registros })
    except dns.resolver.NoAnswer:
        return jsonify({'error': f'No se encontraron registros {tipo_registro} para el dominio especificado'}), 404



 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
