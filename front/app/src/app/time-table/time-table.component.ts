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
  selectedAppointments: any = {};

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
    for (let hour = 8; hour < 17; hour++) {
      for (let minute = 0; minute < 60; minute += 30) {
        const time = `${hour}:${minute === 0 ? '00' : minute}`;
        this.appointmentTimes.push(time);
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
    const dateTime = `${day.toISOString().split('T')[0]}T${time}:00.000Z`;
    if (this.selectedAppointments[dateTime]) {
      delete this.selectedAppointments[dateTime];
    } else {
      this.selectedAppointments[dateTime] = true;
    }
  }

  isSelected(day: Date, time: string) {
    const dateTime = `${day.toISOString().split('T')[0]}T${time}:00.000Z`;
    return !!this.selectedAppointments[dateTime];
  }

  submitAppointments() {
    // Implement logic to submit selected appointments to your server or process the data as needed
    console.log(this.selectedAppointments);
  }
  
}
