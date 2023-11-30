import { Component, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { Appointment } from '../models/Appointment';
import { CookieService } from 'ngx-cookie-service';

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

  showCancelConfirmation: boolean = false;
  cancelId: number = -1;
  cancelApt: Appointment = {
    id: -1,
    tutor_id: -1,
    student_id: -1,
    tutor_name: '',
    student_name: '',
    time: '',
    completed: false
  };

  loading: boolean = false;

  private _subs : Subscription = new Subscription();

  constructor(
    private profileService: ProfileService,
    private route : ActivatedRoute,
    private router : Router,
    private cookieService: CookieService) {
      this.userId = parseInt(this.cookieService.get('userId'));
      this.userType = this.cookieService.get('userType');
    }

  ngOnInit(): void {
    this.loading = true;
    if(this.userType == 'tutor')
    {
      this.userTypeInt = 2;
      this._subs.add(this.profileService.getTutor(this.userId).subscribe(tutor => {
        this.loading = false;
        if(tutor.times){
          this.tutorSchedule = tutor.times;
        }
      }));
      this._subs.add(this.profileService.getAppointments(this.userId, false).subscribe(apts => {
        this.appointments = apts;
      }));
      
    }
    else if(this.userType == 'student')
    {
      this.userTypeInt = 1;
      this._subs.add(this.profileService.getAppointments(this.userId, true).subscribe(apts => {
        this.appointments = apts;
        this.loading = false;
      }));
    }
  }

  ngOnDestroy(): void {
    this._subs.unsubscribe();
  }

  toTutorProfile(id : number){
    this.router.navigate(['/profile', id]);
  }

  showModal(id : number){
    console.log("showing modal for id: " + id)
    this.showCancelConfirmation = true;
    this.cancelId = id;
    this.cancelApt = this.appointments.find(a => a.id == id)!;
  }

  closeModal(){
    this.showCancelConfirmation = false;
  }

  cancelAppointment(id : number){
    console.log("cancelling id: " + id);
    this.showCancelConfirmation = false;
    this.profileService.cancelAppointment(id).subscribe(res => {
      this.appointments = this.appointments.filter(a => a.id != id);
    });
  }

  completeAppointment(id : number){
    console.log("completing id: " + id);
    this.profileService.completeAppointment(id).subscribe(res => {
      this.appointments = this.appointments.filter(a => a.id != id);
    });
  }

}
