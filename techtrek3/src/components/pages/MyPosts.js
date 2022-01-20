import React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

const Post = () => {
  return (
    <div>
        <Card sx={{ maxWidth: 450 }}>
            <CardContent>
                <Typography variant="h5" component="div">
                    Post Title
                </Typography>
                <Typography variant="body1">
                    Post Description
                </Typography>
                <CardMedia>
                Post Picture
                </CardMedia>
            </CardContent>
            <CardActions>
                <Button size="medium">Edit</Button>
                <Button size="medium" variant="contained">Delete</Button>
            </CardActions>
        </Card>
    </div>
  )
};

export default Post;
