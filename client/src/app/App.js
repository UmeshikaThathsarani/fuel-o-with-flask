import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { Layout } from 'antd';

import Home from './pages/home/Home';
import Prediction from './pages/prediction/Prediction';
import History from './pages/history/History';
import Rent from './pages/rent/Rent';

import AppNavBar from './components/appNavBar/AppNavBar';

// import 'antd/dist/antd.css';

import './App.css';
import AppFooter from './components/appFooter/AppFooter';

const { Content,Sider } = Layout;

function App() {
  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider>
        <div className="logo" />
        <AppNavBar />
      </Sider>
      <Layout className="page-container">
        <Content className="content-container">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/prediction" element={<Prediction />} />
            <Route path="/history" element={<History />} />
            <Route path="/rent" element={<Rent />} />
          </Routes>
        </Content>
        <AppFooter/>
      </Layout>
    </Layout>
  );
}

export default App;
