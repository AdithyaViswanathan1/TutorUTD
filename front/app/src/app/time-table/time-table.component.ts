import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-time-table',
  templateUrl: './time-table.component.html',
  styleUrls: ['./time-table.component.scss']
})
export class TimeTableComponent implements OnInit {

  @Input() tableType: number = 0; //0 = view only, 1 = tutor editing, 2 = appointment booking

  daysInWeek: Date[] = [];
  appointmentTimes: string[] = [];

  selectedTimes: string[] = [];

  constructor() {

  }
  ngOnInit(): void {
    this.initWeek();
    this.initTimes();
  }

  initWeek() {
    const today = new Date();
    for (let i = 0; i < 7; i++) {
      const day = new Date(today);
      day.setDate(today.getDate() + i);
      this.daysInWeek.push(day);
    }
  }

  initTimes() {
    for (let hour = 8; hour < 20; hour++) {
      for (let minute = 0; minute < 60; minute += 30) {
        if(hour < 12) 
        {
          const time = `${hour}:${minute === 0 ? '00' : minute} AM`;
          this.appointmentTimes.push(time);
        }
        else if(hour > 12)
        {
          const time = `${hour - 12}:${minute === 0 ? '00' : minute} PM`;
          this.appointmentTimes.push(time);
        }
        else
        {
          const time = `${hour}:${minute === 0 ? '00' : minute} PM`;
          this.appointmentTimes.push(time);
        }
        
      }
    }
  }

  previousWeek() {
    this.daysInWeek = this.daysInWeek.map(day => {
      const newDay = new Date(day);
      newDay.setDate(day.getDate() - 7);
      return newDay;
    });
  }

  nextWeek() {
    this.daysInWeek = this.daysInWeek.map(day => {
      const newDay = new Date(day);
      newDay.setDate(day.getDate() + 7);
      return newDay;
    });
  }

  toggleSelection(day: Date, time: string) {
    const dateTime = `${day.toISOString().split('T')[0]}T${time}`;
    if (this.selectedTimes.includes(dateTime)) {
      this.selectedTimes = this.selectedTimes.filter(time => time !== dateTime);
    } else {
      this.selectedTimes.push(dateTime);
    }
  }

  isSelected(day: Date, time: string) {
    const dateTime = `${day.toISOString().split('T')[0]}T${time}`;
    return this.selectedTimes.includes(dateTime);
  }
  
}
