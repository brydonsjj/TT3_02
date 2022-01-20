import React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

const Post = ({ post }) => {
  return ( 
    <Box m={2}>
        <Card sx={{ maxWidth: 450 }}>
            <CardContent>
                <Typography variant="h5" component="div">
                    {post.Post_Title}
                </Typography>
                <Typography variant="body1">
                    {post.Post_Description}
                </Typography>
                { post.Post_image.includes("gif") ? 
                    <CardMedia image={post.Post_image} component="video" alt="Video" /> :
                    <CardMedia image={post.Post_image} component="img" alt="Image" />
                }
            </CardContent>
            <CardActions>
                <Button size="medium">Edit</Button>
                <Button size="medium" variant="contained">Delete</Button>
            </CardActions>
        </Card>
    </Box>
  )
};

export default Post;
