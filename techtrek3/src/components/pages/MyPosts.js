import React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Posts from '../Posts';

const MyPosts = () => {
    return (
        <div>
            <Typography variant="h2">
                My Posts
            </Typography>
            <Posts />
        </div>
    )
};

export default MyPosts;
