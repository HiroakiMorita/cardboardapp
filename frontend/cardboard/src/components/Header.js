// import React from 'react'
import React, {useState, useEffect}  from 'react';
// import AppBar from '@material-ui/core/AppBar';
// import Toolbar from '@material-ui/core/Toolbar';
// import { Typography, Button } from '@material-ui/core';
import { Link } from 'react-router-dom';
import axios from 'axios'

/**
* @author
* @function Header
**/

const originUrl = 'http://0.0.0.0:8000';


const Header = (props) => {
    const url = new URL('/cardboardapp/', originUrl)





    return(
    <div>
        
        <h1>梱包箱判定アプリ</h1>

        <div>
            <button>ログイン</button>
            <button>サインアップ</button>
        </div>
    </div>


        // <AppBar position="static">
        //     <Toolbar>
        //         <Link to="/">
        //             <Typography variant="h4" type="title" color="inherit" >
        //                 Blog
        //             </Typography>
        //         </Link>
        //         <div style={{marginLeft: 'auto'}}>
        //             <Link to="/new">
        //                 <Button color="inherit">新規作成</Button>
        //             </Link>
        //         </div>
        //     </Toolbar>
        // </AppBar>
    )

    }


export default Header
