import React, { useState } from 'react';
import axios from 'axios';
import TableComponent from './TableComponent'; // Importa el componente de tabla

const DomainSearch = () => {
  const [domain, setDomain] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const handleSubmit = async () => {
    setError('');
    setResult(null);

    try {
      const response = await axios.get(`http://127.0.0.1:5000/dns/${domain}`);
      if (response && response.data) {
        setResult(response.data);
      } else {
        setError('No se recibió una respuesta del servidor');
      }
    } catch (err) {
      setError('Error al realizar la solicitud');
    }
  };

  return (
    <div>
      <input
        type="text"
        value={domain}
        onChange={(e) => setDomain(e.target.value)}
      />
      <button onClick={handleSubmit}>Buscar</button>
      {error && <p>{error}</p>}
      {result && <TableComponent data={result.registros} />} {/* Paso los datos de los registros a TableComponent */}
    </div>
  );
};

export default DomainSearch;
