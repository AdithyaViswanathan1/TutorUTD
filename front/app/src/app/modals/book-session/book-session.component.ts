import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { Appointment } from 'src/app/models/Appointment';
import { ProfileService } from 'src/app/profile.service';

@Component({
  selector: 'app-book-session',
  templateUrl: './book-session.component.html',
  styleUrls: ['./book-session.component.scss']
})
export class BookSessionComponent implements OnInit {
  @Output() cancel = new EventEmitter<number>();
  @Output() close = new EventEmitter();
  appointments: Appointment[] = [];
  tutorSchedule: string[] = [];
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
        this.appointments = tutor.appointments;
      }
      if(tutor.tutorSchedule){
        this.tutorSchedule = tutor.tutorSchedule;
      }
    }));
  }

  cancelBooking(){
    this.close.emit();
  }

  saveBooking(){
    this.close.emit();
  }
}
