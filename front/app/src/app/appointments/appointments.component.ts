import { Component, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { Appointment } from '../models/Appointment';

@Component({
  selector: 'app-appointments',
  templateUrl: './appointments.component.html',
  styleUrls: ['./appointments.component.scss']
})
export class AppointmentsComponent implements OnInit{

  userId: number = 0;
  appointments: Appointment[] = [];
  tutorSchedule: string[] = [];
  userType: string = '';
  userTypeInt: number = 0;

  private _subs : Subscription = new Subscription();

  constructor(
    private profileService: ProfileService,
    private route : ActivatedRoute,
    private router : Router) {
      this.route.params.subscribe(params => {
      this.userType = params['userType'];
      this.userId = params['id'];
    });
  }

  ngOnInit(): void {
    if(this.userType == 'tutor')
    {
      this.userTypeInt = 2;
      this._subs.add(this.profileService.getTutor(this.userId).subscribe(tutor => {
        if(tutor.appointments){
          this.appointments = tutor.appointments;
        }
        if(tutor.tutorSchedule){
          this.tutorSchedule = tutor.tutorSchedule;
        }
      }));
    }
    else if(this.userType == 'student')
    {
      this.userTypeInt = 1;
      this._subs.add(this.profileService.getStudent(this.userId).subscribe(student => {
        if(student.appointments){
          this.appointments = student.appointments;
        }
      }));
    }
  }

  ngOnDestroy(): void {
    this._subs.unsubscribe();
  }

}
