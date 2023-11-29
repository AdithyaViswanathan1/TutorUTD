import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Subscription } from 'rxjs';
import { Appointment } from '../models/Appointment';

@Component({
  selector: 'app-time-table',
  templateUrl: './time-table.component.html',
  styleUrls: ['./time-table.component.scss']
})
export class TimeTableComponent implements OnInit {

  @Input() tableType: number = 0; //0 = view only, 1 = tutor editing, 2 = appointment booking
  @Input() selectedTimes: string[] = [];
  @Input() appointments: Appointment[] = [];

  @Output() modified = new EventEmitter<string[]>();

  appointmentTimes: string[] = [];
  daysInWeek: Date[] = [];

  selectedAppointments: string[] = [];

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
    for (let hour = 9; hour <= 20; hour++) {
      for(let minute = 0; minute < 60; minute += 30)
      {
        let min = minute.toString();
        if(minute === 0)
        {
          min = "00";
        }
        if(hour < 12) 
        {
          const time = `${hour}:${min} AM`;
          this.appointmentTimes.push(time);
        }
        else if(hour > 12)
        {
          const time = `${hour - 12}:${min} PM`;
          this.appointmentTimes.push(time);
        }
        else
        {
          const time = `12:${min} PM`;
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
    if(this.tableType === 0) //if view only
    {
      return; 
    }
    else if(this.tableType === 1) //if tutor editing schedule
    {
      const dateTime = `${day.toDateString().split(' ')[0]}.${time}`;
      if (this.selectedTimes.includes(dateTime)) 
      {
        this.selectedTimes = this.selectedTimes.filter(time => time !== dateTime); //remove the time from the array
      } 
      else 
      {
        this.selectedTimes.push(dateTime);
      }
      this.modified.emit(this.selectedTimes);
    }
    else if(this.tableType === 2) //if student booking an appointment
    {
      const dateTime = `${day.toDateString()}.${time}`;
      const scheduleDate = `${day.toDateString().split(' ')[0]}.${time}`;
      if(this.selectedTimes.includes(scheduleDate)) //if time is in tutor schedule
      {
        if (this.selectedAppointments.includes(dateTime)) 
        {
          this.selectedAppointments = this.selectedAppointments.filter(time => time !== dateTime); //remove the time from the array
        } 
        else 
        {
          this.selectedAppointments.push(dateTime);
        }
      }  
    }   
  }

  isSelected(day: Date, time: string) { //if time is in tutor schedule
    const dateTime = `${day.toDateString().split(' ')[0]}.${time}`;
    return this.selectedTimes.includes(dateTime);
  }

  hasAppointment(day: Date, time: string) { //if slot has an existing appointment
    const dateTime = `${day.toDateString()}.${time}`;
    return this.appointments.some(appointment => appointment.time === dateTime);
  }

  isStudentSelected(day: Date, time: string) { //if current student has selected this appointment to book
    const dateTime = `${day.toDateString()}.${time}`;
    return this.selectedAppointments.includes(dateTime);
  }
  
  isInPast(day: Date) { //if time is in the past
    const today = new Date();
    return day.getDate() < today.getDate() && day.getMonth() <= today.getMonth() && day.getFullYear() <= today.getFullYear();
  }
}
