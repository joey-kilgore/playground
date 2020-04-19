import React, { Component } from 'react';
import dayStyles from './daylio.css'

var moodValue = {
    'rad' : 5,
    'good' : 4,
    'meh' : 3,
    'bad' : 2,
    'depressed' : 2,
    'awful' : 1
}

class DayCard extends Component {
    render(){
        console.log(this.props.day);
        const day = this.props.day;
        var sumMood = 0;
        var numMood = 0;
        for (var key of Object.keys(day)) {
            if(key != 'monthDate' && key != 'weekDay'){
                console.log(key);
                sumMood += moodValue[day[key]['mood']];
                numMood++;
            }
        }
        var avgMood = (sumMood/numMood).toFixed(1);
        return(
            <div>
                <div className={dayStyles.cardTitle}>{day.monthDate}</div>
                <p>{day.weekDay}</p>
                <p>{avgMood}/5.0</p>
            </div>
        )
    }
}

export default DayCard;