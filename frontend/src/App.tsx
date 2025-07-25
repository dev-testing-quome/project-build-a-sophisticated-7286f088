import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ContractListPage from './pages/ContractListPage';

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<ContractListPage />} />
        {/* Add more routes as needed */}
      </Routes>
    </BrowserRouter>
  );
};

export default App;