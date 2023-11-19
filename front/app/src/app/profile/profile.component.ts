import { Component, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { Appointment } from '../models/Appointment';
import { CookieService } from 'ngx-cookie-service';
import { faStar } from '@fortawesome/free-solid-svg-icons';

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
  isEditingSchedule: boolean = false;
  bookingSession: boolean = false;
  biography: string = '';
  isFavorited: boolean = false;

  faStar = faStar;

  private _subs : Subscription = new Subscription();

  constructor(
    private profileService: ProfileService,
    private route : ActivatedRoute,
    private router : Router,
    private cookieService: CookieService) {
      this.route.params.subscribe(params => {
      this.tutorId = params['tutorId'];
    });
  }

  ngOnInit(): void {
    this.isStudent = this.cookieService.get('userType') == 'student';

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

    this._subs.add(this.profileService.isFavorited(parseInt(this.cookieService.get('userId')), this.tutorId).subscribe(res => {
        this.isFavorited = res;
      }
    ));
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

  editSchedule(){
    this.isEditingSchedule = true;
  }

  saveSchedule(){
    this.isEditingSchedule = false;
    //TODO: call service to save schedule
  }

  toggleFavorite(){
    this.profileService.toggleFavorite(parseInt(this.cookieService.get('userId')), this.tutorId).subscribe(res => {
        if(res)
        {
          this.isFavorited = !this.isFavorited;
        }
      }
    );
  }
}
