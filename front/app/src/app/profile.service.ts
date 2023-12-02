import { Injectable } from '@angular/core';
import { Tutor } from './models/Tutor';
import { Observable, of } from 'rxjs';
import { httpManager } from './httpManager';
import { Student } from './models/Student';
import { ProfileEdit } from './models/ProfileEdit';
import { Appointment } from './models/Appointment';
import { AppointmentRequest } from './models/AppointmentRequest';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  manager: httpManager;

  constructor(httpManager: httpManager) {
    this.manager = httpManager;
   }

  getTutor(id : number) : Observable<Tutor>
  {
    return this.manager.getTutor(id);
  }

  getStudent(id : number) : Observable<Student>
  {
    return this.manager.getStudent(id);
  }

  editProfile(id : number, data : ProfileEdit) : Observable<boolean>
  {
    return this.manager.editProfile(id, data);
  }

  getFavorites(id : number) : Observable<Tutor[]>
  {
    return this.manager.getFavorites(id);
  }

  toggleFavorite(studentId : number, tutorId : number, isFavorited : boolean) : Observable<boolean>
  {
    return this.manager.toggleFavorite(studentId, tutorId, isFavorited);
  }

  makeAppointment(appointmentRequest: AppointmentRequest) : Observable<boolean>
  {
    return this.manager.makeAppointment(appointmentRequest);
  }

  getAppointments(id : number, isStudent: boolean) : Observable<Appointment[]>
  {
    return this.manager.getAppointments(id, isStudent);
  }

  completeAppointment(id : number) : Observable<any>
  {
    return this.manager.completeAppointment(id);
  }

  cancelAppointment(id : number) : Observable<any>
  {
    return this.manager.cancelAppointment(id);
  }

  getStudentHours(id : number) : Observable<number>
  {
    return this.manager.getStudentHours(id);
  }

  uploadProfilePicture(file : FormData) : Observable<boolean>
  {
    return this.manager.uploadProfilePicture(file);
  }
  
}
