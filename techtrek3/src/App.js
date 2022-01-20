import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from './components/pages/Layout'
import Home from './components/pages/Home'
import Login from './components/pages/Login'
import MyPosts from './components/pages/MyPosts'

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route path="login" element={<Login />} />
          <Route path="myposts" element={<MyPosts />} />
          <Route path="*" element={<Home />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default App;
