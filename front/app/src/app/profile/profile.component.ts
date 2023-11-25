import { Component, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { Appointment } from '../models/Appointment';
import { CookieService } from 'ngx-cookie-service';
import { faStar } from '@fortawesome/free-solid-svg-icons';
import { ProfileEdit } from '../models/ProfileEdit';
import { BookingData } from '../models/BookingData';
import { AppointmentRequest } from '../models/AppointmentRequest';
import { AppointmentService } from '../appointment.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  isStudent: boolean = true;
  tutorId: number = 0;
  fullName: string = '';
  profilePicture: string = '';
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
  totalHours: number = 0;
  editInput: ProfileEdit = {fullName: '', biography: '', courses: []};
  loading: boolean = false;

  faStar = faStar;

  private _subs : Subscription = new Subscription();

  constructor(
    private profileService: ProfileService,
    private appointmentService: AppointmentService,
    private route : ActivatedRoute,
    private router : Router,
    private cookieService: CookieService) {
      this.route.params.subscribe(params => {
      this.tutorId = params['tutorId'];
    });
  }

  ngOnInit(): void {
    this.loading = true;
    this.isStudent = this.cookieService.get('userType') == 'student';

    this._subs.add(this.profileService.getTutor(this.tutorId).subscribe(tutor => {
      this.loading = false;
      this.fullName = tutor.full_name;
      this.editInput.fullName = tutor.full_name;
      this.biography = tutor.biography;
      this.editInput.biography = tutor.biography;
      this.totalHours = tutor.total_hours;
      if(tutor.profile_picture){
        this.profilePicture = tutor.profile_picture;
      }
      else
      {
        this.profilePicture = 'assets/images/default.jpg';
      }
      this.courses = tutor.subjects;
      this.editInput.courses = tutor.subjects;
      if(tutor.appointments){
        this.appointments = tutor.appointments;
      }
      if(tutor.times){
        this.tutorSchedule = tutor.times;
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

  saveTutorModal(data: ProfileEdit){
    this.isEditing = false;
    
    this.profileService.editProfile(this.tutorId, data).subscribe(res => {
      this.editInput = data;
      this.fullName = data.fullName ? data.fullName : this.fullName;
      this.biography = data.biography ? data.biography : this.biography;
      this.courses = data.courses ? data.courses : this.courses;
    });
  }

  closeStudentModal(){
    this.bookingSession = false;
  }

  editSchedule(){
    this.isEditingSchedule = true;
  }

  saveSchedule(){
    this.isEditingSchedule = false;
    let data : ProfileEdit = {hours: this.tutorSchedule};
    this.profileService.editProfile(this.tutorId, data).subscribe(res => {});
  }

  updateSchedule(data : string[]){
    this.tutorSchedule = data;
  }

  bookAppointment(data: BookingData){
    let req : AppointmentRequest = {
      student_id: parseInt(this.cookieService.get('userId')),
      tutor_id: this.tutorId,
      course: data.subject,
      dates: data.times,
      location: data.location
    };
    console.log(req);
    this.appointmentService.makeAppointment(req).subscribe();
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
