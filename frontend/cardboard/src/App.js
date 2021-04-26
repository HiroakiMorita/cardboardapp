import React from 'react';
import { BrowserRouter as Router, Route} from "react-router-dom";
// import logo from './logo.svg';
import './App.css';
import Header from './components/Header';
// import Home from './components/Home';

function App() {
  return (
    <div className="App">
        <Router>
            <Route exact path="/" component={Header}></Route>
        </Router>
    </div>
  );
}


// class App extends React.Component {
//   render() {
//     return (
//       <h1>Hello World</h1>
//     );
//   }
// }

// { 
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header> }


export default App;
