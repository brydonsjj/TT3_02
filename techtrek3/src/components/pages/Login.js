import React from 'react';
import './login.css';
import { TextField, Button} from '@mui/material';

const Login = () => {
    return (
        <div className="loginPage">
            <h3 className="title">Welcome To TechTrek3</h3>
            <div className="form">
                <div></div>
                <div className="formInput">
                    <TextField
                        required
                        id="standard-required"
                        label="Username"
                        defaultValue=""
                        variant="standard"
                    />
                </div>
                <div className="formInput">
                    <TextField
                        required
                        id="standard-required"
                        label="Password"
                        defaultValue=""
                        variant="standard"
                    />
                </div>
                <div>
                    <Button type="button" variant="contained" className="form__custom-button">
                        Log in
                    </Button>
                </div>
            </div>
        </div>
    );
};

export default Login;
