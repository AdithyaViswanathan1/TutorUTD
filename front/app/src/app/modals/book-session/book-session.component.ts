import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { Appointment } from 'src/app/models/Appointment';
import { BookingData } from 'src/app/models/BookingData';
import { ProfileService } from 'src/app/profile.service';

@Component({
  selector: 'app-book-session',
  templateUrl: './book-session.component.html',
  styleUrls: ['./book-session.component.scss']
})
export class BookSessionComponent implements OnInit {
  @Output() save = new EventEmitter<BookingData>();
  @Output() close = new EventEmitter();
  @Input() courses: string[] = [];
  tutorAppointments: Appointment[] = [];
  tutorSchedule: string[] = [];

  selectedTimes: string[] = [];
  selectedCourse: string = '';
  prefix: string = '';
  classNumber: string = '';

  tutorId: number = 0;

  private _subs : Subscription = new Subscription();

  constructor(private profileService: ProfileService,
    private route: ActivatedRoute){
    this.route.params.subscribe(params => {
      this.tutorId = params['tutorId'];
    });
  }

  ngOnInit(): void {
    this._subs.add(this.profileService.getTutor(this.tutorId).subscribe(tutor => {
      if(tutor.times){
        this.tutorSchedule = tutor.times;
      }
    }));

    this._subs.add(this.profileService.getAppointments(this.tutorId, false).subscribe(apts => {
      this.tutorAppointments = apts;
    }));
  }

  cancelBooking(){
    this.close.emit();
  }

  updateSelected(selected: string[]){
    this.selectedTimes = selected;
  }

  saveBooking(){
    let res : BookingData = {
      subject: this.selectedCourse.toUpperCase(),
      times: this.selectedTimes,
      location: 'Online'
    }; 
    this.save.emit(res);
  }
}
