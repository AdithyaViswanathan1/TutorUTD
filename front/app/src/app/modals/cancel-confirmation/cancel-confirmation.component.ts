import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Appointment } from 'src/app/models/Appointment';

@Component({
  selector: 'app-cancel-confirmation',
  templateUrl: './cancel-confirmation.component.html',
  styleUrls: ['./cancel-confirmation.component.scss']
})
export class CancelConfirmationComponent {
  @Input() appointment: Appointment = {
    id: -1,
    tutor_id: -1,
    student_id: -1,
    tutor_name: '',
    student_name: '',
    time: '',
    completed: false
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
    this.cancel.emit(this.appointment.id);
  }

}
