import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ProfileService } from '../profile.service';
import { Appointment } from '../models/Appointment';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-table-demo',
  templateUrl: './table-demo.component.html',
  styleUrls: ['./table-demo.component.scss']
})
export class TableDemoComponent implements OnInit {

  tutorId: number = 0;
  fullName: string = '';
  profilePicture: File = new File([], ''); //make a default image
  courses: string[] = [];
  appointments: Appointment[] = [];
  tutorSchedule: string[] = [];

  private _subs : Subscription = new Subscription();

  constructor(
    private profileService: ProfileService,
    private route : ActivatedRoute){
      this.route.params.subscribe(params => {
      this.tutorId = params['tutorId'];
    });
  }

  ngOnInit(): void {
    this._subs.add(this.profileService.getTutorProfile(this.tutorId).subscribe(tutor => {
      this.fullName = tutor.fullName;
      if(tutor.profilePicture){
        this.profilePicture = tutor.profilePicture;
      }
      this.courses = tutor.courses;
      if(tutor.appointments){
        this.appointments = tutor.appointments;
      }
      if(tutor.tutorSchedule){
        this.tutorSchedule = tutor.tutorSchedule;
      }
    }));
  }

  ngOnDestroy(): void {
    this._subs.unsubscribe();
  }

}
