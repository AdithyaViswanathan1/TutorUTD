import { Component, EventEmitter, OnInit, Output } from '@angular/core';
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
  tutorAppointments: Appointment[] = [];
  tutorSchedule: string[] = [];

  selectedTimes: string[] = [];
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
      if(tutor.appointments){
        this.tutorAppointments = tutor.appointments;
      }
      if(tutor.times){
        this.tutorSchedule = tutor.times;
      }
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
      subject: this.prefix.toUpperCase() + ' ' + this.classNumber,
      times: this.selectedTimes,
      location: 'Online'
    }; 
    this.save.emit(res);
  }
}
