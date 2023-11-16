import React, { useEffect, useState } from "react";
import axios from "axios";
import { Container, Typography, List, ListItem, ListItemText, Divider, Pagination } from "@mui/material";
import { format } from "date-fns";
import DeleteIcon from '@mui/icons-material/Delete';
import IconButton from '@mui/material/IconButton';
import ListItemSecondaryAction from '@mui/material/ListItemSecondaryAction';

export const Home = () => {
  const [message, setMessage] = useState('');
  const [user, setUser] = useState('');
  const [posts, setPosts] = useState([]);
  const [selectedPostIndex, setSelectedPostIndex] = useState(null);
  const [selectedDeletePostIndex, setSelectedDeletePostIndex] = useState(null);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  const length_pagination = 5;

  if (localStorage.getItem('access_token') === null) {
    window.location.href = '/login';
  }

  useEffect(() => {
    const fetchData = async () => {
      try {
        const postsResponse = await axios.get(`http://localhost:8000/posts/?page=${page}`);
        const userResponse = await axios.get('http://localhost:8000/users/home');

        setPosts(postsResponse.data.results);
        setUser(userResponse.data.user);
        setMessage(userResponse.data.message);
        setTotalPages(Math.ceil(postsResponse.data.count / length_pagination));
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [page]);

  const handlePostClick = (index) => {
    // Actualiza el índice del post seleccionado al hacer clic en un ListItem
    setSelectedPostIndex(selectedPostIndex === index ? null : index);
  };

  const handleDeletePostClick = (index) => {
    // Actualiza el índice del post seleccionado al hacer clic en un ListItem
    setSelectedDeletePostIndex(selectedDeletePostIndex === index ? null : index);
    const deletePost = async () => {
        try {
            const response = await axios.delete(`http://localhost:8000/posts/${posts[index].id}/`);
            window.location.href = '/';
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }
    deletePost();
  };

  const handlePageChange = (event, value) => {
    setSelectedPostIndex(null);
    setPage(value);
  };

  const formatDate = (dateString) => {
    if(!dateString) return;
    const date = new Date(dateString);
    return format(date, "dd/MM HH:mm");
  };

  return (
    <Container maxWidth="md" style={{ marginTop: '50px' }}>
      <Typography variant="h4" align="center" gutterBottom>
        Bienvenido {user.first_name} {message}
      </Typography>
        <List>
        {posts.length > 0 ? (
          posts.map((post, index) => (
            <React.Fragment key={post.id}>
              <ListItem
                alignItems="flex-start"
                button
                onClick={() => handlePostClick(index)}
              >
                <ListItemText
                  primary={post.title}
                  secondary={
                    <React.Fragment>
                      <Typography
                        component="span"
                        variant="body2"
                        color="text.primary"
                      >
                        Author: {post.author.username}
                      </Typography>
                      {` - ${formatDate(post.date_posted)}`}
                    </React.Fragment>
                  }
                />
                {user.is_admin && (
                <ListItemSecondaryAction>
                  <IconButton edge="end" aria-label="delete" onClick={() => handleDeletePostClick(index)}>
                    <DeleteIcon />
                  </IconButton>
                </ListItemSecondaryAction>)}
              </ListItem>
              {selectedPostIndex === index && (
                <Typography variant="body1" style={{ margin: '10px 0' }}>
                  {post.content}
                </Typography>
              )}
              <Divider />
            </React.Fragment>
          ))
        ) : (
          <Typography variant="body1" align="center">
            No hay posts disponibles.
          </Typography>
        )}
      </List>
      <Pagination
        count={totalPages}
        page={page}
        onChange={handlePageChange}
        color="primary"
        style={{ marginTop: '20px', display: 'flex', justifyContent: 'center' }}
      />
    </Container>
  );
};
