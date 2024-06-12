// App.js
import React, { useState } from 'react';
import './App.css';
import DomainSearch from './components/DomainSearch';
import TableComponent from './components/TableComponent';

function App() {
  const [registros] = useState([]);

  // Lógica para obtener registros de la API

  return (
    <div className="App">
      <h1>Domain Inventory</h1>
      <DomainSearch />
      <TableComponent registros={registros} /> {/* Pasar registros como prop */}
    </div>
  );
}

export default App;
