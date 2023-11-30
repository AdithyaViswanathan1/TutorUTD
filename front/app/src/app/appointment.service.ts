import { Injectable } from '@angular/core';
import { httpManager } from './httpManager';
import { AppointmentRequest } from './models/AppointmentRequest';
import { Observable } from 'rxjs';
import { Appointment } from './models/Appointment';

@Injectable({
  providedIn: 'root'
})
export class AppointmentService {

  constructor(private httpManager: httpManager) { }

}
