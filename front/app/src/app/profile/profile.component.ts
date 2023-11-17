import { Component, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { Appointment } from '../models/Appointment';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  isStudent: boolean = true;
  tutorId: number = 0;
  fullName: string = '';
  profilePicture: File = new File([], ''); //make a default image
  courses: string[] = [];
  appointments: Appointment[] = [];
  tutorSchedule: string[] = [];
  classPrefix: string = '';
  classNumber: string = '';
  isEditing: boolean = false;
  bookingSession: boolean = true;
  biography: string = '';

  private _subs : Subscription = new Subscription();

  constructor(
    private profileService: ProfileService,
    private route : ActivatedRoute,
    private router : Router) {
      this.route.params.subscribe(params => {
      this.tutorId = params['tutorId'];
    });
    this.route.params.subscribe(params => {
      this.isStudent = params['userType'] == 'student';
    })
  }

  ngOnInit(): void {
    this._subs.add(this.profileService.getTutor(this.tutorId).subscribe(tutor => {
      this.fullName = tutor.fullName;
      this.biography = tutor.biography;
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

  addCourse() {
    if (this.classPrefix && this.classNumber) {
        const courseString = this.classPrefix + this.classNumber;
        this.courses.push(courseString);
        
        this.classPrefix = '';
        this.classNumber = '';
    }
  } 

  showTutorModal(){
    this.isEditing = true;
  }

  showStudentModal(){
    this.bookingSession = true;
  }

  closeTutorModal(){
    this.isEditing = false;
  }

  closeStudentModal(){
    this.bookingSession = false;
  }

  editName(name: string){
    this.fullName = name;
  }

  editBio(bio: string){
    this.biography = bio;
  }
}
