import React from 'react';
import './login.css';
import { TextField, Button, Box, Grid, Card, CardContent, Typography } from '@mui/material';

const Login = (props) => {
    return (
        <Grid container alignItems="stretch" justifyContent="center">
            <Grid item xs={12} md={6} xs={{ p: 1 }}>
                <Card raised sx={{ mt: 8, p: 4 }}>
                    <CardContent>
                        <Typography align="center" variant="h3">Welcome to Techtrek3!</Typography>
                        <Grid container direction={"column"} spacing={2} mt={2} alignItems="center" justifyContent="center">
                            <Grid item>
                                <TextField
                                    required
                                    id="standard-required"
                                    label="Username"
                                    defaultValue=""
                                />
                            </Grid>
                            <Grid item>
                                <TextField
                                    required
                                    id="standard-required"
                                    label="Password"
                                    defaultValue=""
                                    xs={{ mt: 2 }}
                                />
                            </Grid>
                            <Grid item>
                                <Button color="primary" size="large" variant="contained" type="submit" onClick={props.onLogin}>
                                    Log in
                                </Button>
                            </Grid>
                        </Grid>  
                    </CardContent>
                </Card>
            </Grid>
        </Grid>
    );
};

export default Login;
