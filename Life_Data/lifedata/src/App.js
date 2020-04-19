import React, { Component } from 'react';
import Title from './components/Title.js'
import DayCard from './components/daylio/DayCard.js'
import data from './data/daylio.json'
import './App.css';
import { render } from '@testing-library/react';

class App extends Component {
  render(){
    return (
      <div className="App">
        <Title />
        <table style={{width:"100%"}}>
          <tr>
            <td><DayCard day={data['2020-04-17']}/></td>
            <td><DayCard day={data['2020-04-16']}/></td>
            <td><DayCard day={data['2020-04-15']}/></td>
            <td><DayCard day={data['2020-04-14']}/></td>
            <td><DayCard day={data['2020-04-13']}/></td>
          </tr>
        </table>
      </div>
    )
  }
}

export default App;
