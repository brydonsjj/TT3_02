import React, { useState, useEffect } from 'react';
import Grid from '@mui/material/Grid';
import Post from '../Post';

const Home = () => {
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
        <Grid backgroundColor="#F5F7FB" container justifyContent="center" alignItems="center">
            <Grid item>
                {posts.map((post, index) => (
                    <Post key={index} post={post} />
                ))}
            </Grid>
        </Grid>
    );
};

export default Home;
