import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Appointment } from 'src/app/models/Appointment';

@Component({
  selector: 'app-cancel-confirmation',
  templateUrl: './cancel-confirmation.component.html',
  styleUrls: ['./cancel-confirmation.component.scss']
})
export class CancelConfirmationComponent {
  @Input() appointment: Appointment = {
    appointmentId: -1,
    tutorId: -1,
    studentId: -1,
    tutorName: '',
    studentName: '',
    time: ''
  };
  @Input() userType: string = '';
  @Output() cancel = new EventEmitter<number>();
  @Output() close = new EventEmitter();

  constructor() { }

  return()
  {
    this.close.emit();
  }

  confirm()
  {
    this.cancel.emit(this.appointment.appointmentId);
  }

}
