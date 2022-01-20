import React, {Component} from 'react';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import Layout from './components/pages/Layout'
import Home from './components/pages/Home'
import Login from './components/pages/Login'
import MyPosts from './components/pages/MyPosts'

class App extends Component {

    state = {
        loggedIn:false,
        userData:null
    };
    renderRoutes(){
        if (!this.state["loggedIn"]){
            return (
                <BrowserRouter>
                    <Routes>
                        <Route path="/" element={<Layout/>}>
                            <Route path="login" element={<Login onLogin={()=>this.handleLogin()}/>}/>
                            <Route path="myposts" element={<MyPosts/>}/>
                            <Route path="" element={<Home/>}/>
                            <Route path="*" element={<Home/>}/>
                        </Route>
                    </Routes>
                </BrowserRouter>
            );
        }
        else{
            return(
                <BrowserRouter>
                    <Routes>
                        <Route path="/" element={<Layout/>}>
                            <Route path="myposts" element={<MyPosts/>}/>
                            <Route path="" element={<Home/>}/>
                            <Route path="login" element={<Home/>}/>
                        </Route>
                    </Routes>
                </BrowserRouter>
            )
        }
    }


    handleLogin = () => {
        this.state["userData"] = {
            username:"user",
            password:"password"
        }
        // if valid login status
        if(this.state["userData"]["username"] == "user"){
            this.state["loggedIn"] = true

        }
        console.log(this.state);
    }
    handleLogout = () => {
        this.state["loggedIn"] = false
        this.state["userData"] = null
    }

    render() {

        return (
            <div>
                {this.renderRoutes()}
            </div>
        );
    }
};

export default App;
