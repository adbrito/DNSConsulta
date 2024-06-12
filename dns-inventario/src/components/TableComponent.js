import React from 'react';

const TableComponent = ({ data }) => {
  // Verificar si data está definido antes de intentar mapearlo
  if (!data) {
    return <div>No hay datos disponibles.</div>;
  }

  return (
    <div>
      <h2>Resultados</h2>
      <table>
        <thead>
          <tr>
            <th>Tipo</th>
            <th>Datos</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item.type}</td>
              <td>{item.data}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TableComponent;
