import React, {useState, useEffect}  from 'react';
import axios from 'axios';
import Card from '@material-ui/core/Card';
import CardMedia from '@material-ui/core/CardMedia';
import CardContent from '@material-ui/core/CardContent';
import { Typography } from '@material-ui/core';
import { NavLink } from 'react-router-dom';
// import convertFormat from '../function/Convert.js';

/**
* @author
* @function Home
**/

const Home = (props) => {
  const [articleList, setArticle] = useState([]);

  useEffect(() => {axios
      .get(`${process.env.REACT_APP_END_POINT}/api/articles/`)
        .then(res => {
            const articleList = res.data;
            setArticle(articleList);
        })
        .catch(err => {
            console.log(err);
      });
  }, [props.match.params]);

  return(
      <div>
          {
            articleList.map(article => {
              return (
                <Card
                      key={`ranking-item-${article.uuid }`}
                      style={{ maxWidth: '500px', margin: '32px auto'}}
                      src={`post/${article.uuid}`}
                >
                  <NavLink key={article.uuid} to={`/post/${article.uuid}`}>
                    <CardMedia
                      image={article.image ? process.env.REACT_APP_END_POINT+article.image: 'http://design-ec.com/d/e_others_50/l_e_others_500.png'}
                      title={article.title}
                      style={{ height: '200px' }}
                    />
                    <CardContent>
                      <Typography type="title" variant="h4">
                        {article.title}
                      </Typography>
                      <Typography className='right-placement' type="title" >
                        {/* {convertFormat(article.created_at)} */}
                      </Typography>
                    </CardContent>
                  </NavLink>
                </Card>
              )
            })
          }
        </div>
    )

  }

export default Home