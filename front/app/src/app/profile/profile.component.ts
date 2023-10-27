import { Component, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { Course } from '../models/Course';
import { Appointment } from '../models/Appointment';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  tutorId: number = 0;
  firstName: string = '';
  lastName: string = '';
  profilePicture: File = new File([], ''); //make a default image
  courses: Course[] = [];
  appointments: Appointment[] = [];
  tutorSchedule: string[] = [];
  classPrefix: string = '';
  classNumber: string = '';
  isEditing: boolean = false;
  biography: string = '___________________'

  private _subs : Subscription = new Subscription();

  constructor(
    private profileService: ProfileService,
    private route : ActivatedRoute,
    private router : Router) {
      this.route.params.subscribe(params => {
      this.tutorId = params['tutorId'];
    });
  }

  ngOnInit(): void {
    this._subs.add(this.profileService.getTutorProfile(this.tutorId).subscribe(tutor => {
      this.firstName = tutor.firstName;
      this.lastName = tutor.lastName;
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

  addCourse(){ //TODO: add checking to ensure fields are valid
    const newCourse: Course = {
      classPrefix: this.classPrefix,
      classNumber: parseInt(this.classNumber)
    };

    this.courses.push(newCourse);

    this.classPrefix = '';
    this.classNumber = '';
  }

}
