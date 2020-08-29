import React, { Component } from 'react';
import Title from './components/Title.js'
import DayCard from './components/daylio/DayCard.js'
import data from './data/daylio.json'
import './App.css';
import { render } from '@testing-library/react';

class App extends Component {
  constructor() {
    super();
    this.state = {
      startDate : '2020-04-13',
      endDate : '2020-04-17'
    };
    this.handleClick = this.handleClick.bind(this);
    this.setStartDate = this.setStartDate.bind(this);
    this.setEndDate = this.setEndDate.bind(this);
    this.convertFromDate = this.convertFromDate.bind(this);
  }
  
  handleClick() {
    console.log('CLICK!!!!');
  }
  
  setStartDate(e) {
    this.props.setState({
      startDate : e.target.value
    });
  }
  setEndDate(e) {
    this.props.setState({
      endDate : e.target.value
    });
  }

  convertFromDate(d) {
    console.log(d.getFullYear() + '-' + (d.getMonth()+1) + '-' + d.getDate());
    return d.getFullYear() + '-' + (d.getMonth()+1) + '-' + d.getDate();
  }

  convertToDate(s) {
    
  }

  render(){
    var end = new Date(this.endDate);
    var d = new Date(this.startDate)
    console.log(d);
    console.log(end);
    console.log(d<=end);
    var index = 0;
    var cardList = [];
    for(var d = new Date(this.startDate); d > end; d.setDate(d.getDate() + 1)){
      cardList.push(
          <td style={{width:"18%"}}><DayCard day={data[this.convertFromDate(d)]}/></td>
      )
      console.log(d);
    }
    console.log(cardList);

    return (
      <div className="App">
        <Title />
        <input value={this.state.startDate} onChange={this.setStartDate}/>
        <input value={this.state.endDate} onChange={this.setEndDate} />
        <table style={{width:"100%"}}>
          <tbody>
            <tr>
              <td style={{width:"18%"}}><DayCard day={data['2020-04-17']}/></td>
              <td style={{width:"18%"}}><DayCard day={data['2020-04-16']}/></td>
              <td style={{width:"18%"}}><DayCard day={data['2020-04-15']}/></td>
              <td style={{width:"18%"}}><DayCard day={data['2020-04-14']}/></td>
              <td style={{width:"18%"}}><DayCard day={data['2020-04-13']}/></td>
            </tr>
            <tr>
              {cardList}
            </tr>
          </tbody>
        </table>
      </div>
    )
  }
}

export default App;
