import React, { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Post from '../Post';

const Posts = () => {
    let postsJSON = require('../../POST.json');
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        const fetchPosts = async () => {
            try {
                setPosts(postsJSON);
            } catch (err) {
                console.log(err);
            }
        };

        fetchPosts();
    }, []);

    return (
        <Grid container justifyContent="center" alignItems="center">
            <Grid item>
                {posts.map((post, index) => (
                    <Post key={index} post={post} />
                ))}
            </Grid>
        </Grid>
    );
};

export default Posts;
